print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
c=0;c1 = 0
total=0
t=0; r =0; u=0; e=0; l=0; o=0; v=0; f=0
t1=0
t2=0
n = name1+name2
print(n)
name=list(n)
print(name)

if "t" or "T" in name:
    t=name.count("t")+name.count("T")
if "r" or "R" in name:
    r=name.count("r")+name.count("R")
if "u" or "U" in name:
    u=name.count("u")+name.count("U")
if "e" or "E" in name:
    e=name.count("e")+name.count("E")
t1 = t+r+u+e 
print(f"the 1st total is {t1}")
if "l" or "L" in name:
    l=name.count("l")+name.count("L")
if "o" or "O" in name:
    o=name.count("o")+name.count("O")
if "v" or "V" in name:
    v=name.count("v")+name.count("V")
if "e" or "E" in name:
    f=name.count("e")+name.count("E")
t2 = l+o+v+f 
print(f"the 2nd total is {t2}")
Love_Score = int(str(t1)+str(t2))
print(f"Your score {Love_Score}")
if(Love_Score<10 or Love_Score>90):
    print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif(Love_Score>=40 and Love_Score<=50):
    print(f"Your score is {Love_Score}, you are alright together.")
else:
    print(f"Your score is {Love_Score}.")


# Angela's solution:print("The Love Calculator is calculating your score...")
# name1 = input()  # What is your name?
# name2 = input()  # What is their name?
# # Your code below this line 👇
# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e

# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))
# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")
