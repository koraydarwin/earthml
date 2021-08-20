import numpy as np

NOISE_TYPES = (
    "additive_gaussian",
    "additive_exponential", 
    "additive_rayleigh",
    "multiplicative_exponential",
    "multiplicative_rayleigh")

ADDITIVE_DEFAULT_PARAMS = {
    "up_bound_scale"  : 0.15,
    "low_bound_scale" : 0.01,
    "snr_thres"       : 10,
    "rate_thres"      : 1}   

MULTIPLICATIVE_DEFAULT_PARAMS = {
    "scale"      : 4,
    "snr_thres"  : 10,
    "rate_thres" : 1}

NOISE_TYPE2DEFAULT_PARAMS = {
    "additive_gaussian"           : ADDITIVE_DEFAULT_PARAMS,
    "additive_exponential"        : ADDITIVE_DEFAULT_PARAMS,
    "additive_rayleigh"           : ADDITIVE_DEFAULT_PARAMS,
    "multiplicative_exponential"  : MULTIPLICATIVE_DEFAULT_PARAMS,
    "multiplicative_rayleigh"     : MULTIPLICATIVE_DEFAULT_PARAMS}

def noise_aug(data,
              noise_type,
              snr,
              rate,
              scale_params = None):
    '''Return a noisy version of data for a fraction (`rate`) of the data
    samples if snr > scale_params['snr_threshold']. For the remaining
    fraction, return original data unchanged. Also return original
    data if snr is lower than the threshold.
    Arguments:
    noise_type: str
       One of "additive_gaussian",  "additive_exponential", "additive_rayleigh",
       "multiplicative_exponential", "multiplicative_rayleigh"
    data: numpy array 
       XXX TODO check shape (also:could this be an hdf5 file?)
       data to be augmented, shape: (num_samples, num_channels)
       
    snr: float or int
       the ratio of the power of a signal (meaningful or desired input) to the
       power of noise (meaningless or unwanted input).
       XXX TODO clarify meaning
       
    rate: float or int
       rate of augmentation
       XXX TODO clarify meaning
    
    snr_thres: float or int
       signal to noise threshold to be augmented.
       XXX TODO clafify meaning
       
    scale_params: dict (optional) 
       sets scale parameters for the type of noise to be used. possible keys:
       "low_bound_scale", "up_bound_scale", "scale", "snr_thres"
       XXX TODO snr_thres is not really a "scale parameter"
    Returns:
    NumPy array with the shape of the original data argument.
    '''
    assert noise_type in NOISE_TYPES
    if scale_params is None:
        scale_params = NOISE_TYPE2DEFAULT_PARAMS[noise_type]
    _check_options(noise_type, scale_params)

    if np.random.uniform(0, 1) < rate and snr >= scale_params["snr_thres"]: 
        noise_func = NOISE_TYPE2FUNC[noise_type]
        noise_augmented = noise_func(data = data, scale_params = scale_params)
    else:
        noise_augmented = data
    return noise_augmented
                 
def _check_options(noise_type, scale_params_main):
    assert noise_type in NOISE_TYPES
    if noise_type in ["additive_gaussian", "additive_exponential", "additive_rayleigh"]:
        if "scale" in scale_params_main:
            raise ValueError("%s does not use scale" % noise_type)
    elif (("low_bound_scale" in scale_params_main) or
          ("up_bound_scale" in scale_params_main)):
        raise ValueError(
            "%s does not use low_bound_scale or up_bound_scale" % noise_type)

def gauss_add_noise(data, scale_params):
    '''Apply additive Gaussian noise with a random scale variable onto 
    raw waveform data'''
    data_noisy = np.empty(data.shape)
    num_samples, num_channels = data.shape
    for i in range(num_channels):
        channel_scale = np.random.uniform(
            scale_params["low_bound_scale"], 
            scale_params["up_bound_scale"])
        noise = np.random.normal(0, channel_scale * max(data[:,i]), num_samples)
        data_noisy[:, i] = data[:,i] + noise
    return data_noisy 

def exp_add_noise(data, scale_params):
    '''Apply additive exponential noise with a random scale variable onto
    raw waveform data'''
    data_noisy = np.empty(data.shape)
    num_samples, num_channels = data.shape
    signs = np.random.choice([-1,1], data.shape)
    for i in range(num_channels):
        channel_scale = np.random.uniform(
            scale_params["low_bound_scale"], 
            scale_params["up_bound_scale"])
        noise = signs[:,i] * np.random.exponential(channel_scale * max(data[:,i]), num_samples)
        data_noisy[:, i] = data[:,i] + noise
    return data_noisy 

def ray_add_noise(data, scale_params):
    '''Apply additive Rayleigh noise with a random scale variable onto
    raw waveform data'''
    data_noisy = np.empty(data.shape)
    num_samples, num_channels = data.shape
    signs = np.random.choice([-1,1], data.shape)
    for i in range(num_channels):
        channel_scale = np.random.uniform(
            scale_params["low_bound_scale"], 
            scale_params["up_bound_scale"])
        noise = signs[:,i] * np.random.rayleigh(channel_scale * max(data[:,i]), num_samples)
        data_noisy[:, i] = data[:,i] + noise
    return data_noisy 

def exp_mult_noise(data, scale_params):
    '''Apply multiplicative exponential noise with a scale value determined by
    scale_params['scale'] onto raw waveform data'''
    data_noisy = np.empty(data.shape)
    noise_fac = 1 + np.random.exponential(scale_params['scale'], data.shape)
    data_noisy = data * noise_fac
    return data_noisy   

def ray_mult_noise(data, scale_params):
    '''Apply multiplicative Rayleigh noise with a scale value determined by
    scale_params['scale'] onto raw waveform data'''
    data_noisy = np.empty(data.shape)
    noise_fac = 1 + np.random.rayleigh(scale_params['scale'], data.shape)
    data_noisy = data * noise_fac
    return data_noisy

NOISE_TYPE2FUNC = {
    'additive_gaussian'          : gauss_add_noise,
    "additive_exponential"       : exp_add_noise,
    "additive_rayleigh"          : ray_add_noise,
    "multiplicative_exponential" : exp_mult_noise,
    "multiplicative_rayleigh"    : ray_mult_noise}
