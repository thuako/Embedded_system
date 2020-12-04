import utils
import numpy as np

# hyperparameter
width = 128
depth = 32


# make data

def all_zero_gen():
    all_zero = np.zeros((32, 128), dtype=np.int)
    all_zero_binary = utils.int_to_binary_concatenate(all_zero, 1)
    all_zero_binary_string = utils.int_to_binary_concatenate(all_zero_binary)

    utils.write_bram('all_zeros.coe', all_zero_binary_string)

def systolic_1_1_8bit_gen():
    act = np.concatenate( (np.arange(0, 32, dtype=np.int), np.arange(0, 32, dtype=np.int)), axis=0 ).reshape(-1, 1)
    weight = np.ones((64, 1), dtype=np.int)
    pre_sum = np.zeros((64, 1), dtype=np.int)

    for i in range(weight.shape[0]):
        weight[i] = np.round(i / 4)
        if i > 31:
            weight[i] = -weight[i]

    act_binary = utils.int_to_binary_concatenate([act], 32)
    weight_binary = utils.int_to_binary_concatenate([weight], 8)
    pre_sum_binary = utils.int_to_binary_concatenate([pre_sum], 16)

    act_binary_string = utils.int_to_binary_concatenate([act_binary])
    weight_binary_string = utils.int_to_binary_concatenate([weight_binary])
    pre_sum_binary_string = utils.int_to_binary_concatenate([pre_sum_binary])

    utils.write_bram('act_8.coe', act_binary_string)
    utils.write_bram('weight_8.coe', weight_binary_string)
    utils.write_bram('pre_sum_8.coe', pre_sum_binary_string)

def systolic_1_1_2bit_gen():
    # depth is 8
    act0 = np.arange(0, 4, dtype=np.int)
    act1 = np.arange(3, -1, step= -1, dtype=np.int)
    act2 = np.arange(0, 4, dtype=np.int)    
    act3 = np.arange(3, -1, step= -1, dtype=np.int)

    for i in range(1):
        act0 = np.append(act0, np.arange(0, 4, dtype=np.int))
        act1 = np.append(act1, np.arange(3, -1, step= -1, dtype=np.int))
        act2 = np.append(act2, np.arange(0, 4, dtype=np.int))
        act3 = np.append(act3, np.arange(3, -1, step= -1, dtype=np.int))

    
    weight = np.ones((8, 1), dtype=np.int)
    pre_sum = np.zeros((8, 1), dtype=np.int)

    for i in range(weight.shape[0]):
        weight[i] = np.int(i % 4)
        if i > 3:
            weight[i] = -weight[i]

    act_binary = utils.int_to_binary_concatenate([act0, act1, act2, act3, act0, act1, act2, act3, act0, act1, act2, act3, act0, act1, act2, act3], 2)
    weight_binary = utils.int_to_binary_concatenate([weight, weight, weight, weight], 2)
    pre_sum_binary = utils.int_to_binary_concatenate([pre_sum], 16)

    act_binary_string = utils.int_to_binary_concatenate([act_binary])
    weight_binary_string = utils.int_to_binary_concatenate([weight_binary])
    pre_sum_binary_string = utils.int_to_binary_concatenate([pre_sum_binary])

    utils.write_bram('act.coe', act_binary_string)
    utils.write_bram('weight.coe', weight_binary_string)
    utils.write_bram('pre_sum.coe', pre_sum_binary_string)


def systolic_1_1_v4_gen():
    # depth is 8
    act = np.arange(0, 8, dtype=np.int)
    weight = np.arange(0, 8, dtype=np.int)
    pre_sum = np.zeros((8, 1), dtype=np.int)

    act_list = []
    weight_list = []
    for i in range(4):
        act_list.append(act)
        # weight_list.append(weight)

    act_binary = utils.int_to_binary_concatenate(act_list, 8)
    weight_binary = utils.int_to_binary_concatenate([weight], 8)
    pre_sum_binary = utils.int_to_binary_concatenate([pre_sum], 16)

    act_binary_string = utils.int_to_binary_concatenate([act_binary])
    weight_binary_string = utils.int_to_binary_concatenate([weight_binary])
    pre_sum_binary_string = utils.int_to_binary_concatenate([pre_sum_binary])

    utils.write_bram('act_v4.coe', act_binary_string)
    utils.write_bram('weight_v4.coe', weight_binary_string)
    utils.write_bram('pre_sum_v4.coe', pre_sum_binary_string)



# systolic_1_1_2bit_gen()

# systolic_1_1_8bit_gen()

# systolic_1_1_v4_gen()

def systolic_1_1_v4_gen_show_result(act = None, weight = None, size= None):
    # depth is 8
    if act is None:
        act = np.arange(0, 8, dtype=np.int)

    if weight is None:
        weight = np.arange(0, 8, dtype=np.int)
    pre_sum = np.zeros((8, 1), dtype=np.int)

    if size is None:
        size = 1

    act_matrix = np.repeat(act.reshape(-1, 1), size, axis=1)
    weight_matrix = np.repeat(weight.reshape(-1, 1), size, axis=1)

    result = np.matmul(act_matrix , weight_matrix.T)
    print(f'activation : \n{act_matrix}\nweight : \n{weight_matrix}\nresult : \n{result}\nresult sahpe : {result.shape} ')



    act_list = []
    for i in range(4):
        act_list.append(act)

    act_binary = utils.int_to_binary_concatenate(act_list, 8)
    weight_binary = utils.int_to_binary_concatenate([weight], 8)
    pre_sum_binary = utils.int_to_binary_concatenate([pre_sum], 16)

    act_binary_string = utils.int_to_binary_concatenate([act_binary])
    weight_binary_string = utils.int_to_binary_concatenate([weight_binary])
    pre_sum_binary_string = utils.int_to_binary_concatenate([pre_sum_binary])

    utils.write_bram('./gen_data/act_v4.coe', act_binary_string)
    utils.write_bram('./gen_data/weight_v4.coe', weight_binary_string)
    utils.write_bram('./gen_data/pre_sum_v4.coe', pre_sum_binary_string)



weight = np.arange(7, -1, -1)
act = np.arange(1, 9)

systolic_1_1_v4_gen_show_result(act, weight, 8)









