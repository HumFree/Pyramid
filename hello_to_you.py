#! /usr/bin/python3.6

name = input("What's your name? ")
school = input("What school do you go to? ")
grade = input("What grade are you in? ")

string = "Please to meet you {}.\nI've learned a lot about you.\nLike, You go to {} and your in the {} grade."
output = string.format(name, school, grade)

print(output)
