katz_deli = []
ANOTHER_DELI = ["Amanda", "Annette", "Ruchi", "Jason",
                "Logan", "Spencer", "Avi", "Joe", "Rachel", "Lindsey"]


def line(waiting_list):
    if len(waiting_list) == 0:
        print("The line is currently empty.")
    else:
        line_of_customers = "The line is currently:"
        if len(waiting_list) > 0:
            for customer in waiting_list:
                line_of_customers += f" {waiting_list.index(customer) + 1}. {customer}"
        print(line_of_customers)


def take_a_number(line, name_to_add):
    line.append(name_to_add)
    line_number = int(line.index(name_to_add))
    print(
        f"Welcome, {name_to_add}. You are number { line_number + 1} in line.")


def now_serving(line):
    if len(line) == 0:
        print("There is nobody waiting to be served!")
    elif len(line) > 0:
        next_in_line = line.pop(0)
        print(f"Currently serving {next_in_line}.")
