import re
from utils import inputfile_to_array, remove_empty_lines_and_concat
from math import floor, ceil
from statistics import mean 

luggage_rules = inputfile_to_array("inputs/input_day_7.txt")

def bags_that_can_contain_directly(luggage_rules, bags_to_search_for):

    bags_that_can_contain_bag_to_search_for = set()
    for luggage_rule in luggage_rules:
        outer_bag = luggage_rule.split("contain")[0].strip().replace("bags","").strip()
        content   = luggage_rule.split("contain")[-1].strip()
        inner_bags_unsanitized = content.split(",")
        inner_bags = []
        for bag in inner_bags_unsanitized:
            inner_bags.append(bag.replace(".","").replace("bags","").replace("bag","").strip())
        for bag_to_search_for in bags_to_search_for:
            for inner_bag in inner_bags:
                if bag_to_search_for in inner_bag:
                    bags_that_can_contain_bag_to_search_for.add(outer_bag)
    return (bags_that_can_contain_bag_to_search_for)

def get_value_of_bag(luggage_rules, input_bag):
    content_of_bag = get_content_of_bag(luggage_rules, input_bag)
    if content_of_bag:
        value = 1
        for i in content_of_bag:
            number,bag = i
            value +=  int(number) * int(get_value_of_bag(luggage_rules, bag))
        return value
    else:
        return 1

def get_content_of_bag(luggage_rules, input_bag):

    number_and_bag_list = []
    for luggage_rule in luggage_rules:
        outer_bag = luggage_rule.split("contain")[0].strip().replace("bags","").strip()
        if outer_bag == input_bag:
            unsanitized_content = luggage_rule.split("contain")[-1].strip().split(",")
            if "no other" in unsanitized_content[0]:
                return False
            for inner_bag in unsanitized_content:
                inner_bag = inner_bag.strip()
                number_and_bag_list.append((inner_bag.split(" ")[0]," ".join(inner_bag.split(" ")[1:3])))
    return number_and_bag_list


def task_a(luggage_rules):
    bags_to_look_for = {"shiny gold"}
    solution_bags = set()
    while bool(bags_to_look_for):
        (bags_from_this_run)  = bags_that_can_contain_directly(luggage_rules, bags_to_look_for)
        solution_bags = solution_bags | bags_from_this_run
        bags_to_look_for = bags_from_this_run
    return len(solution_bags)

def task_b(luggage_rules):
    bag = "shiny gold"
    return get_value_of_bag(luggage_rules, bag)-1 # Here I have to subtract 1 because the top bag itself is not to be counted 

print("Number of bags that can have at least one shiny gold bag in task a:", task_a(luggage_rules))
print("Number of bags included in a shiny gold bag in task b:", task_b(luggage_rules))

