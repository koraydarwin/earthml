import numpy as np
import pytest
from noise_aug.core import noise_aug

data = np.array([[2,3,4], [5,6,7], [8,9,10]])
raw_data_shape = data.shape


def test_dimension_add_gauss():
    """ Checks whether the dimension of the original data is equal to the augmented data. """
    noisy_data_shape = noise_aug("additive_gaussian",
                                data,
                                11,
                                2,
                                {"low_bound_gauss": 0.01, "up_bound_gauss": 0.15, "snr_thres":10, "rate_thres":1}).shape
    assert raw_data_shape == noisy_data_shape

def test_dimension_mult_exp():
    """ Checks whether the dimension of the original data is equal to the augmented data. """
    noisy_data_shape = noise_aug("multiplicative_exponential",
                                data,
                                11,
                                2,
                                {"scale": 4, "snr_thres":10, "rate_thres":1}).shape
    assert raw_data_shape == noisy_data_shape

def test_dimension_mult_ray():
    """ Checks whether the dimension of the original data is equal to the augmented data. """
    noisy_data_shape = noise_aug("multiplicative_rayleigh",
                                data,
                                11,
                                2,
                                {"scale": 4, "snr_thres":10, "rate_thres":1}).shape
    assert raw_data_shape == noisy_data_shape

def test_dimension_add_exp():
    """ Checks whether the dimension of the original data is equal to the augmented data. """
    noisy_data_shape = noise_aug("additive_exponential",
                                data,
                                11,
                                2,
                                {"scale": 4, "snr_thres":10, "rate_thres":1}).shape
    assert raw_data_shape == noisy_data_shape
                        
    
def test_add_gaus():
    noisy_data = noise_aug("additive_gaussian",
              data,
              11,
              2,
              {"low_bound_gauss": 0.01, "up_bound_gauss": 0.15, "snr_thres":10, "rate_thres":1})
    assert not(data == noisy_data).all()
        
def test_mult_exp():
    noisy_data = noise_aug("multiplicative_exponential",
              data,
              11,
              2,
              {"scale": 4, "snr_thres":10, "rate_thres":1})
    assert not(data == noisy_data).all()
    
def test_mult_ray():
    noisy_data = noise_aug("multiplicative_rayleigh",
              data,
              11,
              2,
              {"scale": 4, "snr_thres":10, "rate_thres":1})
    assert not(data == noisy_data).all()

def test_add_exp():
    noisy_data = noise_aug("additive_exponential",
              data,
              11,
              2,
              {"scale": 4, "snr_thres":10, "rate_thres":1})
    assert not(data == noisy_data).all()


def check_noise_type(noise_type):
    noise_lst = ["additive_gaussian", "multiplicative_exponential", "multiplicative_rayleigh", "additive_exponential"]
    if not(noise_type in noise_lst):
            raise ValueError("invalid noise_type")
    else:
        return "it is ok"
            

def test_add_gaus1():
    assert check_noise_type("multiplicative_exponential")
        
def test_mult_exp1():
    assert check_noise_type("multiplicative_exponential")
        
def test_mult_ray1():
    assert check_noise_type("multiplicative_rayleigh")

def test_add_exp1():
    assert check_noise_type("additive_exponential")
