target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total=0
for r in range(0, target+1):
  if(r%2==0):
    total+=r
print (total)

# # angela's code:
# even_sum = 0
# # range(starting number, range ends number, increment by 2)
# for number in range(2, target + 1, 2):
#   even_sum += number
# print(even_sum)
