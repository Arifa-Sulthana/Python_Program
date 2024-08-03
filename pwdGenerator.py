import random
import string
print("Welcome to the PyPassword Generator!")

l1=string.ascii_letters
l2='!@#$%^&*()~'
l_in=int(input("How many letters would you like in your password?\n"))
s_in=int(input("How many symbols would you like?\n"))
n_in=int(input("How many numbers would you like?\n"))
letter=""
symbol=""
number =""
for i in range(l_in):
    op=random.choice(l1)
    print(op)
    letter += str(op)
print(letter)
for i in range(s_in):
    op= random.choice(l2)
    print(op)
    symbol += str(op)
for i in range(n_in):
    op=random.randint(0,9)
    print(op)
    number += str(op)
fl=letter+symbol+number
print(fl)
fl=''.join(random.sample(fl,len(fl)))
print(f"Your password is: {fl}")

# import random
# import string
# print("Welcome to the PyPassword Generator!")

# l1=string.ascii_letters
# l2='!@#$%^&*()~'
# l_in=int(input("How many letters would you like in your password?\n"))
# s_in=int(input("How many symbols would you like?\n"))
# n_in=int(input("How many numbers would you like?\n"))
# letter=[]
# symbol=[]
# number =[]
# for i in range(l_in):
#     op=random.choice(l1)
#     print(op)
#     letter += str(op)
# print(letter)
# for i in range(s_in):
#     op= random.choice(l2)
#     print(op)
#     symbol += str(op)
# for i in range(n_in):
#     op=random.randint(0,9)
#     print(op)
#     number += str(op)
# fl=letter+symbol+number
# print(fl)
# random.shuffle(fl)
# print(fl)
# password=""
# for char in fl:
#     password += char
# print(f"Your password is: {password}")

# # angela's code:
# #Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level
# # password = ""

# # for char in range(1, nr_letters + 1):
# #   password += random.choice(letters)

# # for char in range(1, nr_symbols + 1):
# #   password += random.choice(symbols)

# # for char in range(1, nr_numbers + 1):
# #   password += random.choice(numbers)

# # print(password)

# #Hard Level
# password_list = []

# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")
