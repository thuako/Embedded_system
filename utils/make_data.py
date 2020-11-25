import numpy as np

def int_to_binary_concatenate( arr, m=1):
    '''
    Arguments
    arr : nd.array must be in the list
    m : bit width

    convert nd.array to binary string
    both two dimension and one dimension are compatable for this function.
    and string which in list is also compatable.
    ex) 

    a = np.array([1,2,2,1,3,1]).reshape(-1, 2) to 
    [['00010010'], ['00100001', ], ['00110001', ]]

    or 

    b = np.array([4,5,6]).reshape(-1, 1) to
    [['0100'], ['0101'], ['0110']]

    '''
    # args is consist of nd.array
    if isinstance(arr[0],np.ndarray):
        # numpy array convert to string by using vectorize func
        to_str_func = np.vectorize(lambda x: ((np.binary_repr(x, m)[::-1])[:m])[::-1])
        for i in range(len(arr)):
            arr[i] = to_str_func(arr[i]) 

        # print(arr[0][0], f'arr type : {type(arr[0][0])}')

        # u4 to string
        result_list = []
        for tv_row in range(len(arr[0])):
                result_list.append([''.join(binary[tv_row].astype(str)) for binary in arr])

    # args is consist of list which allocate strings                
    else:
        result_list = []
        for data_row in range(len(arr[0])):
            one_line = ''
            for num_arg in range(len(arr)):
                one_line += ''.join(arr[num_arg][data_row])
            result_list.append(one_line)
    return result_list

def write_testvector(file_name, *args):
    # file write
    text_file = open( file_name , mode='wt', encoding='utf-8')
    write_binary(text_file, *args)
    text_file.close()


def write_bram(file_name, *args):
    file = open( file_name , mode='wt', encoding='utf-8')
    msg = 'memory_initialization_radix=2;\nmemory_initialization_vector=\n'
    file.write(msg)
    write_binary(file, *args)
    file.close()


def write_binary(file_stream, *args):
    check_num = 0 # to print testvector bit width
    for data_row in range(len(args[0])):
        one_line = ''
        for num_arg in range(len(args)):
            one_line += args[num_arg][data_row]
        file_stream.write(one_line + '\n')

        if(check_num == 0):
            print(f'the number of the data width is {len(one_line)}')
            check_num = 1