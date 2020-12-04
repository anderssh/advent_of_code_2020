import re
from utils import inputfile_to_array

passport_list_with_empty_lines = inputfile_to_array("inputs/input_day_4.txt")

codes = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid'
]

def remove_empty_lines_and_concat(passport_list_with_empty_lines):

    element = ''
    passport_list = []
    for i, item in enumerate(passport_list_with_empty_lines):
        if item == "":
            passport_list.append(element)
            element = ''
        else:
            element = element + item
            if i == len(passport_list_with_empty_lines)-1:
                passport_list.append(element)
    return passport_list

def passport_element_to_dict(passport_string, codes):
    string_list = passport_string.split(" ")
    mydict = {}
    for element in string_list:
        code_and_value_list = element.split(":")
        if code_and_value_list[0] != "cid":
            mydict[code_and_value_list[0]] = code_and_value_list[1]
    print(mydict)

def get_number_of_valid_passports(passport_list, codes):
    number_of_valid = 0
    for i in passport_list:
        this_passport_is_valid = True
        for k in codes:
            if k not in i and k != "cid":
                this_passport_is_valid = False
        if this_passport_is_valid:
            number_of_valid += 1
    return number_of_valid
def get_number_of_valid_passports(passport_list, codes):
    return
def all_relevant_codes_are_present(codes):
    for code in codes:
        if code not in passport_dict:
    return False


def validate_fields(passport_dict, codes):
    if not all_relevant_codes_are_present():
        return False
    if not validate_birth_year(passport_dict.get("byr")): return False
    if not validate_issue_year(passport_dict.get("iyr")): return False
    if not validate_expiration_year(passport_dict.get("eyr")): return False
    if not validate_height(passport_dict.get("hgt")): return False
    if not validate_eye_color(passport_dict.get("ecl")): return False
    if not validate_hair_color(passport_dict.get("hcl")): return False
    if not validate_passport_id(passport_dict.get("pid")): return False
    return True

def validate_birth_year(birth_year):

    if (1920 <= int(birth_year) <= 2002) and (len(str(birth_year)) == 4):
        return True 
    return False

def validate_issue_year(issue_year):

    if (2010 <= int(issue_year) <= 2020) and (len(str(issue_year)) == 4):
        return True 
    return False

def validate_expiration_year(expiration_year):

    if (2020 <= int(expiration_year) <= 2030) and (len(str(expiration_year)) == 4):
        return True 
    return False

def validate_height(height):

    unit = str(height[-2]) + str(height[-1])
    if unit == "in" and len(height) == 4:
        number = int(height[0:2])
        if 59 <= number <= 76:
            return True
    elif unit == "cm" and len(height) == 5:
        number = int(height[0:3])
        if 150 <= number <= 193:
            return True
    return False


def validate_eye_color(eye_color):

    valid_colors= [
    "amb",
    "blu",
    "brn",
    "gry",
    "grn",
    "hzl",
    "oth",
    ]
    if eye_color in valid_colors:
        return True
    return False

def validate_hair_color(hair_color):
    if len(hair_color) == 7 and hair_color[0] == "#":
        hair_color = hair_color[1:]
        try:
            int(hair_color, 16)
            return True
        except ValueError:
            return False
    return False

def validate_passport_id(passport_id):
    if len(passport_id) == 6 and passport_id.isdigit():
        return True
    return False


def task_a(passport_list_with_empty_lines, codes):
    passport_list = remove_empty_lines_and_concat(passport_list_with_empty_lines)
    number_valid_passports = get_number_of_valid_passports(passport_list, codes)
    return number_valid_passports

def task_b(passport_list_with_empty_lines, codes):
    passport_list = remove_empty_lines_and_concat(passport_list_with_empty_lines)
    passport_element_to_dict()
    return

#print("The number of valid passports in task a is:", task_a(passport_list_with_empty_lines, codes) )
task_b(passport_list_with_empty_lines, codes)