from utils import inputfile_to_array

number_list = inputfile_to_array("input_day_1.txt")

def task_1(number_list):
    for first_number in number_list:
        for second_number in number_list:
            sum_of_numbers = first_number + second_number
            if sum_of_numbers == 2020:
                print(first_number)
                print(second_number)
                return first_number*second_number
def task_2(number_list):
    for first_number in number_list:
        for second_number in number_list:
            for third_number in number_list:
                sum_of_numbers = first_number + second_number + third_number
                if sum_of_numbers == 2020:
                    print(first_number)
                    print(second_number)
                    print(third_number)
                    return first_number*second_number*third_number
print(task_1(number_list))
print(task_2(number_list))
