#match case statements

print("Your gender is:\n1.Male\n2.Female\n3.Another\n4.Not interested\n")
x=int(input("Choose the option:"))

match x:
    case 1:
        print("You are men")
    case 2:
        print("You are women")
    case 3:
        print("You are different")
    case 4:
        print("No worries")
    case _:
        print("Please choose from the option")