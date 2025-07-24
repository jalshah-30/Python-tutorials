#if else condition statements

age = int(input("Enter your age:"))
print("Your age is ",age)

if(age>=18):
    print("You can drive the car")
    if(age>=70):
        print("You have to give back driving test")
    elif(age<70 and age>=40):
        print("Your age is between 40-70")
    else:
        print("You are young enough")
else:
    print("You cannot drive the car\nWait for your 18th birthday")