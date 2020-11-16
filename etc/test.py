import utils
import numpy as np
import numpy.random as rd
from utils import vec_bin_array



def random_datagen(num):

    weight1 = rd.randint(-2**30, 2**30, num )
    weight2 = rd.randint(-2**30, 2**30, num )

    act1 = rd.randint(-2^30, 2^30, num )   
    act2 = rd.randint(-2^30, 2^30, num )

    mod = rd.randint(0,3, num, dtype=np.int32)

    result1 = rd.randint(-2^30, 2^30, num )
    result2 = rd.randint(-2^30, 2^30, num )

    print(weight1[0], weight2[0])

    return weight1, weight2, act1, act2, mod, result1, result2


weight1, weight2, act1, act2, mod, result1, result2 = random_datagen(4)    



# utils.write_txt_file(4, 'test.tv', vec_bin_array(weight1, 64), vec_bin_array(weight2, 64), vec_bin_array(act1, 64), vec_bin_array(act2, 64), vec_bin_array(mod, 3), vec_bin_array(result1, 64), vec_bin_array(result2, 64)    )


utils.write_txt_file(1, 'test3.tv',vec_bin_array(np.array([-5], dtype=np.int8), 8),vec_bin_array(np.array([0]), 4) )
