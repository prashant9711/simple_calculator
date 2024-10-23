"""This module contains the calculator functions for the formulas square, tri, lazy caterer, and magic squares"""

# 3 new functions: hypotenus, area of circle and area of triangle

def hypotenuse(a, b):    
    """Calculates the hypotenuse of a right triangle"""
    return round((a**2 + b**2)**0.5, 2)

def  area_of_circle(r):
    """Calculates the area of a circle"""
    return 3.14159 * r**2

def area_of_triangle(b, h):
    """Calculates the area of a triangle"""
    return 0.5 * b * h

# done with the new functions

def squareNums(n):
    """Calculates the square"""
    # fixed the case where the user enters a square root number
    
    return (n**2)


def triNums(n):
    """Calculates the tri number"""
    return (n * (n + 1)) / 2


def lazyCaterer(n):
    """Calculates the lazy caterer number"""
    return (n**2 + n + 2) / 2


def magicSquares(n):
    """Calculates the magic squares number"""
    return (n * (n**2 + 1)) / 2


def run_calculator(input_formula, input_num):
    """Calls and returns results for the specified formulas"""
    calculator = [squareNums, triNums, lazyCaterer, magicSquares]
    formula = calculator[input_formula - 1]
    return_result = formula(input_num)
    return return_result


if __name__ == "__main__":
    print(
        "Choose which formula to use: 1 for square, 2 for tri, 3 for lazy caterer, 4 for magic squares"
    )
    input_formula = int(input())
    print(
        "Enter a number to calculate the square, tri, lazy caterer, and magic squares numbers"
    )
    input_num = int(input())

    result = run_calculator(input_formula, input_num)
    print(result)
