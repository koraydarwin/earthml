import numpy as np
from core.noise_pack import noise_aug

data = np.random.randint(10, size = (4,3))


def test_random():
  """ Checks whether the functions in noise_aug return the same noisy_data """

  np.random.seed(3)
  augmented1 = noise_aug("multiplicative_exponential",
              data,
              11,
              2,
              scale_params_main = {
              "low_bound_gauss": 0.01, 
              "up_bound_gauss": 0.15, 
              "scale": 4}
              )
  
  np.random.seed(3)
  augmented2 = noise_aug("multiplicative_exponential",
              data,
              11,
              2,
              scale_params_main = {
              "low_bound_gauss": 0.01, 
              "up_bound_gauss": 0.15, 
              "scale": 4}
              )
  
  assert (augmented1 == augmented2).all()

def test_dimension():
    """ Checks whether the dimension of the original data is equal to the augmented data. """
    
    raw_data_shape = data.shape
    noisy_data_shape = noise_aug("multiplicative_exponential",
                                data,
                                11,
                                2,
                                scale_params_main = {
                                "low_bound_gauss": 0.01, 
                                "up_bound_gauss": 0.15, 
                                "scale": 4}).shape
    assert raw_data_shape == noisy_data_shape
    
def test_add_gaus():
    np.random.seed(3)
    raw_data = np.random.randint(10, size = (4,3))
    
    noisy_data = noise_aug("additive_gaussian",
              data,
              11,
              2,
              scale_params_main = {
              "low_bound_gauss": 0.01, 
              "up_bound_gauss": 0.15, 
              "scale": 4})
    assert not(raw_data == noisy_data).all()

def test_mult_exp():
    np.random.seed(3)
    raw_data = np.random.randint(10, size = (4,3))
    
    noisy_data = noise_aug("multiplicative_exponential",
              data,
              11,
              2,
              scale_params_main = {
              "low_bound_gauss": 0.01, 
              "up_bound_gauss": 0.15, 
              "scale": 4})
    assert not(raw_data == noisy_data).all()
    
def test_mult_ray():
    np.random.seed(3)
    raw_data = np.random.randint(10, size = (4,3))
    
    noisy_data = noise_aug("multiplicative_rayleigh",
              data,
              11,
              2,
              scale_params_main = {
              "low_bound_gauss": 0.01, 
              "up_bound_gauss": 0.15, 
              "scale": 4})
    assert not(raw_data == noisy_data).all()

def test_add_exp():
    np.random.seed(3)
    raw_data = np.random.randint(10, size = (4,3))
    noisy_data = noise_aug("additive_exponential",
              data,
              11,
              2,
              scale_params_main = {
              "low_bound_gauss": 0.01, 
              "up_bound_gauss": 0.15, 
              "scale": 4})
     assert not(raw_data == noisy_data).all()
