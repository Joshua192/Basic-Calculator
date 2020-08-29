from Operators import addition, divide, multiply, subtraction
import math

a = int(input("Input a first number: "))
op = str(input("Input an operator: "))
b = int(input("Input a second number: "))

if op == '+':
    print(addition(a, b))
if op == '-':
    print(subtraction(a, b))
if op == '/':
    print(divide(a, b))
if op == '*':
    print(multiply(a, b))
