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




    





































       