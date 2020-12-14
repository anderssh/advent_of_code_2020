from utils import inputfile_to_array

seat_map = inputfile_to_array("inputs/input_day_11.txt")
def perform_seating(seat_map, seating_algorithm):
    if seating_algorithm == 1:
        occupied_set_threshold = 4
    else:
        occupied_set_threshold = 5
    out_map = seat_map[:]

    for i in range(len(seat_map)):
        for j in range(len(seat_map[0])):
            if seating_algorithm == 1:
                relevant_seats = get_adjacent_seats(seat_map,i,j)
            else:
                relevant_seats = get_visible_seats(seat_map,i,j) 
            row_as_string = out_map[i]
            if seat_map[i][j] == "L":
                if num_ocupied_relevant_seats(seat_map, relevant_seats) == 0:
                    out_map[i] = row_as_string[:j] + "#" + row_as_string[j + 1:]
            elif seat_map[i][j] == "#":
                if num_ocupied_relevant_seats(seat_map, relevant_seats) >= occupied_set_threshold:
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
        try:
            if seat_map[seat_row][seat_column] == "#":
                occupied_counter += 1
        except:
            print("This position has an error!", seat_row, seat_column)
            exit(1)

    return occupied_counter

def get_visible_seats(seat_map, row_number, column_number):
    positions = set()

    directions = []
    if row_number == 0 and column_number == 0:
        directions = ["E", "SE", "S"]
    elif row_number == 0 and column_number == (len(seat_map[0])-1):
        directions = ["S", "SW", "W"]
    elif row_number == (len(seat_map)-1) and column_number == 0:
        directions = ["N", "NE", "E"]
    elif row_number == (len(seat_map)-1) and column_number == (len(seat_map[0])-1):
        directions = ["N", "W", "NW"]
    elif row_number == 0:
        directions = ["E", "SE", "S", "SW", "W"]
    elif row_number == (len(seat_map)-1):
        directions = ["N", "NW", "W", "NE", "E"]
    elif column_number == 0:
        directions = ["NE", "E", "SE", "S", "N"]
    elif column_number == (len(seat_map[0])-1):
        directions = ["N", "NW", "SW", "W", "S"]
    elif (0 < row_number < len(seat_map)- 1) and (0 < column_number < len(seat_map[0])-1):
        directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    else:
        print("SOMETHING IS SUPER WRONG")
        print("Row number: ", row_number)
        print("column number: ", column_number)
        exit(1)
    
    distance_to_end_of_row = len(seat_map) -1 - row_number
    distance_to_end_of_column = len(seat_map[0]) -1 - column_number
    least_distance_to_start = min(row_number, column_number)
    least_distance_to_end   = min(distance_to_end_of_row, distance_to_end_of_column)
    least_distance_row_start_column_end = min(row_number, distance_to_end_of_column)
    least_distance_row_end_column_start = min(column_number, distance_to_end_of_row)

    if "N" in directions:
        for i in range(row_number - 1, -1, -1):
            positions.add((i,column_number))
            if seat_map[i][column_number] in ["#","L"]:
                break
    if "NE" in directions:
        counter = 1
        for i in range(row_number- 1, (row_number - least_distance_row_start_column_end) -1, -1):
            positions.add((i,column_number+counter))
            if seat_map[i][column_number+counter]  in ["#","L"]:
                break
            counter += 1
    if "E" in directions:
        for i in range(column_number +1, len(seat_map[0])):
            positions.add((row_number,i))
            if seat_map[row_number][i]  in ["#","L"]:
                break
    if "SE" in directions:
        counter = 1
        for i in range(row_number + 1,row_number + least_distance_to_end+1):
            positions.add((i,column_number+counter))
            if seat_map[i][column_number+counter]  in ["#","L"]:
                break
            counter += 1
    if "S" in directions:
        for i in range(row_number +1, len(seat_map)):
            positions.add((i,column_number))
            if seat_map[i][column_number]  in ["#","L"]:
                break
    if "SW" in directions:
        counter = 1
        for i in range(row_number+ 1, row_number + least_distance_row_end_column_start+1):
            positions.add((i,column_number-counter))
            if seat_map[i][column_number-counter]  in ["#","L"]:
                break
            counter += 1
    if "W" in directions:
        for i in range(column_number -1, -1, -1):
            positions.add((row_number,i))
            if seat_map[row_number][i]  in ["#","L"]:
                break
    if "NW" in directions:
        counter = 1
        for i in range(row_number- 1, (row_number - least_distance_to_start)-1, -1):
            positions.add((i,column_number-counter))
            if seat_map[i][column_number-counter]  in ["#","L"]:
                break
            counter += 1
    return positions

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
            positions.append((row_number,column_number))
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
            positions.append((row_number,column_number-1))
            positions.append((row_number-1,column_number-1))
            positions.append((row_number+1,column_number-1))
        elif column_number == 0:
            positions.append((row_number,column_number+1))
            positions.append((row_number-1,column_number+1))
            positions.append((row_number+1,column_number+1))
        else:
            positions.append((row_number,column_number-1))
            positions.append((row_number,column_number+1))
            positions.append((row_number+1,column_number-1))
            positions.append((row_number+1,column_number+1))
            positions.append((row_number-1,column_number-1))
            positions.append((row_number-1,column_number+1))
    return positions
def get_last_seating(seat_map, seating_algorithm):
    perform_seating_counter = 0
    old_seat_map = seat_map[:]
    while True:
        perform_seating_counter += 1
        #print("So many rounds in perform_seating:", perform_seating_counter)
        new_seating = perform_seating(old_seat_map, seating_algorithm)
        #print("The number of taken seats are:", count_num_occupied_seats(new_seating))
        if new_seating == old_seat_map:
            return new_seating
        old_seat_map = new_seating

def task_1(seat_map):
    last_seating = get_last_seating(seat_map, 1)
    return count_num_occupied_seats(last_seating)

def task_2(seat_map):
    last_seating = get_last_seating(seat_map, 2)
    return count_num_occupied_seats(last_seating)

print(task_1(seat_map))
print(task_2(seat_map))
