import numpy as np

def noise_aug(noise_type,
              data,
              snr,
              rate,
              scale_params_main = None):
     
    '''
    
    noise_type: str
       "additive_gaussian" or "multiplicative_exponential", "multiplicative_rayleigh" or "additive_exponential"
    
    data: 
       data, it can be .hdf5 file or numpy array which will be augmented 
       
    snr: float or int
       the ratio of the power of a signal (meaningful or desired input) to the power of noise (meaningless or unwanted input).
       
    rate: float or int
       rate of augmentation
    
    rate_thres: float or int
       rate threshold to be augmented     
       
    snr_thres: float or int
       signal to noise threshold to be augmented.
       
    scale_params_main: dict (optional) {"low_bound_gauss": None, "up_bound_gauss": None, "scale": None, "snr_thres": None, "rate_thres":1}
       "low_bound_gauss" which determines lower bound of the interval for standard deviation of additive_gaussian function. 
       It is for additive_gaussian and its default value is 0.01.
       
       "up_bound_gauss" which determines upper bound of the interval for standard deviation of additive_gaussian function. 
       It is for additive_gaussian and its default value is 0.15.
       
       "scale" which is scale value for "multiplicative_exponential", "multiplicative_rayleigh" and "additive_exponential" functions and its default value is 4.
       
       "snr_thres" which is threshold value for be augmented; its default value is 10. If it is greater than 10, it will be augmented.
       
       "rate_thres" which is threshold value for be augmented; its default value is 1. If it is greater than 1, it will be augmented.
       
       
    '''
    
    def check_options(noise_type):
        if noise_type == "additive_gaussian" and "scale" in scale_params_main:
            raise ValueError("additive_gaussian noise does not use scale parameter")
        elif noise_type == "multiplicative_exponential" and (("low_bound_gauss" in scale_params_main) or ("up_bound_gauss" in scale_params_main)):
            raise ValueError("multiplicative_exponential noise does not use low_bound_gauss or up_bound_gauss parameter")
        elif noise_type == "multiplicative_rayleigh" and (("low_bound_gauss" or "up_bound_gauss") in scale_params_main):
            raise ValueError("multiplicative_rayleigh noise does not use low_bound_gauss or up_bound_gauss parameter")
        elif noise_type == "additive_exponential" and (("low_bound_gauss" or "up_bound_gauss") in scale_params_main):
            raise ValueError("additive_exponential noise does not use low_bound_gauss or up_bound_gauss parameter")
        else:
            return scale_params_main
            
    def _set_default_params(noise_type):
        if noise_type == "additive_gaussian":
            scale_params_main = {"low_bound_gauss": 0.01, "up_bound_gauss": 0.15, "snr_thres":10, "rate_thres":1}   
        elif noise_type == "multiplicative_exponential":
            scale_params_main = {"scale":4, "snr_thres":10, "rate_thres":1}
        elif noise_type == "multiplicative_rayleigh":
            scale_params_main = {"scale":4, "snr_thres":10, "rate_thres":1}
        elif noise_type == "additive_exponential":
            scale_params_main = {"scale":4, "snr_thres":10, "rate_thres":1}
        else:
            raise ValueError(noise_type  + " " +  "could not be found, enter valid noise_type")
        return scale_params_main
           
    
    if scale_params_main is None:
        scale_params_main = _set_default_params(noise_type)
    else:
        scale_params_main = check_options(noise_type)
        
        
    if np.random.uniform(0, scale_params_main["rate_thres"]) < rate and snr >= scale_params_main["snr_thres"]: 
            if noise_type == "additive_gaussian":
                noise_augmented = gauss_add_noise(data, snr, rate, scale_params = scale_params_main)
            elif noise_type == "multiplicative_exponential":
                noise_augmented = exp_mult_noise(data, snr, rate, scale_params = scale_params_main)
            elif noise_type == "multiplicative_rayleigh":
                noise_augmented = ray_mult_noise(data, snr, rate, scale_params = scale_params_main)
            elif noise_type == "additive_exponential":
                noise_augmented = exp_add_noise(data, snr, rate, scale_params = scale_params_main)
            else:
                raise ValueError(noise_type  + " " +  "could not be found, enter valid noise_type")
    else:
        noise_augmented = data
    return noise_augmented
                 
def gauss_add_noise(data, snr, rate, scale_params = None):
    '''Apply additive Gaussian noise with a random scale variable onto raw waveform data; scale_params = 
                                                          {low_bound_gauss: None, up_bound_gauss: None,"snr_thres":None, "rate_thres":None}'''
    data_noisy = np.empty(data.shape)
    num_chan = data.shape[1]
    for i in range(num_chan):
        data_noisy[:, i] = data[:,i] + np.random.normal(0, np.random.uniform(scale_params["low_bound_gauss"], 
                                                                             scale_params["up_bound_gauss"])*max(data[:,i]), data.shape[0]) 
    return data_noisy 
   
def exp_mult_noise(data, snr, rate, scale_params = None):
    '''Apply multiplicative exponential noise with a random scale value onto raw waveform data; scale_params = 
                                                                         {scale: None, "snr_thres":None, "rate_thres":None}'''
    data_noisy = np.empty(data.shape)
    data_noisy = data * (1 + np.random.exponential(scale_params['scale'], data.shape))
    return data_noisy   

def ray_mult_noise(data, snr, rate, scale_params = None):
    '''Apply multiplicative Rayleigh noise with a random scale value onto raw waveform data; scale_params = 
                                                                         {scale: None, "snr_thres":None, "rate_thres":None}'''
    data_noisy = np.empty(data.shape)
    data_noisy = data * (1 + np.random.rayleigh(scale_params['scale'], data.shape))
    return data_noisy   

def exp_add_noise(data, snr, rate, scale_params = None):
    '''Apply additive exponential noise with a random scale variable onto raw waveform data; scale_params = 
                                                                         {scale: None, "snr_thres":None, "rate_thres":None}'''
    data_noisy = np.empty(data.shape)
    signs = np.random.choice([-1,1],data.shape)
    data_noisy = data + signs * np.random.exponential(scale_params['scale'], data.shape)
    return data_noisy   
