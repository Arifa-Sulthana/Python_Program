two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
print("The entered number is: "+two_digit_number)
print(type(two_digit_number))
num_len =len(two_digit_number)
temp =0
for char in range (num_len):
    f=int(two_digit_number[char])
    temp = temp+f
print("the sum of digits from entered number is: "+str(temp))
