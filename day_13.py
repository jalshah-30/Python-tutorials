#string methods

name = "!!-jal-!!"

print(len(name))
print(name.upper())  #all letters become capital
print(name.lower()) #all letters become small
print(name.rstrip("!")) #removes exclaimatory mark only right
# print(name.rstrip("@")) 

print(name.replace("jal","Jal")) #replaces no matter where and how much
print(name.split("-")) #makes list

feelings="i Like jal"
print(feelings.capitalize()) #Capitalises the first letter of the string

str1 = "Welcome to Jal's coding challenge!!"
print(len(str1))
print(str1.center(50)) #leaves the space 
print(len(str1.center(50)))

print(name.count("i"))     #counts the number of times a letter or name is used
print(name.endswith("i"))
print(name.endswith("!!")) #Checks whether it ends with the given or not

love="Hitanshi"
print(love.endswith("n",1,5))
print(love.find("i"))  #finds the first occured letter and gives output as index
# print(love.index("j"))
print(love.isalnum())  #a-z,A-Z,0-9
print(love.isalpha()) #a-z,A-Z
print(love.islower()) #a-z
print(love.isprintable()) #checks if string is printable
print(love.isspace())
print(love.isprintable())
print(love.istitle()) #Every word of string starts with capital letter
print(love.isupper()) #A-Z
print(love.startswith("H"))
print(love.swapcase()) #capital changes into small and vice versa

movie= "Ramayana: the good vs evil"
print(movie.title())
