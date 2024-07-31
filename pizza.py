print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
S=15
M=20
L=25
a_p_s_y = 2
a_p_ml_y = 3
c_y=1
msg="Thank you for choosing Python Pizza Deliveries! Your final bill is: "
if(size=="S"):
    if(add_pepperoni=="Y"):
      p= int(S)+2
      if(extra_cheese=="Y"):
        pp=p+1
        print(msg+str(pp))
      elif(extra_cheese=="N"):
            pp=p
            print(msg+str(pp))
    elif(add_pepperoni=="N"):
      p=int(S)
      if(extra_cheese=="Y"):        
        pp=p+1
        print(msg+str(pp))
      elif(extra_cheese=="N"):
        pp=p
        print(msg+str(pp))
elif(size=="M"):
   if(add_pepperoni=="Y"):
      p= int(M)+3
      if(extra_cheese=="Y"):
        pp=p+1
        print(msg+str(pp))
      elif(extra_cheese=="N"):
            pp=p
            print(msg+str(pp))
   elif(add_pepperoni=="N"):
      p= int(M)
      if(extra_cheese=="Y"):        
        pp=p+1
        print(msg+str(pp))
      elif(extra_cheese=="N"):
        pp=p
        print(msg+str(pp))
elif(size=="L"):
   if(add_pepperoni=="Y"):
      p= int(L)+3
      if(extra_cheese=="Y"):
        pp=p+1
        print(msg+str(pp))
      elif(extra_cheese=="N"):
            pp=p
            print(msg+str(pp))
   elif(add_pepperoni=="N"):
      p= int(L)
      if(extra_cheese=="Y"):        
        pp=p+1
        print(msg+str(pp))
      elif(extra_cheese=="N"):
        pp=p
        print(msg+str(pp))


    
# print("Thank you for choosing Python Pizza Deliveries!")
# size = input()  # What size pizza do you want? "S", "M", or "L"
# add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
# extra_cheese = input()  # Do you want extra cheese? "Y" or "N"

# # Your code below this line 👇
# bill = 0
# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3

# if extra_cheese == "Y":
#   bill += 1

# print(f"Your final bill is: ${bill}.") 
