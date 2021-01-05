import utils
import numpy as np




def dynamic_2bit(act = None, weight = None, column=None):
    pre_sum = np.zeros((8, 1), dtype=np.int)
    
    result=None
    for i in range(len(act)):
        act_matrix = np.repeat(act[i].reshape(-1, 1), column, axis=1)
        weight_matrix = np.repeat(weight[i].reshape(-1, 1), column, axis=1)
        if result is None:
            result = np.matmul(act_matrix , weight_matrix.T)
        else:
            result = result + np.matmul(act_matrix , weight_matrix.T)
    print(f'activation : \n{act}\nweight : \n{weight}\nresult : \n{result}\nresult sahpe : {result.shape} ')
    

    act_binary = utils.int_to_binary_concatenate(act, 8)
    weight_binary = utils.int_to_binary_concatenate(weight, 2)
    pre_sum_binary = utils.int_to_binary_concatenate([pre_sum], 16)

    act_binary_string = utils.int_to_binary_concatenate([act_binary])
    weight_binary_string = utils.int_to_binary_concatenate([weight_binary])
    pre_sum_binary_string = utils.int_to_binary_concatenate([pre_sum_binary])

    utils.write_bram('./gen_data/act_v4.coe', act_binary_string)
    utils.write_bram('./gen_data/weight_v4.coe', weight_binary_string)
    utils.write_bram('./gen_data/pre_sum_v4.coe', pre_sum_binary_string)

row = 4
column = 1

act = []
weight = []
for i in range(4):
    act.append(np.random.randint(0, 4, row))
    weight.append(np.random.randint(-2, 2, row))

dynamic_2bit(act, weight, column)





