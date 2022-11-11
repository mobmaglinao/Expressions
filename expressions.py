import math

def calc_math_expression(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == ":":
        if num2 == 0:
            return None
        else:
            return num1 / num2
    else:
        return None

def calc_math_expression_from_str(str_input):
    equation = str_input.split()
    num1 = float(equation[0])
    num2 = float(equation[2])
    operator = equation[1]
    return calc_math_expression(num1, num2, operator)

def find_largest_and_smallest_numbers(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        if num2 <= num1 and num2 <= num3:
            return num1, num2
        else:
            return num1, num3
    elif num2 >= num1 and num2 >= num3:
        if num1 <= num2 and num1 <= num3:
            return num2, num1
        else:
            return num2, num3
    elif num3 >= num1 and num3 >= num2:
        if num1 <= num2 and num1 <= num3:
            return num3, num1
        else:
            return num3, num2

def quadratic_equation_solver(a, b, c):
    root = (b**2 - 4*a*c)
    if root < 0:
        return None, None

    elif root == 0:
        solution1 = (-b) / (2*a)
        return solution1, None
    else:
        solution1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        solution2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
        return solution1, solution2

def quadratic_equation_solver_from_user_input():
    user_input = str(input("Please enter values for a, b, and c: "))
    quadratic_input = user_input.split()
    a = float(quadratic_input[0])
    b = float(quadratic_input[1])
    c = float(quadratic_input[2])
    if a == 0:
        print("ERROR: a cannot be 0")
    else:
        return quadratic_equation_solver(a, b, c)


def temp_checker(min_temp, temp_1, temp_2, temp_3):
    if min_temp < (temp_1 and temp_2) or min_temp < (temp_1 and temp_3) or min_temp < (temp_2 and temp_3):
        return True
    else:
        return False



