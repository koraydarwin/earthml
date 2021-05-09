from package.core import noise_aug

def test_noise_aug():
    
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
                                "scale_expo": 4}).shape[0]
    
    
    assert shape == augmented_shape 
