from utils import inputfile_to_array

passwords_and_policy_list = inputfile_to_array("inputs/input_day_2.txt")

def extract_policy_and_password_from_string(passwords_and_policy_string):
    '''
    Takes in a string of the format "<n>-<N> <a>: <x>[x..]" where
    n: is the first number in the password policy
    N: is the second number in password policy
    a: is the letter
    x: is the password (can contain different characters)

    returns a tupple in the format:
    (n,N,a,x)

    '''
    string_list = passwords_and_policy_string.split(" ")
    letter_in_policy = string_list[1][:-1]
    policy_string = string_list[0].split("-")
    first_number = int(policy_string[0])
    second_number = int(policy_string[1])
    password = string_list[-1]

    return (first_number,second_number,letter_in_policy,password)

def count_letter_in_string(my_letter,my_string):
    '''
    Returns the number of occurences "my_letter" in "my_string"
    '''
    counter = 0
    for i in my_string:
        if i == my_letter:
            counter = counter +1
    return counter

def task_1(passwords_and_policy_list):
    valid_passwords = 0
    for passwords_and_policy_string in passwords_and_policy_list:
        (minimum,maximum,letter,password) = extract_policy_and_password_from_string(passwords_and_policy_string)
        if minimum <= count_letter_in_string(letter, password) and count_letter_in_string(letter, password) <= maximum:
            valid_passwords = valid_passwords + 1
    return valid_passwords

def task_2(passwords_and_policy_list):
    valid_passwords = 0
    for passwords_and_policy_string in passwords_and_policy_list:
        (first_pos,second_pos,letter,password) = extract_policy_and_password_from_string(passwords_and_policy_string)
        if (password[first_pos-1] == letter) ^ (password[second_pos-1] == letter):
            valid_passwords = valid_passwords +1
    return valid_passwords

print(task_1(passwords_and_policy_list))
print(task_2(passwords_and_policy_list))