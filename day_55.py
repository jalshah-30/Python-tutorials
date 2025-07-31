#Snake Water Gun game

import random

# computer=   1   2   3
#player=    1 D   W   L
#           2 L   D   W
#           3 W   L   D

computer=[1,2,3]
player=[1,2,3]
x= random.choice(computer)


print("Choose option from below:\n1.Snake\n2.Water\n3.Gun\n")

try:
    y=int(input("Choose the option:"))
except ValueError:
    print("Put integer value only.")

if(y==x):
    print("Draw\n")
else:
    if((y==1 and x==2)or(y==2 and x==3) or(y==3 and x==1)):
        print("You Won")
    else:
        print("You Lose")

print("The computer chose:",x)