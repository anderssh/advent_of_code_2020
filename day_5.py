import re
from utils import inputfile_to_array
from math import floor, ceil
from statistics import mean 

seating_codes = inputfile_to_array("inputs/input_day_5.txt")


def get_seat_row(row_code):
    upper_limit = 127
    lower_limit = 0
    for character in row_code:
        if character == "F":
            upper_limit = floor(mean([lower_limit, upper_limit]))
        elif character == "B":
            lower_limit = ceil(mean([lower_limit, upper_limit]))
        else:
            print(" This should never happend, the row character is neither 'B' nor 'F")
    return upper_limit # Same as lower limit when function is returning

def get_seat_column(column_code):
    upper_limit = 7
    lower_limit = 0
    for character in column_code:
        if character == "L":
            upper_limit = floor(mean([lower_limit, upper_limit]))
        elif character == "R":
            lower_limit = ceil(mean([lower_limit, upper_limit]))
        else:
            print(" This should never happend, column code character is neither 'R' nor 'L")
    return upper_limit # Same as lower limit when function is returning

def get_seat_id(row, column):
    return int(row) * 8 + column

def get_row_and_column_code(seating_code):
    return (seating_code[0:7],seating_code[7:10])


def get_highest_seat_id(seating_codes):
    current_highest_seat_id = 0
    for seating_code in seating_codes:
        row_code,column_code = get_row_and_column_code(seating_code)
        seat_id = get_seat_id(get_seat_row(row_code), get_seat_column(column_code))
        if seat_id > current_highest_seat_id:
            current_highest_seat_id = seat_id
    return current_highest_seat_id

def get_sorted_seat_ids(seating_codes):
    seat_id_list = []
    for seating_code in seating_codes:
        row_code,column_code = get_row_and_column_code(seating_code)
        seat_id = get_seat_id(get_seat_row(row_code), get_seat_column(column_code))
        seat_id_list.append(seat_id)
        seat_id_list.sort()
    return seat_id_list

def get_missing_seat_id(seating_codes):
    sorted_id_list = get_sorted_seat_ids(seating_codes)
    for i in range(sorted_id_list[0], sorted_id_list[-1]):
        if i not in sorted_id_list:
            if ((i-1) in sorted_id_list) and ((i+1) in sorted_id_list):
                return i
        

def get_code_from_seat_id(seat_id, seating_codes):
    for seating_code in seating_codes:
        row_code,column_code = get_row_and_column_code(seating_code)
        the_seat_id = get_seat_id(get_seat_row(row_code), get_seat_column(column_code))
        if the_seat_id == seat_id:
            return seating_code


print("The hightest seat_id is:", get_highest_seat_id(seating_codes))
print("The missing seat code is:", get_missing_seat_id(seating_codes))