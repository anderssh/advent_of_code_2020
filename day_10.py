from utils import inputfile_to_array
import functools

joltage_list = sorted([int(item) for item in inputfile_to_array("inputs/input_day_10.txt")])

memo_dict = {}
def get_permutations(joltage_list, the_element_before):
    worklist = joltage_list[:]
    if worklist:
        usable_adapters_this_round = get_elements_with_small_enough_difference(worklist, the_element_before)
        permutations = 0
        for adapter in usable_adapters_this_round:
            list_to_pass_to_function = worklist[:]
            if adapter in memo_dict:
                permutations += memo_dict[adapter]
            else:
                list_to_pass_to_function = [x for x in worklist if x > adapter]
                permutations_from_this_run = int(get_permutations(list_to_pass_to_function, adapter))
                memo_dict[adapter] = permutations_from_this_run
                permutations = permutations + permutations_from_this_run
        return permutations
    return 1

def get_elements_with_small_enough_difference(joltage_list, element_to_compare_to):
    output_list = []
    for element in joltage_list:
        if abs(element-element_to_compare_to) <= 3:
            output_list.append(element)
    return output_list

def get_joltage_differences(joltage_list):
    worklist = joltage_list[:]
    worklist.append(0)
    worklist.append(max(worklist)+3)
    diff_list = []
    for i in range(len(worklist)-1):
            min_joltage_in_list = min(worklist)
            worklist.remove(min_joltage_in_list)
            diff_list.append(abs(min_joltage_in_list - min(worklist)))
    return diff_list

def hashing_function(the_list, value):
    the_list_as_strings = [str(i) for i in the_list]
    value_str = str(value)
    return value_str.join(the_list_as_strings)

def task_1(joltage_list):
    diff_list = (get_joltage_differences(joltage_list))
    number_of_ones = diff_list.count(1)
    number_of_threes = diff_list.count(3)
    return number_of_threes*number_of_ones

print(task_1(joltage_list))
print(get_permutations(joltage_list, 0))
