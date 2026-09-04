# Arithmetic Operations
from pyscript import display, document

def adding_numbers(e): # this operation adds the two numbers together
    first_number = float(document.getElementById("num1").value)
    second_number = float(document.getElementById("num2").value)
    sum = first_number + second_number

    display(f'The sum of {first_number} and {second_number} is {sum}', target='output') # displaying the result

def subtracting_numbers(e): # this operation subtracts the second number from the first number
    first_number = float(document.getElementById("num1").value)
    second_number = float(document.getElementById("num2").value)
    difference = first_number - second_number

    display(f'The difference of {first_number} and {second_number} is {difference}', target='output') # displaying the result

def multiplying_numbers(e): # this operation multiplies the two numbers
    first_number = float(document.getElementById("num1").value)
    second_number = float(document.getElementById("num2").value)
    product = first_number * second_number

    display(f'The product of {first_number} and {second_number} is {product}', target='output') # displaying the result

def dividing_numbers(e): # this operation divides the first number by the second number
    first_number = float(document.getElementById("num1").value)
    second_number = float(document.getElementById("num2").value)
    quotient = first_number / second_number

    display(f'The quotient of {first_number} and {second_number} is {quotient}', target='output') # displaying the result

def modulus_numbers(e):
    first_number = float(document.getElementById("num1").value)
    second_number = float(document.getElementById("num2").value)
    remainder = first_number % second_number

    display(f'The remainder of {first_number} and {second_number} is {remainder}', target='output') # displaying the result

def exponent_numbers(e):
    first_number = float(document.getElementById("num1").value)
    second_number = float(document.getElementById("num2").value)
    exponent = first_number ** second_number

    display(f'{first_number} raised to the power of {second_number} is {exponent}', target='output') # displaying the result

def floor_division_numbers(e):
    first_number = float(document.getElementById("num1").value)
    second_number = float(document.getElementById("num2").value)
    floor_quotient = first_number // second_number

    display(f'The floor division of {first_number} and {second_number} is {floor_quotient}', target='output') # displaying the result
