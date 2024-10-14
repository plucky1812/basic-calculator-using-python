"""
Python Calculator
Author: Lucky Singh
Date: [Date of Issue, e.g., October 14, 2024]

Description:
This program is a simple calculator built using Python that can perform basic arithmetic operations 
as well as some advanced functions. It supports the following features:

Features:
- Addition: Adds two numbers.
- Subtraction: Subtracts one number from another.
- Multiplication: Multiplies two numbers.
- Division: Divides one number by another, with error handling for division by zero.
- Square: Calculates the square of a given number.
- Cube: Calculates the cube of a given number.

Usage:
Run the script and follow the prompts to perform different calculations.
"""




def cal(choice):
    no1 = 0
    no2 = 0
    output = 0

    if choice == 1:
        print("\t\t\n\n*************ADDITION**************\n\n")
        no1 = int(input("ENTER no1 : "))
        no2 = int(input("ENTER no2 : "))
        output = no1 + no2
        print(f"{no1}  + {no2} = {output}" )
        print("\t\t\n\n**********************************\n\n")

        
    elif choice == 2:
        print("\t\t\n\n*************SUBRACTION**************\n\n")
        no1 = int(input("ENTER no1 : "))
        no2 = int(input("ENTER no2 : "))
        output = no1 - no2
        print(f"{no1}  - {no2} = {output}" )
        print("\t\t\n\n**********************************\n\n")

        
    elif choice == 3:
        print("\t\t\n\n*************MULTIPLICATION**************\n\n")
        no1 = int(input("ENTER no1 : "))
        no2 = int(input("ENTER no2 : "))
        output = no1 * no2
        print(f"{no1}  * {no2} = {output}" )
        print("\t\t\n\n**********************************\n\n")

        
    elif choice == 4:
        print("\t\t\n\n*************DIVISION**************\n\n")
        no1 = int(input("ENTER no1 : "))
        no2 = int(input("ENTER no2 : "))
        output = no1 / no2
        print(f"{no1}  + {no2} = {output}" )
        print("\t\t\n\n**********************************\n\n")

        
    elif choice == 5 :
        print("\t\t\n\n*************SQUARE ROOT**************\n\n")
        no1 = int(input("ENTER no1(base) : "))
        output = no1 ** 2
        print(f"{no1}  ** 2 = {output}" )
        print("\t\t\n\n**********************************\n\n")

        
    elif choice == 6:
        print("\t\t\n\n*************CUBE**************\n\n")
        no1 = int(input("ENTER no1 (base): "))
        output = no1 ** 3
        print(f"{no1} ** 3 = {output}" )
        print("\t\t\n\n**********************************\n\n")

    else:
        pass

c = "y"
while c == "y":              
    print("\t\t------------calculator code---------------\n\n\n")
    print("\t\t 1. ADDITION ")
    print("\t\t 2. SUBRACTION ")
    print("\t\t 3. MULTIPILCATION ")
    print("\t\t 4. DIVISION ")
    print("\t\t 5. SQUARE ROOT ")
    print("\t\t 6. CUBE ")
    choice = int(input("\t ENTER YOUR CHOICE : "))

    if choice > 6 or choice < 1:
        print("invalid choice")
    else:
        cal(choice)
    c = input("do you want to continue (y/n)")








