from utils import inputfile_to_array, get_input_file
import re

get_input_file(15)
starting_numbers = inputfile_to_array("inputs/input_day_15.txt")[0].split(",")
starting_numbers = [int(n) for n in starting_numbers]


def put_list_in_dict_as_keys_and_turn_as_value(the_list):
    the_dict = {}
    for i in range(len(the_list)):
        the_dict[the_list[i]] = i +1
    return the_dict

def play_game(starting_numbers, number_of_rounds = 2020):
    turn_list = []
    turn_number = len(starting_numbers)
    num_dict = put_list_in_dict_as_keys_and_turn_as_value(starting_numbers[:-1])
    next_value  = starting_numbers[-1]
    while turn_number < number_of_rounds:
        last_spoken = next_value
        if last_spoken in num_dict.keys():
            difference = turn_number - num_dict[last_spoken]
            next_value = difference
            turn_list.append(difference)
            num_dict[last_spoken] = turn_number
        else:
            num_dict[last_spoken] = turn_number
            next_value = 0
        turn_number += 1
    return(next_value)
print(play_game(starting_numbers, number_of_rounds = 2020))
print(play_game(starting_numbers, number_of_rounds = 30000000))