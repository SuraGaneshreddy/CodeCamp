# Write a program to input 2 number and an arithmetic operator.
# from unittest import result
i = int(input("Enter first Number: "))
j = int(input("Enter second Number: "))
operator = input("Enter an operator (+,-,*,/,%): ")
if operator == '+':
    result = i + j
    print("Addition is: ",result)
if operator == '-':
    result = i - j
    print("Subtraction is : ",result)
if operator == '*':
    result = i * j
    print("Multiplication is : ",result)
if operator == '/':
    result = i / j
    print("Division is : ",result)
if operator == '%':
    result = i % j
    print("Modulus is : ",result)