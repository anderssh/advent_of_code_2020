from utils import inputfile_to_array
import re
bus_table = inputfile_to_array("inputs/input_day_13.txt")

def get_timestamp_and_bus_list(bus_table):
    timestamp = int(bus_table[0])
    busses_raw = bus_table[1]

    bus_list = re.findall('[0-9]+', busses_raw)
    bus_list = [int(item) for item in bus_list] 
    return timestamp,bus_list

def get_earliest_bus(timestamp, bus_list):
    earliest_bus = bus_list[0]
    time_to_arrival = 99999999999
    for bus_time in bus_list:
        new_time_to_arrival = int(bus_time) - (timestamp % bus_time)
        if new_time_to_arrival < time_to_arrival:
            time_to_arrival = new_time_to_arrival
            earliest_bus = bus_time
    return earliest_bus, time_to_arrival

def task_1(bus_table):
    timestamp, bus_list = get_timestamp_and_bus_list(bus_table)
    print(timestamp)
    print(bus_list)
    earliest_bus, time_to_arrival = get_earliest_bus(timestamp, bus_list)
    return (earliest_bus * time_to_arrival)

print(task_1(bus_table))