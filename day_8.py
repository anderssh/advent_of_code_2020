from utils import inputfile_to_array

boot_code = inputfile_to_array("inputs/input_day_8.txt")

def perform_instruction(instruction, accumulator, i, sign, number):
    if instruction == "acc":
        i += 1
        if sign == "-":
            accumulator -= number
        elif sign == "+":
            accumulator += number
    elif instruction == "jmp":
        if sign == "-":
            i -= number
        elif sign == "+":
            i += number
        else:
            print("Sign is neither '-' nor '+' ")
    elif instruction == "nop":
        i += 1
    return (i, accumulator)

def get_all_nop_instruction_indexes(boot_code):
    indexes = []
    i = 0
    for line in boot_code:
        if "nop" in line:
            indexes.append(i)
        i +=1
    return indexes

def get_all_jmp_instruction_indexes(boot_code):
    indexes = []
    i = 0
    for line in boot_code:
        if "jmp" in line:
            indexes.append(i)
        i +=1
    return indexes

def run_boot_code(boot_code):
    already_visited_instructions = []
    accumulator                  = 0
    i                            = 0
    last_index                   = len(boot_code)-1
    is_last_index_reached        = False
    while (i not in already_visited_instructions) and (not is_last_index_reached):
        instruction        = boot_code[i].split(" ")[0]
        signed_number      = boot_code[i].split(" ")[1]
        sign               = signed_number[0]
        number             = int(signed_number[1:])
        already_visited_instructions.append(i)
        (i, accumulator) = perform_instruction(instruction, accumulator, i, sign, number)
        if i > last_index:
            is_last_index_reached = True
        
    return (is_last_index_reached, accumulator)

def part_a(boot_code):
    _,accumulator = run_boot_code(boot_code)
    return accumulator

def change_instruction(to_instruction, index, boot_code):
    '''
    Returns the boot_code with the instruction changed to <to_instruction> in the same index
    The signed number is left as it was
    '''
    signed_number = boot_code[index].split(" ")[1]
    new_boot_code = boot_code[:] # This is to do copy by value
    new_boot_code[index] = ' '.join([to_instruction, signed_number])
    return new_boot_code
    

def part_b(boot_code):
    nop_indexes = get_all_nop_instruction_indexes(boot_code)
    jmp_indexes = get_all_jmp_instruction_indexes(boot_code)

    for i in nop_indexes:
        new_boot_code = change_instruction("jmp", i, boot_code)
        (is_last_index_reached, accumulator) = run_boot_code(new_boot_code)
        if is_last_index_reached:
            return accumulator
    for i in jmp_indexes:
        new_boot_code = change_instruction("nop", i, boot_code)
        (is_last_index_reached, accumulator) = run_boot_code(new_boot_code)
        if is_last_index_reached:
            return accumulator


print(part_a(boot_code))
print(part_b(boot_code))