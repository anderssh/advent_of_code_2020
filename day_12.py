from utils import inputfile_to_array
import math
actions = inputfile_to_array("inputs/input_day_12.txt")

heading_dict = {
    "N": 0,
    "E": 90,
    "S": 180,
    "W": 270,
    }

def get_key_from_dict(val, the_dict):
    for key, value in the_dict.items():
         if val == value:
             return key
    return "key doesn't exist"

def change_heading(direction, turn_angle, original_heading):
    if direction == "L":
        turn_angle = -turn_angle
    naive_new_heading = heading_dict.get(original_heading) + turn_angle
    while naive_new_heading < 0:
        naive_new_heading += 360
    normalized_heading = naive_new_heading%360
    return get_key_from_dict(normalized_heading, heading_dict) 

def rotate_waypoint(direction, turn_angle, position):
    x_pos, y_pos = position
    if direction == "L":
        turn_angle = 360 - turn_angle
    turn_angle_increments = int(turn_angle/90)
    for _ in range (turn_angle_increments):
        x_pos, y_pos, = y_pos, -x_pos
    position = (x_pos, y_pos)
    return position

def move_ship(action, heading, position):
    x_position, y_position = position
    letter = action[0]
    number = int(action[1:])
    if letter in ["N","S"]:
        ydiff = round(math.cos(math.radians(heading_dict.get(letter)))) * number
        y_position += ydiff
    elif letter in ["E","W"]:
        xdiff = round(math.sin(math.radians(heading_dict.get(letter)))) * number
        x_position += xdiff
    elif letter in ["L","R"]:
        heading = change_heading(letter, number, heading)
    elif letter == "F":
        xdiff = round((math.sin(math.radians(heading_dict.get(heading))))) * number
        ydiff = round((math.cos(math.radians(heading_dict.get(heading))))) * number
        x_position += xdiff
        y_position += ydiff
    else:
        print("Something is wrong")
        print("The instruction was: ", action)
    position = (int(x_position), int(y_position))
    return heading, position

def move_ship_and_waypoint(action, position_ship, position_waypoint):
    x_position_ship, y_position_ship = position_ship
    x_position_waypoint, y_position_waypoint = position_waypoint
    letter = action[0]
    number = int(action[1:])
    if letter in ["N","S"]:
        ydiff = round(math.cos(math.radians(heading_dict.get(letter)))) * number
        y_position_waypoint += ydiff
    elif letter in ["E","W"]:
        xdiff = round(math.sin(math.radians(heading_dict.get(letter)))) * number
        x_position_waypoint += xdiff
    elif letter in ["L","R"]:
        (x_position_waypoint,y_position_waypoint) = rotate_waypoint(letter, number, position_waypoint)
    elif letter == "F":
        x_position_ship += x_position_waypoint * number
        y_position_ship += y_position_waypoint * number
    else: 
        print("Something is wrong")
        print("The instruction was: ", action)
    position_ship = (int(x_position_ship), int(y_position_ship))
    position_waypoint = (int(x_position_waypoint), int(y_position_waypoint))
    return (position_ship, position_waypoint)

def move_ship_move_ship_and_waypoint_through_instructions(actions):
    position_ship = (0,0)
    position_waypoint = (10,1)
    for action in actions:
        position_ship,position_waypoint = move_ship_and_waypoint(action, position_ship, position_waypoint)
    return (position_ship,position_waypoint)

def move_ship_through_instructions(actions):
    position = (0,0)
    heading  = "E"
    for action in actions:
        heading,position = move_ship(action, heading, position)
    return (heading,position)

def get_manhatten_dist(position):
    x_position, y_position = position
    print("x_position: ", x_position )
    print("y_position: ", y_position )
    return abs(int(x_position)) + abs(int(y_position))


def task_1(actions):
    _,position = move_ship_through_instructions(actions)
    manhatten_dist = get_manhatten_dist(position)
    return manhatten_dist

def task_2(actions):
    position,_ = move_ship_move_ship_and_waypoint_through_instructions(actions)
    manhatten_dist = get_manhatten_dist(position)
    return manhatten_dist

print("The distance in task 1 is: ", task_1(actions))
print("The distance in task 2 is: ", task_2(actions))