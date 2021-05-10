import numpy as np
from package.core import noise_aug




def test_random(augmented1, augmented2):
  """ Checks whether the functions in noise_aug return the same noisy_data """
  
  np.random.seed(3)
  augmented1 = noise_aug(noise_type,
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
              )
  
  np.random.seed(3)
  augmented2 = noise_aug(noise_type,
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
              )
  
  assert augmented1 == augmented2




