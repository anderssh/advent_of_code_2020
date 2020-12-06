import re
from utils import inputfile_to_array, remove_empty_lines_and_concat

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

def passport_element_to_dict(passport_string):
    '''
    Takes in a space separated string which is one passport and
    put them in a dictionary, with key=code and value=valie
    '''
    string_list = passport_string.split(" ")
    mydict = {}
    for element in string_list:
        code_and_value_list = element.split(":")
        if code_and_value_list[0]:
            mydict[code_and_value_list[0]] = code_and_value_list[1]
    return mydict

def get_number_of_passports_with_all_relevant_codes(passport_list, codes):
    '''
    Takes in passport list as returned by "remove_empty_lines_and_concat"
    Returns number of passports with all codes there. Uses
    the "all_relevant_codes_are_present" function.
    '''
    number_of_valid = 0
    for passport_string in passport_list:
        passport_dict = passport_element_to_dict(passport_string)
        if all_relevant_codes_are_present(passport_dict, codes):
            number_of_valid += 1
    return number_of_valid

def get_number_of_valid_passports(passport_list, codes):
    '''
    Takes in passport list as returned by "remove_empty_lines_and_concat"
    Returns number of passports with all relevant codes there and valid
    '''
    number_of_valid = 0
    for passport_string in passport_list:
        passport_dict = passport_element_to_dict(passport_string)
        if all_fields_valid(passport_dict, codes):
            number_of_valid += 1
    return number_of_valid
    
def all_relevant_codes_are_present(passport_dict, codes):
    '''
    Takes in on passport dict.
    Returns True if all relevant codes are in the dictionary, ignores "cid"
    '''
    for code in codes:
        if code not in passport_dict and code != "cid":
            return False
    return True


def all_fields_valid(passport_dict, codes):
    '''
    Takes in on passport dict.
    Returns True if all relevant codes are in the dictionary,
    and all values are valid
    '''
    if not all_relevant_codes_are_present(passport_dict, codes):
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
    if len(passport_id) == 9 and passport_id.isdigit():
        return True
    return False


def task_a(passport_list_with_empty_lines, codes):
    passport_list = remove_empty_lines_and_concat(passport_list_with_empty_lines)
    number_valid_passports = get_number_of_passports_with_all_relevant_codes(passport_list, codes)
    return number_valid_passports

def task_b(passport_list_with_empty_lines, codes):
    passport_list = remove_empty_lines_and_concat(passport_list_with_empty_lines)
    number_valid_passports = get_number_of_valid_passports(passport_list, codes)
    return number_valid_passports

print("The number of valid passports in task a is:", task_a(passport_list_with_empty_lines, codes))
print("The number of valid passports in task b is:", task_b(passport_list_with_empty_lines, codes))