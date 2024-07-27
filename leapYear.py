# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
cy = year%100
if(cy==0):
  d= year%400
  if(d==0):
    print("Leap year")
  else:
    print("Not leap year")
elif(cy!=0):
  s=year%4
  if(s==0):
    print("Leap year")
  else:
    print("Not leap year")
