import numpy as np
import numpy.random as rd
import utils
from utils import int_to_binary_concatenate as itb


def tell_mod(mod):
    if(mod == 0): return '+'
    elif(mod == 1): return "~src2"
    elif(mod == 2): return 'src1 & src2'
    elif(mod == 3): return 'src1 | src2'
    elif(mod == 4): return 'src1 >> 1'
    elif(mod == 5): return 'src1 << 1'
    elif(mod == 6): return 'src1 == src2'
    elif(mod == 7): return 'src1 != src2'

def make_result(src1, src2, mod):
    if(mod == 0): return src1 + src2
    elif(mod == 1): return ~src2
    elif(mod == 2): return src1 & src2
    elif(mod == 3): return src1 | src2
    elif(mod == 4): return src1 >> 1
    elif(mod == 5): return src1 << 1
    elif(mod == 6): return src1 == src2
    elif(mod == 7): return 0

def make_branch(src1, src2, mod):
    if(mod < 6): return 0
    elif(mod == 6): return src1 == src2
    elif(mod == 7): return src1 != src2

def make_overflow(src1, src2, mod):
    if(mod == 0): return ( src1 + src2) > 255    
    else: return 0

#############data generate###################

def alu_data_gen():
    data_num = 8
    src1 = np.arange(0, 8, dtype=np.int) 
    src2 = np.arange(8, 16, dtype=np.int) 

    # src1 = rd.randint(0, 256, data_num, dtype=np.uint8)
    # src2 = rd.randint(0, 256, data_num, dtype=np.uint8)

    # src1 = np.ones(data_num, dtype=np.int) * 4
    # src2 = np.ones(data_num, dtype=np.int) * 4
    mod = np.arange(0, 8, dtype=np.int) 

    # print(src1)

    rst_vecfunc = np.vectorize(make_result)
    brc_vecfunc = np.vectorize(make_branch)
    ovf_vecfunc = np.vectorize(make_overflow)    

    rst = rst_vecfunc(src1, src2, mod)
    brc = brc_vecfunc(src1, src2, mod)
    ovf = ovf_vecfunc(src1, src2, mod)

    return [src1, src2, mod, rst, brc, ovf]


data_list = alu_data_gen()
binary_data = [ itb(data_list[0:2], 8),
 itb([data_list[2]], 3),
 itb([data_list[3]], 8),
 itb(data_list[4:], 1)]

# print(binary_data)
# print( itb(binary_data, 1))

for i in range(data_list[0].shape[0]):
    print(f'src1 : {data_list[0][i]}\t src1 : {data_list[1][i]}\t mod : {tell_mod(data_list[2][i])}\n \
    result : {data_list[3][i]}\n')

concated_binary = itb(binary_data, 1)

utils.write_txt_file('test1.tv', concated_binary)