# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.
# print(names)
# 🚨 Remember to remove the print statement above when you submit.
# names =input()
import random
name=input()
names =name.split(", ")
print(names)
l=len(names)-1
r_n = random.randint(0,l)
print(r_n)
eo=names[r_n]
print(f"{eo} is going to buy the meal today!")
