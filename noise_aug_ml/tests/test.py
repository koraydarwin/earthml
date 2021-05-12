import numpy as np
import pytest
from noise_aug.core import noise_aug

data = np.random.randint(10, size = (4,3))

def doo():
    raise ValueError('Dimension Error')

def test_dimension():
    """ Checks whether the dimension of the original data is equal to the augmented data. """
    
    raw_data_shape = data.shape
    data1 = np.random.randint(10, size = (5,6))
    noisy_data_shape = noise_aug("multiplicative_exponential",
                                data,
                                5,
                                2,
                                {"low_bound_gauss": 0.01, "up_bound_gauss": 0.15, "scale": 4, "snr_thres":10, "rate_thres":1}).shape
    if raw_data_shape == noisy_data_shape:
        assert raw_data_shape == noisy_data_shape
        
    else:
        doo()
        
def foo():
    raise ValueError("Data did not augmented")
    
def test_add_gaus():
    np.random.seed(3)
    raw_data = np.random.randint(10, size = (4,3))
    noisy_data = noise_aug("additive_gaussian",
              raw_data,
              11,
              2,
              {"low_bound_gauss": 0.01, "up_bound_gauss": 0.15, "scale": 4, "snr_thres":10, "rate_thres":1})

    if not(raw_data == noisy_data).all():
        assert not(raw_data == noisy_data).all()
        
    else:
        foo()

def test_mult_exp():
    np.random.seed(3)
    raw_data = np.random.randint(10, size = (4,3))
    noisy_data = noise_aug("multiplicative_exponential",
              raw_data,
              11,
              2,
              {"low_bound_gauss": 0.01, "up_bound_gauss": 0.15, "scale": 4, "snr_thres":10, "rate_thres":1})
    if not(raw_data == noisy_data).all():
        assert not(raw_data == noisy_data).all()
    else:
        foo()
    
def test_mult_ray():
    np.random.seed(3)
    raw_data = np.random.randint(10, size = (4,3))
    
    noisy_data = noise_aug("multiplicative_rayleigh",
              raw_data,
              11,
              2,
              {"low_bound_gauss": 0.01, "up_bound_gauss": 0.15, "scale": 4, "snr_thres":10, "rate_thres":1})
    
    if not(raw_data == noisy_data).all():
        assert not(raw_data == noisy_data).all()
    else:
        foo()

def test_add_exp():
    np.random.seed(3)
    raw_data = np.random.randint(10, size = (4,3))
    noisy_data = noise_aug("additive_exponential",
              raw_data,
              11,
              2,
              {"low_bound_gauss": 0.01, "up_bound_gauss": 0.15, "scale": 4, "snr_thres":10, "rate_thres":1})
    if not(raw_data == noisy_data).all():
        assert not(raw_data == noisy_data).all()
    else:
        foo()
