#!/usr/bin/env python3

def admin_login(username, password):
    if (username.upper() == "ADMIN" and password == "12345"):
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if (temperature < 40):
        return "It's brisk out there!"
    elif (temperature < 65):
        return "It's a little chilly out there!"
    elif (temperature < 85 ):
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"
hows_the_weather(33)
hows_the_weather(55)
hows_the_weather(99)
hows_the_weather(75)

def fizzbuzz(num):
    if (num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    elif (num % 3 == 0):
        return "Fizz"
    elif (num % 5 == 0):
        return "Buzz"
    else:
        return num
    
fizzbuzz(0)
fizzbuzz(15)
fizzbuzz(45)

def calculator(operation, num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        print('Invalid operation!')
        return None
    elif (operation == '+'):
        return num1 + num2
    elif (operation == '-'):
        return num1 - num2
    elif (operation == '*'):
        return num1 * num2
    elif (operation == '/'):
        if num2 != 0:
            return num1 / num2
        else:
            print('Division by zero error!')
            return None
    else:
        print('Invalid operation!')
        return None
 
calculator("+", 1, 2)
calculator("+", 5, 7)
calculator("+", 9, 90)
