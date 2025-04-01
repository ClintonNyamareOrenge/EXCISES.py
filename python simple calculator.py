"""
simple calculator
"""
import math

digit1= float(input("Enter the first digit: "))
arithmetic_expression=input("Enter the arithmetic operator(- + * ** % /)")
digit2= float(input("Enter the second digit: "))


if arithmetic_expression=="+":
    result=digit1+digit2
    print(f"the result of the addtion is: {round(result,3)}")
elif arithmetic_expression=="-":
    result=digit1-digit2
    print(f"the result of the subtraction is: {round(result,3)}")
elif arithmetic_expression=="*":
    result=digit1*digit2
    print(f"the result of the multiplication is: {round(result,3)}")
elif arithmetic_expression=="/":
    result=digit1/digit2
    print(f"the result of the division is: {round(result,3)}")
elif arithmetic_expression=="**":
    result=digit1*digit2
    print(f"the result of the calculation is: {round(result,3)}")
elif arithmetic_expression=="%":
    result=digit1%digit2
    print(f"the result of the modulos is: {round(result,3)}")
else:
    print("math error")