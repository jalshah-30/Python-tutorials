'''Local and global variable'''

x=19

print(f"Global Variable {x}")
def love():
    global x
    x=20
    print(f"The local variable {x}")

love()
print(f"Global Variable {x}")