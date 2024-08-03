print("Welcome to the Rollercoster!!")
hight = int(input("Enter your hight in cm: "))
if(hight >= 120):
    print("You can ride the rollercoster!!")
    age=int(input("Enter your age: "))
    tp=0
    bill=0
    if(age<12):
        tp += 5
        print(f"Please pay ${tp}")
    elif(age>=12 and age<18):
        tp += 7
        print(f"Please pay ${tp}")
    else:
        tp += 12
        print(f"Please pay ${tp}")
    wp=input("Want photos? ")
    if(wp=="Y"):
        bill = tp+3
        print(f"Your total bill is ${bill}")
    else:
        print(f"your total bill is ${tp}")
else:
    print("Sorry you have to grow taller before you can ride.")
