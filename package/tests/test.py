import numpy as np
from core.noise_aug import noise_aug

data = np.random.randint(10, size = (4,3))


def test_random():
  """ Checks whether the functions in noise_aug return the same noisy_data """

  
  np.random.seed(3)
  augmented1 = noise_aug("multiplicative_exponential",
              data,
              11,
              2,
              snr_thres = 10,
              rate_thres = 1,
              scale_params = {
              "low_bound_gauss": 0.01, 
              "up_bound_gauss": 0.15, 
              "scale_exp": 4,
              "scale_rayleigh":4}
              )
  
  np.random.seed(3)
  augmented2 = noise_aug("multiplicative_exponential",
              data,
              11,
              2,
              snr_thres = 10,
              rate_thres = 1,
              scale_params = {
              "low_bound_gauss": 0.01, 
              "up_bound_gauss": 0.15, 
              "scale_exp": 4,
              "scale_rayleigh":4}
              )
  
  assert (augmented1 == augmented2).all()



def test_dimension():
    """ Checks whether the dimension of the original data is equal to the augmented data. """
    
    shape = data.shape
    augmented_shape = noise_aug("multiplicative_exponential",
                                data,
                                11,
                                2,
                                snr_thres = 10,
                                rate_thres = 1,
                                scale_params = {
                                "low_bound_gauss": 0.01, 
                                "up_bound_gauss": 0.15, 
                                "scale_exp": 4,
                                "scale_rayleigh":4}).shape
    
    
    assert shape == augmented_shape



def test_mult_exp():
    np.random.seed(3)
    data = np.random.randint(10, size = (4,3))
    
    augmented1 = noise_aug("multiplicative_exponential",
              data,
              11,
              2,
              snr_thres = 10,
              rate_thres = 1,
              scale_params = {
              "low_bound_gauss": 0.01, 
              "up_bound_gauss": 0.15, 
              "scale_exp": 4,
              "scale_rayleigh":4}
              )
    
    assert not(data == augmented1).all()


def test_mult_ray():
    np.random.seed(3)
    data = np.random.randint(10, size = (4,3))
    
    augmented1 = noise_aug("multiplicative_rayleigh",
              data,
              11,
              2,
              snr_thres = 10,
              rate_thres = 1,
              scale_params = {
              "low_bound_gauss": 0.01, 
              "up_bound_gauss": 0.15, 
              "scale_exp": 4,
              "scale_rayleigh":4}
              )
    
    assert not(data == augmented1).all()


def test_add_gaus():
    np.random.seed(3)
    data = np.random.randint(10, size = (4,3))
    
    augmented1 = noise_aug("additive_gaussian",
              data,
              11,
              2,
              snr_thres = 10,
              rate_thres = 1,
              scale_params = {
              "low_bound_gauss": 0.01, 
              "up_bound_gauss": 0.15, 
              "scale_exp": 4,
              "scale_rayleigh":4}
              )
    
    assert not(data == augmented1).all()



def test_add_exp():
    np.random.seed(3)
    data = np.random.randint(10, size = (4,3))
    
    augmented1 = noise_aug("additive_exponential",
              data,
              11,
              2,
              snr_thres = 10,
              rate_thres = 1,
              scale_params = {
              "low_bound_gauss": 0.01, 
              "up_bound_gauss": 0.15, 
              "scale_exp": 4,
              "scale_rayleigh":4}
              )
    
    assert not(data == augmented1).all()
