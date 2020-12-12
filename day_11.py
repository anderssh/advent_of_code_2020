from utils import inputfile_to_array

seat_map = inputfile_to_array("inputs/input_day_11.txt")

def perform_seating(seat_map):
    out_map = seat_map[:]
    for i in range(len(seat_map)):
        for j in range(len(seat_map[0])):
            adjacent_seats = get_adjacent_seats(seat_map,i,j)
            row_as_string = out_map[i]
            if seat_map[i][j] == "L":
                if num_ocupied_relevant_seats(seat_map, adjacent_seats) == 0:
                    out_map[i] = row_as_string[:j] + "#" + row_as_string[j + 1:]
            elif seat_map[i][j] == "#":
                if num_ocupied_relevant_seats(seat_map, adjacent_seats) >= 4:
                    out_map[i] = row_as_string[:j] + "L" + row_as_string[j + 1:]
    return out_map

def count_num_occupied_seats(seat_map):
    occupied_counter = 0
    for i in range(len(seat_map)):
        for j in range(len(seat_map[0])):
            if seat_map[i][j] == "#":
                occupied_counter +=  1
    return occupied_counter

def num_ocupied_relevant_seats(seat_map, relevant_seats):
    occupied_counter = 0
    for seat in relevant_seats:
        seat_row,seat_column = seat
        if seat_map[seat_row][seat_column] == "#":
            occupied_counter += 1
    return occupied_counter

def get_adjacent_seats(seat_map, row_number, column_number):
    positions = []
    if row_number == (len(seat_map)-1):
        positions.append((row_number-1,column_number))
        if column_number == (len(seat_map[0])-1):
            positions.append((row_number-1,column_number-1))
            positions.append((row_number,column_number-1))
        elif column_number == 0:
            positions.append((row_number-1,column_number+1))
            positions.append((row_number,column_number+1))
        else:
            positions.append((row_number-1,column_number-1))
            positions.append((row_number-1,column_number+1))
            positions.append((row_number,column_number-1))
            positions.append((row_number,column_number+1))
    elif row_number == (0):
        positions.append((row_number+1,column_number))
        if column_number == (len(seat_map[0])-1):
            positions.append((row_number,column_number-1))
            positions.append((row_number,column_number-1))
        elif column_number == 0:
            positions.append((row_number,column_number+1))
            positions.append((row_number+1,column_number+1))
        else:
            positions.append((row_number,column_number-1))
            positions.append((row_number,column_number+1))
            positions.append((row_number+1,column_number-1))
            positions.append((row_number+1,column_number+1))
    else:
        positions.append((row_number+1,column_number))
        positions.append((row_number-1,column_number))
        if column_number == (len(seat_map[0])-1):
            positions.append((row_number+1,column_number-1))
            positions.append((row_number-1,column_number-1))
            positions.append((row_number,column_number-1))
        elif column_number == 0:
            positions.append((row_number,column_number+1))
            positions.append((row_number-1,column_number-1))
            positions.append((row_number+1,column_number-1))
        else:
            positions.append((row_number,column_number-1))
            positions.append((row_number,column_number+1))
            positions.append((row_number+1,column_number-1))
            positions.append((row_number+1,column_number))
            positions.append((row_number+1,column_number+1))
            positions.append((row_number-1,column_number-1))
            positions.append((row_number-1,column_number))
            positions.append((row_number-1,column_number+1))
    return positions
def get_last_seating(seat_map):
    perform_seating_counter = 0
    old_seat_map = seat_map[:]
    while True:
        perform_seating_counter += 1
        print("So many rounds in perform_seating:", perform_seating_counter)
        new_seating = perform_seating(old_seat_map)
        print("The number of taken seats are:", count_num_occupied_seats(new_seating))
        if new_seating == old_seat_map:
            return new_seating
        old_seat_map = new_seating

def task_1(seat_map):
    last_seating = get_last_seating(seat_map)

    return count_num_occupied_seats(last_seating)

print(task_1(seat_map))
