import sys
import requests
import os.path


def inputfile_to_array(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()
    lines_as_array = [(line) for line in lines]
    return lines_as_array

def get_input_file(day):

    url = "https://adventofcode.com/2020/day/" + str(day) + "/input"
    filepath = 'inputs/input_day_' + str(day) + ".txt"

    if not os.path.isfile(filepath):
        r = requests.get(url)
        open(filepath, 'wb').write(r.content)
