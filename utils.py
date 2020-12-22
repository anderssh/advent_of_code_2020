import sys
import requests
import os.path


def inputfile_to_array(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()
    lines_as_array = [(line) for line in lines]
    return lines_as_array


def get_input_file(day):

    cookie = {'session': '53616c7465645f5f34699b1a42077135613779bde9a5cef0f4fe370130cfb858f92e79d59582a9738b984ff6a1578819'}
    url = "https://adventofcode.com/2020/day/" + str(day) + "/input"
    filepath = 'inputs/input_day_' + str(day) + ".txt"

    if not os.path.isfile(filepath):
        r = requests.get(url, cookies = cookie)
        open(filepath, 'wb').write(r.content)

def remove_empty_lines_and_concat(list_with_empty_lines, space_separated = True):
    '''
    Takes in the list as read from the file, puts the lines that belong together in
    same list element.
    '''
    space_character = ''
    if space_separated:
        space_character = ' '
    element = ''
    line_list = []
    for i, item in enumerate(list_with_empty_lines):
        if item == "":
            line_list.append(element)
            element = ''
        else:
            if element == '':
                element = element + item
            else:
                element = element + space_character + item
            if i == len(list_with_empty_lines)-1:
                line_list.append(element)
    return line_list