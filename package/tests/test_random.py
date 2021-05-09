import numpy as np
from package.core import noise_aug

np.random.seed(3)


def test_random():
  augmented1 = noise_aug(noise_type,
              data,
              snr,
              rate,
              snr_thres = 10,
              rate_thres = 1,
              scale_params = {
              "low_bound_gauss": 0.01, 
              "up_bound_gauss": 0.15, 
              "scale_expo": 4}
              )
  
  augmented2 = noise_aug(noise_type,
              data,
              snr,
              rate,
              snr_thres = 10,
              rate_thres = 1,
              scale_params = {
              "low_bound_gauss": 0.01, 
              "up_bound_gauss": 0.15, 
              "scale_expo": 4}
              )
  
  assert augmented1 == augmented2




