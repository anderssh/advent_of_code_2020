import re
from utils import inputfile_to_array, remove_empty_lines_and_concat
from math import floor, ceil
from statistics import mean 

customs_form = inputfile_to_array("inputs/input_day_6.txt")

def count_unique_letters(the_string):
    the_set = set()
    for letter in the_string:
        the_set.add(letter)
    return len(the_set)        

def count_letters_in_all_people_of_group(one_groups_declarations):
    '''
    Returns the number of common letters i decleration across all persons in a groups
    '''
    the_set = set()
    one_groups_declarations_list = one_groups_declarations.split(" ")
    first_declaration = one_groups_declarations_list[0]
    for letter in first_declaration:
        the_set.add(letter)
    for decleration in one_groups_declarations_list:
        letters_to_be_removed = []
        for letter in the_set:
            if letter not in decleration:
                letters_to_be_removed.append(letter)
        for letter in letters_to_be_removed:
            the_set.remove(letter)
    return len(the_set)

def sum_of_anyone(group_list):
    '''
    Gives the sum of the unique letters per group, for all groups
    '''
    sum = 0
    for the_string in group_list:
        sum += count_unique_letters(the_string)
    return sum

def sum_of_everyone(all_declarations):
    '''
    Gives the sum of the common letters in all persons in group, for all groups
    '''
    sum = 0
    for one_groups_declarations in all_declarations:
        sum += count_letters_in_all_people_of_group(one_groups_declarations)
    return sum



def task_a(customs_form):
    list_without_blank_lines = remove_empty_lines_and_concat(customs_form, space_separated=False)
    return sum_of_anyone(list_without_blank_lines)

def task_b(customs_form):
    list_without_blank_lines = remove_empty_lines_and_concat(customs_form)
    return sum_of_everyone(list_without_blank_lines)

print("Sum of counts i part a is", task_a(customs_form))
print("Sum of counts i part b is", task_b(customs_form))
