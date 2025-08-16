'''Library management system'''

class library:
    def __init__(self):
        self.no_of_books=0
        self.list =[]

    def add(self):
        self.book_name=input("Enter the name of book:")
        self.no_of_books+=1
        self.list.append(self.book_name)

    def display(self):
        if self.no_of_books==0:
            print("Library is empty")
        else:
            print("Books Availabe in Library:")
            for name in self.list:
                print(name)
        

l1=library()

while True:
    choice=int(input("Choose the option:\n1.Add books\n2.Book counts\n3.Display\n4.Exit\n"))
    if choice==4:
        print("Thank you for using library")
        break
    match choice:
        case 1:
            l1.add()
        case 2:
            print("Number of books:",l1.no_of_books)
        case 3:
            l1.display()
        case 4:
            False
