def invalid_operator(operator):
    return not any([operator == "+", operator == "-"])

def too_many_digits(string_1, string_2):
    return (len(string_1) > 4 or len(string_2) > 4)

def too_many_operations(lst):
    return len(lst) > 5

def not_digits(string_1, string_2):
    return (not string_1.isdigit() or not string_2.isdigit())

def break_down(string):
    first_number = string.split()[0]
    operator = string.split()[1]
    second_number = string.split()[2]
    
    return first_number, operator, second_number

def determine_longest_number(string_1, string_2):
    if len(string_1) > len(string_2):
      return string_1
    else:
      return string_2

def last_operation(operation, list_of_operations):
    return operation == list_of_operations[-1]

def arithmetic_arranger(list_of_operations, has_to_show_answer=False):
    if too_many_operations(list_of_operations):
      return "Error: Too many problems."

    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    for operation in list_of_operations:
        first_number, operator, second_number = break_down(operation)
        
        if too_many_digits(first_number, second_number):
            return "Error: Numbers cannot be more than four digits."
        elif invalid_operator(operator):
            return "Error: Operator must be '+' or '-'."
        elif not_digits(first_number, second_number):
            return "Error: Numbers must only contain digits."
        
        long_number = determine_longest_number(first_number, second_number)
        len_of_long_number = len(long_number)
        
        first_line += f"{first_number}".rjust(len_of_long_number + 2)
        second_line += f"{operator} {second_number.rjust(len_of_long_number)}"
        third_line += f"{'-' * (len_of_long_number + 2)}"

        if has_to_show_answer:
            match operator:
                case "+":
                    answer = int(first_number) + int(second_number)
                case "-":
                    answer = int(first_number) - int(second_number)

            fourth_line += str(answer).rjust(len_of_long_number + 2)

        if last_operation(operation, list_of_operations):
            first_line += "\n"
            second_line += "\n"
        
        if has_to_show_answer:
            third_line += "\n"
        else:
            first_line += "    "
            second_line += "    "
            third_line += "    "
            fourth_line += "    "

    arranged_arithmetic = first_line + second_line + third_line
    if has_to_show_answer:
        return arranged_arithmetic + fourth_line
    else:
        return arranged_arithmetic
