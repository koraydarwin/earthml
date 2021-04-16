def noise_aug(noise_type,
              data,
              snr,
              rate,
              snr_thres = 10,
              rate_thres = 1,
              low_bound_gauss = None, 
              up_bound_gauss = None, 
              scale_expo = None):
    
    
    '''
    
    noise_type: str
       additive_gaussian or multiplicative_exponential
    
    data: 
       data which will be augmented.
       
    snr: float or int
       signal to noise ratio.
       
    rate: float or int
    
    rate_thres: float or int
       rate threshold to be augmented     
       
    snr_thres: float or int
       signal to noise threshold to be augmented.
       
    low_bound_gauss: float
       lower bound of interval which determines the standard deviation of additive_gaussian function.
       
    up_bound_gauss: float
       upper bound of interval which determines the standard deviation of additive_gaussian function.
       
    scale_expo: float or int
       scale value for multiplicative_exponential function.

    '''
    
    
    
    
    if noise_type == "additive_gaussian":
        
        def gauss_add_noise(data):
            
            'Randomly add Gaussian noise onto waveforms.'
            
            data_noisy = np.empty((data.shape))
            if np.random.uniform(0, rate_thres) < rate and all(snr >= snr_thres): 
                data_noisy = np.empty((data.shape))
                data_noisy[:, 0] = data[:,0] + np.random.normal(0, np.random.uniform(low_bound_gauss, up_bound_gauss)*max(data[:,0]), data.shape[0])
                data_noisy[:, 1] = data[:,1] + np.random.normal(0, np.random.uniform(low_bound_gauss, up_bound_gauss)*max(data[:,1]), data.shape[0])
                data_noisy[:, 2] = data[:,2] + np.random.normal(0, np.random.uniform(low_bound_gauss, up_bound_gauss)*max(data[:,2]), data.shape[0])    
            else:
                data_noisy = data
                
            return data_noisy 
    
        noise_augmented = gauss_add_noise(data)
    
    
    
    elif noise_type == "multiplicative_exponential":
        
        def expo_add_noise(data):
            
            'Randomly add exponential noise onto waveforms.'
            
            data_noisy = np.empty((data.shape))
            if np.random.uniform(0, rate_thres) < rate and all(snr >= snr_thres): 
                data_noisy = np.empty((data.shape))
                data_noisy[:, 0] = data[:,0] * (1 + np.random.exponential(scale_expo, data.shape[0]))
                data_noisy[:, 1] = data[:,1] * (1 + np.random.exponential(scale_expo, data.shape[0]))
                data_noisy[:, 2] = data[:,2] * (1 + np.random.exponential(scale_expo, data.shape[0])) 
            else:
                data_noisy = data
            
            return data_noisy 
        
        
        noise_augmented = expo_add_noise(data)
    
    
    
    else:
        raise NameError("noise_type could not be found, enter valid noise_type")
        
        
        
    
    return noise_augmented
