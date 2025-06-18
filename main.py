name = "Boja"
print("Hi "+name)

import keyword
print(keyword.kwlist)

name = 'Boja'
print("He like's dog.")
para = """This is a

sample text."""
print(para)

"""
This is a comment
"""

name= "Boja"
age = "25"

# print("Hi my name is " + name + " and I am " + age + " years old.")
#print(f"Hi my name is {name} and I am {age}year old.")
print("Hi my name is {} and I am {} years old.".format(name, age))

a = 0
a = -13.3
a = 2 + 3j
a = -1j
print(a)

a = 10
b = 3

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)
# print(a**b)

# import random

# print(random.random())
# print(random.randint(1,10))
# print(random.choice([2, 3, 5, 6, 8]))

FILE_SIZE=1_00_000
print(FILE_SIZE)

# a = 10
# b = 3

# print(a <= b)

# if (cond):
    # if-block

# age = int(input("Enter your age: "))
                
# if age>=18:

#     print("you can vote!")
# else:
#     print("you cannot vote.")

# if age<5:
#     print("you have to pay 50.")
# elif age < 16:
#     print("you have to pay 100.")
# else:
#     print("you have to pay 200.")

# age = int(input("Enter your age: "))  

# value_if_true if condition else value_if_false

# result = "you can vote!" if age >=18 else "you cannot vote."
# print(result)

# for _ in range(6):
#     print("Hello World")

# for i in range(2,7):
#     print(i)

# for i in range(2,12,2):
#     print(i)

max = 5
counter = 0

while counter < max:
    # 0 < 5
    # 1 < 5
    # 2 < 5
    # 3 < 5
    # 4 < 5
    # 5 < 5

    print(counter)
    counter +=1
    
correct_pin = "1234"
balance = 5000

pin = input("Enter your pin: ") 

print("1. Check Balance")
print("2. Withdraw Money")
print("3. Deposit Money")

option = int(input("Enter (1, 2, 3): "))
if option == 1:
    print("your current balance is 5000: ")
elif option == 2:
    amount = int(input("Enter amount to withdraw: "))
    print("Withdraw amount = 2000: ")
elif option == 3:
    amount = int(input("Enter amount to deposit: "))
    print("deposit money 5000: ")
else:
    print("Invalid option.")

for _ in range(3):
    print("withdraw amount")

# def rectangle(n):
#     return n * n
# def print_rectangle(n):
#     result = rectangle(n)
#     print(f"rectangle of {n} is {result}")
# num = int(input("Enter a number: ")) 
#     print_rectangle(num) 

# def ctof(c):
#     return (c * 9/5) + 32
# print(ctof(41))
# print(ctof(52))

# def welcome(func):
#     def wrapper():
#         print("Welcome!")
#         func()
#         print("Thanks for visiting.")
#     return wrapper

# @welcome
# def say_hi():
#     print("Hi")
# say_hi()
try:
    age = int(input("Enter your age: "))
    result = 25/age
    print(result)
except ValueError:
    print("invalid input! please enter a number.")
except Exception:
    print(age)
try:
    x = 5
    y = "9"
    print(x + y)
except TypeError:
    print("unsupported operand type(s) for +.")
except type:
    print(x + int(y))
try:
    num = int(input("Enter a number: "))
    result = 10/num
    print(result)
except ZeroDivisionError:
    print("you cannot divide a number by 0.")
except Exception as e:
    print(e)
try:
    colors = ["black", "red", "green"]
    print([3])
except IndexError:
    print("list index out of range")
except Exception:
    print([2])
finally:
    print("END")

import pricing as p

final_price = p.get_final_price(100)
print(final_price)

print(p.say_hello())

from pricing import say_hello, get_final_price

print(say_hello())
final_price = get_final_price(200)
print(final_price)
print(get_final_price(500))

import pandas as pd

df = pd.DataFrame(['a', 'b', 'c'])
print(df)













    





































       