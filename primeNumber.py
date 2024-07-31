# Write your code below this line 👇
def prime_checker(number):
  if number > 1:
   # check for factors
   for i in range(2,number):
       if (number % i) == 0:
           print(number,"is not a prime number.")
        #    print(i,"times",number//i,"is",number)
           break
   else:
       print(number,"is a prime number.")
       
#If the input number is less than or equal to 1, then it is not prime
  else:
   print(number,"is not a prime number.")

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)


# Angela's code:
# def prime_checker(number):
#   is_prime = True
#   for i in range(2, number):
#     if number % i == 0:
#       is_prime = False
#   if is_prime:
#     print("It's a prime number.")
#   else:
#     print("It's not a prime number.")
    
# # Your code above this line 👆
# n = int(input()) # Check this number
# prime_checker(number=n)
