import numpy as np
import pytest
from noise_aug import noise_aug

RAW_DATA = np.array([[ 2,  3,  4,  5],
                     [ 6,  7,  8,  9],
                     [10, 11, 12, 13]])

ADDITIVE_SCALE_PARAMS = {
    "low_bound_scale" : 0.01,
    "up_bound_scale"  : 0.15,
    "snr_thres"       : 10}

MULTIPLICATIVE_SCALE_PARAMS = {
    "scale"     : 4, 
    "snr_thres" : 10}

ADDITIVE_ARGS = {
    'snr'         : 11,
    'rate'        : 1,
    'scale_params': ADDITIVE_SCALE_PARAMS}
    
MULTIPLICATIVE_ARGS = {
    'snr'         : 11,
    'rate'        : 1,
    'scale_params': MULTIPLICATIVE_SCALE_PARAMS}

NOISE_TYPE2ARGS = {
    "additive_gaussian"         : ADDITIVE_ARGS,
    "additive_exponential"      : ADDITIVE_ARGS,
    "multiplicative_exponential": MULTIPLICATIVE_ARGS,
    "multiplicative_rayleigh"   : MULTIPLICATIVE_ARGS}

def test_dimensions():
    '''check dimensions of noisy data'''
    for noise_type, kwargs in NOISE_TYPE2ARGS.items():
        noisy_data = noise_aug(RAW_DATA, noise_type, **kwargs)
        assert RAW_DATA.shape == noisy_data.shape

def test_data_changed():
    '''make sure all data is modified when rate==1'''
    # XXX TODO this is a risky test! randomness means we will
    # sometimes (rarely) have unmodified data despite the code working
    # properly
    for noise_type, kwargs in NOISE_TYPE2ARGS.items():
        noisy_data = noise_aug(RAW_DATA, noise_type, **kwargs)
        assert (RAW_DATA != noisy_data).all()

def test_invalid_noise_type():
    '''make sure we get an error when we use an undefined error type'''
    kwargs = NOISE_TYPE2ARGS['additive_exponential']
    with pytest.raises(AssertionError):
        noisy_data = noise_aug(RAW_DATA, 'junk_noise', **kwargs)

MULTIPLICATIVE_NOISE_TYPE2ARGS = {k: v for k, v in NOISE_TYPE2ARGS.items() if
                            k != 'additive_gaussian' or k != 'additive_exponential'}
def test_invalid_scale_args():
    '''make sure we get an error when we use additive noise arguments with multiplicative
    noise type'''
    gauss_kwargs = NOISE_TYPE2ARGS['additive_gaussian']
    for noise_type in MULTIPLICATIVE_NOISE_TYPE2ARGS:
        with pytest.raises(ValueError):
            noisy_data = noise_aug(RAW_DATA, noise_type, **gauss_kwargs)
