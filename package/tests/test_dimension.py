from core.noise_aug import noise_aug

def test_noise_aug():
    """ Checks whether the dimension of the original data is equal to the augmented data. """
    
    shape = data.shape[0]
    augmented_shape = noise_aug(noise_type,
                                data,
                                snr,
                                rate,
                                snr_thres = 10,
                                rate_thres = 1,
                                scale_params = {
                                "low_bound_gauss": 0.01, 
                                "up_bound_gauss": 0.15, 
                                "scale_expo": 4,
                                "scale_rayleigh":4}).shape[0]
    
    
    assert shape == augmented_shape 
