#!/usr/bin/env python3
def admin_login(username, password):
    if username == "admin" and password == "12345":
        return "Access granted"
    elif username == "Admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    
def hows_the_weather(temperature):
    if temperature < 40:
        return "brisk"
    elif temperature >= 40 and temperature <= 65:
        return "a little chilly"
    elif temperature > 85:
        return "too dang hot"
    else:
        return "perfect"
    
def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    
def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Invalid operation"
 
# def divide(num1, num2):
#     try:
#         quotient = num1 / num2
#         print(quotient)
#     except ZeroDivisionError:
#         print("Error: num2 cannot be equal to 0")
#     except TypeError:
#         print("Error: input must be of type int or float")
#     finally:
#         print("Isn't division fun?")

# dog = "cuddly"

# dict_map = {
#     "hungry": "Refilling food bowl.",
#     "thirsty": "Refilling water bowl.",
#     "playful": "Playing tug-of-war.",
#     "cuddly": "Snuggling.",
# }

# # Remember that a dictionary's .get() method lets us set a default value!
# owner = dict_map.get(dog, "Reading newspaper.")