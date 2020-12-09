from utils import inputfile_to_array
import numpy

    
preamble_length = 25
number_list = [int(item) for item in inputfile_to_array("inputs/input_day_9.txt")]

def check_if_sum_exists_in_number_list(number_list, number):
    for val in number_list:
        for inner_val in number_list:
            if val + inner_val == number:
                return True
    return False

def get_invalid_number(number_list, preamble_length):
    for i in range(len(number_list)):
        list_to_check_in = number_list[i:(preamble_length+i)]
        number_to_check  = number_list[preamble_length + i]
        if not check_if_sum_exists_in_number_list(list_to_check_in,number_to_check):
            return number_to_check

def find_contiguous_numbers(number_list,invalid_number):
    for i in range(len(number_list)):
        for j in range(i+1, len(number_list)):
            contigous_numbers = number_list[i:j+1]
            sum_of_contigous_numbers = numpy.sum(contigous_numbers)
            if sum_of_contigous_numbers > invalid_number:
                break
            if sum_of_contigous_numbers == invalid_number:
                return min(contigous_numbers) + max(contigous_numbers)

     

def task_1(number_list, preamble_length):
    return get_invalid_number(number_list, preamble_length)


def task_2(number_list, preamble_length):
    invalid_number = get_invalid_number(number_list, preamble_length)
    return find_contiguous_numbers(number_list,invalid_number)
print(task_1(number_list, preamble_length))
print(task_2(number_list, preamble_length))
