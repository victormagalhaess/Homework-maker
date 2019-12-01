import sys
from student import student



def core():
    studentData = student(input("Write your name: "), input("Write your grade (e.g 1st, 2nd..): "), input("Write your teacher's name: "), input("Write your school's name: "))
    theme = input("Write the theme of your homework research: ")

if __name__ == '__main__':
    core()