from utils import inputfile_to_array, get_input_file
import re

get_input_file(14)
initialization_program = inputfile_to_array("inputs/input_day_14.txt")
def parse_input(initialization_program):
    mask_index   = -1
    instruction_list    = []
    mask_regex = r"mask = ([\dX]+)"
    mem_regex  = r"mem\[([\d]+)\] = ([\d]+)"
    highest_address_seen = 1
    for line in initialization_program:
        mask_match = re.findall(mask_regex, line)
        mem_match = re.findall(mem_regex, line)
        if mask_match != []:
            instruction_list.append({"mask": mask_match[0], "mem_list": []})
            mask_index += 1
        elif mem_match != []:
            mem_list = instruction_list[mask_index].get("mem_list")
            memory_address,_ = mem_match[0]
            mem_list.append(mem_match[0])
            if int(memory_address) > int(highest_address_seen):
                highest_address_seen = int(memory_address)
            instruction_list[mask_index] = {"mask": instruction_list[mask_index].get("mask"), "mem_list": mem_list}
    return instruction_list, highest_address_seen

def perform_masking(value, mask):
    value_as_binary =  format(int(value), '036b')
    out_value = []
    for i in range(len(mask)):
        value_symbol = value_as_binary[i]
        mask_symbol = mask[i]
        if mask_symbol == "X":
            out_value_symbol = value_symbol
        elif mask_symbol == "1" or mask_symbol == "0":
            out_value_symbol = mask_symbol
        else:
            print("Something is crazy wrong")
            print("Value of value_symbol is: ", mask_symbol)
            exit(1)
        out_value.append(out_value_symbol)
    out_value_binary = "".join(out_value)
    return(int(out_value_binary, 2))

def get_x_indexes(mask):
    index_list = []
    for i in range(len(mask)):
        if mask[i] == "X":
            index_list.append(i)
    return index_list

def replace_x_with_0_and_1(address):
    x_indexes = get_x_indexes(address)
    if x_indexes:
        x_index = x_indexes.pop()
        address_0 = address[:x_index] + "0" + address[x_index + 1:]
        address_1 = address[:x_index] + "1" + address[x_index + 1:]
        if x_indexes:
            output_list = []
        else:
            output_list = [address_1, address_0]
        output_list += replace_x_with_0_and_1(address_0)
        output_list += replace_x_with_0_and_1(address_1)
        return output_list
    else:
        return []


def get_addresses(adress, mask):
    adress_as_binary =  format(int(adress), '036b')
    address_after_masking = []
    for i in range(len(mask)):
        address_symbol = adress_as_binary[i]
        mask_symbol = mask[i]
        if mask_symbol == "X" or mask_symbol == "1":
            output = mask_symbol
        elif mask_symbol == "0":
            output = address_symbol
        else:
            print("Something is crazy wrong")
            print("Value ofaddress_symbol is: ", mask_symbol)
            exit(1)
        address_after_masking.append(output)
    address_as_string = "".join(address_after_masking)
    all_addresses = replace_x_with_0_and_1(address_as_string)
    return(all_addresses)



def task_1(initialization_program):
    instruction_list, highest_address_seen = parse_input(initialization_program)
    memory = [0] * (highest_address_seen+1)
    for instruction in instruction_list:
        mem_list = instruction.get("mem_list")
        mask     = instruction.get("mask")
        for memory_address,value in mem_list:
            value_to_store_in_memory = perform_masking(value, mask)
            try:
                memory[int(memory_address)] = int(value_to_store_in_memory)
            except IndexError:
                print("out of range!")
                print("value of memory address is :", memory_address)
                print("Size of memory is :", highest_address_seen+1)
                exit(1)
    return sum(memory)

def task_2(initialization_program):
    instruction_list, _ = parse_input(initialization_program)
    memory_dict = {}
    i = 0
    for instruction in instruction_list:
        i += 1
        mem_list = instruction.get("mem_list")
        mask     = instruction.get("mask")
        for memory_address,value in mem_list:
            addresses = get_addresses(memory_address, mask)
            try:
                for address in addresses:
                    memory_dict[address] = int(value)
            except IndexError:
                print("out of range!")
                print("value of memory address is :", int(address, 2))
                exit(1)
    return sum(memory_dict.values())
print(task_1(initialization_program))
print(task_2(initialization_program))