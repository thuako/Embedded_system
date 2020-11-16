import numpy as np
import numpy.random as rd

def vec_bin_array(arr, m):
    """
    Arguments: 
    arr: Numpy array of positive integers
    m: Number of bits of each integer to retain

    Returns a copy of arr with every element replaced with a bit vector.
    Bits encoded as int8's.
    """
    to_str_func = np.vectorize(lambda x: np.binary_repr(x).zfill(m))
    strs = to_str_func(arr)
    ret = np.zeros(list(arr.shape) + [m], dtype=np.int8)
    for bit_ix in range(0, m):
        fetch_bit_func = np.vectorize(lambda x: x[bit_ix] == '1')
        ret[...,bit_ix] = fetch_bit_func(strs).astype("int8")

    return ret 

def write_txt_file(num, file_name, *args):

    

    # args to list
    arg_list = []
    for arg in args:
        arg_list.append(arg)

    arg_nums = len(arg_list)


    # binary to string

    args_string_binary = []

    for i in range(arg_nums):
        args_string_binary.append([''.join(binary) for binary in arg_list[i].astype(str) ])


    # file write

    text_file = open( file_name , mode='wt', encoding='utf-8')

    check_num = 0 # to print testvector bit width
    for data_row in range(num):
        one_line = ''
        for num_arg in range(arg_nums):
            one_line += args_string_binary[num_arg][data_row]
        text_file.write(one_line + '\n')
        if(check_num == 0):
            print(f'the number of the testvector width is {len(one_line)}')
            check_num = 1
    text_file.close()


def random_datagen(num):

    weight1 = rd.randint(-2**30, 2**30, num,dtype=np.int64)
    weight2 = rd.randint(-2**30, 2**30, num,dtype=np.int64)

    act1 = rd.randint(-2^30, 2^30, num,dtype=np.int64)   
    act2 = rd.randint(-2^30, 2^30, num,dtype=np.int64)

    mod = rd.randint(0,3, num, dtype=np.int64)

    result1 = rd.randint(-2^30, 2^30, num,dtype=np.int64)
    result2 = rd.randint(-2^30, 2^30, num,dtype=np.int64)

    print(weight1[0], weight2[0])

    return weight1, weight2, act1, act2, mod, result1, result2


weight1, weight2, act1, act2, mod, result1, result2 = random_datagen(4)    



write_txt_file(4, 'test.tv', vec_bin_array(weight1, 64), vec_bin_array(weight2, 64), vec_bin_array(act1, 64), vec_bin_array(act2, 64), vec_bin_array(mod, 3), vec_bin_array(result1, 64), vec_bin_array(result2, 64)    )










