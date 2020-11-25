import utils
import numpy as np

# hyperparameter
width = 128
depth = 32


# make data
all_zero = np.zeros((32, 128), dtype=np.int)
all_zero_binary = utils.int_to_binary_concatenate(all_zero, 1)
all_zero_binary_string = utils.int_to_binary_concatenate(all_zero_binary)

utils.write_bram('all_zeros.coe', all_zero_binary_string)

