import pytest
from src.calculator import calculator as calc
import math
# 3 tests parametrized for the hypotenuse function
@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        pytest.param(3,4,5, id="Getting the hypotenuse of a right triangle with sides 3 and 4"),
        pytest.param(8,15,17, id="Getting the hypotenuse of a right triangle with sides 8 and 15"),
        pytest.param(10,11,14.87, id="Getting the hypotenuse of a right triangle with sides 10 and 11")    
        ],
)


def test_hypotenus(input_a,input_b,expected):
    """Tests the hypotenuse function"""
    assert calc.hypotenuse(input_a, input_b) == expected
 

# 3 tests parametrized for the area of the circle function
@pytest.mark.parametrize(
    "input_radius, expected",
    [
        pytest.param(-2, 12.56636, id="Getting the area of a circle with radius 2"),
        pytest.param(5, 78.53975, id="Getting the area of a circle with radius 5"),
        pytest.param(10, 314.159, id="Getting the area of a circle with radius 10")    
        ],
) 

def test_area_of_circle(input_radius, expected):
    """Tests the area of circle function"""
    assert calc.area_of_circle(input_radius) == expected


# 3 tests parametrized for the area of the triangle function
@pytest.mark.parametrize(
    "input_length, input_breadth, expected",
    [
        pytest.param(2, 3, 3, id="Getting the area of a triangle with base 2 and height 3"),
        pytest.param(-5, 6, -15, id="Getting the area of a triangle with base 5 and height 6"),
        pytest.param(-8, -9, 36, id="Getting the area of a triangle with base 8 and height 9")    
        ],
)
  
def test_area_of_triangle(input_length, input_breadth, expected):
    """Tests the area of triangle function"""
    assert calc.area_of_triangle(input_length, input_breadth) == expected

# 3 tests parametrized for the square function
@pytest.mark.parametrize(
    "input_num, expected",
    [
        pytest.param(2, 4, id="Getting the square of 2"),
        pytest.param(-5, 25, id="Getting the square of 5"),
        pytest.param(3, 9, id="Getting the square of 8")    
        ],
)
def test_squareNums(input_num, expected):
    """Tests the square function"""
    assert calc.squareNums(input_num) == expected

# 3 tests parametrized for the tri function
@pytest.mark.parametrize(
    "input_num, expected",
    [
        pytest.param(2, 3, id="Getting the tri number of 2"),
        pytest.param(5, 15, id="Getting the tri number of 5"),
        pytest.param(8, 36, id="Getting the tri number of 8")    
        ],
)    
def test_triNums(input_num, expected):
    """Tests the tri function"""
    assert calc.triNums(input_num) == expected

# 3 tests parametrized for the lazy caterer function
@pytest.mark.parametrize(
    "input_num, expected",
    [
        pytest.param(2, 4, id="Getting the lazy caterer number of 2"),
        pytest.param(5, 16, id="Getting the lazy caterer number of 5"),
        pytest.param(8, 37, id="Getting the lazy caterer number of 8")    
        ],
)
def test_lazyCaterer(input_num, expected):
    """Tests the lazy caterer function"""
    assert calc.lazyCaterer(input_num) == expected

# 3 tests parametrized for the magic squares function
@pytest.mark.parametrize(
    "input_num, expected",
    [
        pytest.param(2, 5, id="Getting the magic squares number of 2"),
        pytest.param(5, 65, id="Getting the magic squares number of 5"),
        pytest.param(8, 260, id="Getting the magic squares number of 8")    
        ],
)

def test_magicSquares(input_num, expected):
    """Tests the magic squares function"""
    assert calc.magicSquares(input_num) == expected

    

