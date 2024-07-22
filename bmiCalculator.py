# 1st input: enter height in meters e.g: 1.65
height = input("enter you hight: ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("enter you weight: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

h = float(height)
w = int(weight)
bmi_cal = w/(h**2)

print(int(bmi_cal))
