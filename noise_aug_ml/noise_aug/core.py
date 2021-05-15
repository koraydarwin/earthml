import numpy as np

SCALE_AND_THRES_PARAMS = {"low_bound_gauss": 0.01, "up_bound_gauss": 0.15, "scale": 4, "snr_thres":10, "rate_thres":1}
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
       
    scale_params_main: dict (optional) {"low_bound_gauss": None, "up_bound_gauss": None, "scale": None}
       "low_bound_gauss" which determines lower bound of the interval for standard deviation of additive_gaussian function. 
       It is for additive_gaussian and its default value is 0.01.
       
       "up_bound_gauss" which determines upper bound of the interval for standard deviation of additive_gaussian function. 
       It is for additive_gaussian and its default value is 0.15.
       
       "scale" which is scale value for "multiplicative_exponential", "multiplicative_rayleigh" and "additive_exponential" functions and its default value is 4.
       
       
    '''
    
    if scale_params_main is None:
        scale_params_main = SCALE_AND_THRES_PARAMS
        
    if noise_type == "additive_gaussian":
        noise_augmented = gauss_add_noise(data, snr, rate, scale_params = scale_params_main)
    elif noise_type == "multiplicative_exponential":
        noise_augmented = exp_mult_noise(data, snr, rate, scale_params = scale_params_main)
    elif noise_type == "multiplicative_rayleigh":
        noise_augmented = ray_mult_noise(data, snr, rate, scale_params = scale_params_main)
    elif noise_type == "additive_exponential":
        noise_augmented = exp_add_noise(data, snr, rate, scale_params = scale_params_main)
    else:
        raise NameError(noise_type  + " " +  "could not be found, enter valid noise_type")
    return noise_augmented


GAUSS_DEFAULT_SCALE_PARAMS = {"low_bound_gauss": 0.01, "up_bound_gauss": 0.15}          
def gauss_add_noise(data, snr, rate, scale_params = None):
    if scale_params is None:
        scale_params = GAUSS_DEFAULT_SCALE_PARAMS
    '''Apply additive Gaussian noise with a random scale variable onto raw waveform data; scale_params = {low_bound_gauss: None, up_bound_gauss: None}'''
    data_noisy = np.empty(data.shape)
    if np.random.uniform(0, scale_params["rate_thres"]) < rate and snr >= scale_params["snr_thres"]: 
        data_noisy = np.empty((data.shape))
        for i in range(3):
            data_noisy[:, i] = data[:,i] + np.random.normal(0, np.random.uniform(scale_params["low_bound_gauss"], 
                                                                             scale_params["up_bound_gauss"])*max(data[:,0]), data.shape[0]) 
    else:
        data_noisy = data
    return data_noisy 

EXP_AND_RAY_DEFAULT_SCALE_PARAMS = {"scale": 4}    
def exp_mult_noise(data, snr, rate, scale_params = None):
    if scale_params is None:
        scale_params = EXP_AND_RAY_DEFAULT_SCALE_PARAMS 
    '''Apply multiplicative exponential noise with a random scale value onto raw waveform data; scale_params = {scale: None}'''
    data_noisy = np.empty(data.shape)
    if np.random.uniform(0, scale_params["rate_thres"]) < rate and snr >= scale_params["snr_thres"]: 
        data_noisy = np.empty((data.shape))
        data_noisy = data * (1 + np.random.exponential(scale_params['scale'], data.shape))
    else:
        data_noisy = data
    return data_noisy   

def ray_mult_noise(data, snr, rate, scale_params = None):
    '''Apply multiplicative Rayleigh noise with a random scale value onto raw waveform data; scale_params = {scale: None}'''
    if scale_params is None:
        scale_params = EXP_AND_RAY_DEFAULT_SCALE_PARAMS 
    data_noisy = np.empty(data.shape)
    if np.random.uniform(0, scale_params["rate_thres"]) < rate and snr >= scale_params["snr_thres"]: 
        data_noisy = np.empty((data.shape))
        data_noisy = data * (1 + np.random.rayleigh(scale_params['scale'], data.shape))
    else:
        data_noisy = data
    return data_noisy   

def exp_add_noise(data, snr, rate, scale_params = None):
    if scale_params is None:
        scale_params = EXP_AND_RAY_DEFAULT_SCALE_PARAMS
    '''Apply additive exponential noise with a random scale variable onto raw waveform data; scale_params = {scale: None}'''
    data_noisy = np.empty(data.shape)
    if np.random.uniform(0, scale_params["rate_thres"]) < rate and snr >= scale_params["snr_thres"]: 
        data_noisy = np.empty((data.shape))
        signs = np.random.choice([-1,1],data.shape)
        data_noisy = data + signs * np.random.exponential(scale_params['scale'], data.shape)
    else:
        data_noisy = data
    return data_noisy   

  
