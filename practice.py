#! /usr/bin/python3.6

# Practice of string methods

# .upper, .lower, .title, .capitalize,
# .islower, .isupper, .index, .strip,
# .count, .format,

name = "Chris Humphrey"
#print(name)
#print(name.upper())
#print(name.lower())
#print(name.capitalize())

user_name = input("What's your name? ")
location = input("Where do you live? ")
kids = input("How many kids do you have? ")
string = "Your name is {} and you live in {}. You have {} kids."
print(string.format(user_name, location, kids))



#print(user_name)
#print(len(user_name))
