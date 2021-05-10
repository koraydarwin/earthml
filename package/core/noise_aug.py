import numpy as np

def noise_aug(noise_type,
              data,
              snr,
              rate,
              snr_thres = 10,
              rate_thres = 1,
              scale_params = {
              "low_bound_gauss": 0.01, 
              "up_bound_gauss": 0.15, 
              "scale_expo": 4,
              "scale_rayleigh":4}
              ):
     
    '''
    
    noise_type: str
       additive_gaussian or multiplicative_exponential, multiplicative_rayleigh or additive_exponential
    
    data: 
       data which will be augmented.
       
    snr: float or int
       signal to noise ratio.
       
    rate: float or int
       rate of augmentation
    
    rate_thres: float or int
       rate threshold to be augmented     
       
    snr_thres: float or int
       signal to noise threshold to be augmented.
       
    scale_params: dict (optional)
       "low_bound_gauss" which determines lower bound of the interval for standard deviation of additive_gaussian function. 
       It is for additive_gaussian and its default value is 0.01.
       
       "up_bound_gauss" which determines upper bound of the interval for standard deviation of additive_gaussian function. 
       It is for additive_gaussian and its default value is 0.15.
       
       "scale_expo" which is scale value for multiplicative_exponential and additive_exponential function and its default value is 4.
       
       "scale_rayleigh" which is scale value for multiplicative_rayleigh function and its default value is 4.
       
       
    '''
        
    if noise_type == "additive_gaussian":
        
        noise_augmented = gauss_add_noise(data, snr, rate, snr_thres, rate_thres, scale_params = {"low_bound_gauss": 0.01, "up_bound_gauss": 0.15})
        
    elif noise_type == "multiplicative_exponential":
        
        noise_augmented = expo_mult_noise(data, snr, rate, snr_thres, rate_thres, scale_params = {"scale_expo": 4})
        
    elif noise_type == "multiplicative_rayleigh":
        
        noise_augmented = ray_mult_noise(data, snr, rate, snr_thres, rate_thres, scale_params = {"scale_rayleigh":4})
        
    elif noise_type == "additive_exponential":
        
        noise_augmented = expo_add_noise(data, snr, rate, snr_thres, rate_thres, scale_params = {"scale_expo": 4})
    
    else:
        
        raise NameError(noise_type  + " " + + "could not be found, enter valid noise_type")
        
        
    return noise_augmented


        
def gauss_add_noise(data, snr, rate, snr_thres, rate_thres, scale_params = {"low_bound_gauss": 0.01, "up_bound_gauss": 0.15}):
            
    'Randomly add Gaussian noise onto waveforms.'
            
    data_noisy = np.empty((data.shape))
    if np.random.uniform(0, rate_thres) < rate and all(snr >= snr_thres): 
        data_noisy = np.empty((data.shape))
        data_noisy[:, 0] = data[:,0] + np.random.normal(0, np.random.uniform(scale_params["low_bound_gauss"], 
                                                                             scale_params["up_bound_gauss"])*max(data[:,0]), data.shape[0])
        data_noisy[:, 1] = data[:,1] + np.random.normal(0, np.random.uniform(scale_params["low_bound_gauss"], 
                                                                             scale_params["up_bound_gauss"])*max(data[:,1]), data.shape[0])
        data_noisy[:, 2] = data[:,2] + np.random.normal(0, np.random.uniform(scale_params["low_bound_gauss"], 
                                                                             scale_params["up_bound_gauss"])*max(data[:,2]), data.shape[0])    
    else:
        data_noisy = data
                
    return data_noisy 


  
def expo_mult_noise(data, snr, rate, snr_thres, rate_thres, scale_params = {"scale_expo": 4}):
            
    'Randomly add multiplicative exponential noise onto waveforms.'
            
    data_noisy = np.empty((data.shape))
    if np.random.uniform(0, rate_thres) < rate and all(snr >= snr_thres): 
        data_noisy = np.empty((data.shape))
        data_noisy[:, 0] = data[:,0] * (1 + np.random.exponential(scale_params["scale_expo"], data.shape[0]))
        data_noisy[:, 1] = data[:,1] * (1 + np.random.exponential(scale_params["scale_expo"], data.shape[0]))
        data_noisy[:, 2] = data[:,2] * (1 + np.random.exponential(scale_params["scale_expo"], data.shape[0])) 
    else:
        data_noisy = data
            
    return data_noisy   


def ray_mult_noise(data, snr, rate, snr_thres, scale_params = {"scale_rayleigh": 4}):

    'Randomly add multiplicative Rayleigh noise onto waveforms.'
    
    data_noisy = np.empty((data.shape))
    if np.random.uniform(0, rate_thres) < rate and all(snr >= snr_thres): 
        data_noisy = np.empty((data.shape))
        data_noisy[:, 0] = data[:,0] * (1 + np.random.rayleigh(scale_params["scale_rayleigh"], data.shape[0]))
        data_noisy[:, 1] = data[:,1] * (1 + np.random.rayleigh(scale_params["scale_rayleigh"], data.shape[0]))
        data_noisy[:, 2] = data[:,2] * (1 + np.random.rayleigh(scale_params["scale_rayleigh"], data.shape[0])) 
    else:
        data_noisy = data
            
    return data_noisy   


def expo_add_noise(data, snr, rate, snr_thres, rate_thres, scale_params = {"scale_expo": 4}):
            
    'Randomly add exponential noise onto waveforms.'
            
    data_noisy = np.empty((data.shape))
    if np.random.uniform(0, rate_thres) < rate and all(snr >= snr_thres): 
        data_noisy = np.empty((data.shape))
        signs = np.random.choice([-1,1],data.shape[0])
        data_noisy[:, 0] = data[:,0] + (signs*np.random.exponential(scale_params["scale_expo"], data.shape[0]))
        data_noisy[:, 1] = data[:,1] + (signs*np.random.exponential(scale_params["scale_expo"], data.shape[0]))
        data_noisy[:, 2] = data[:,2] + (signs*np.random.exponential(scale_params["scale_expo"], data.shape[0])) 
    else:
        data_noisy = data
            
    return data_noisy   

    
