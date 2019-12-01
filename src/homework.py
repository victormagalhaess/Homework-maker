import sys
from student import student
from search import search

def core():
    studentData = student(input("Write your name: "), input("Write your grade (e.g 1st, 2nd..): "), input("Write your teacher's name: "), input("Write your school's name: "))
    language = input("Write the language code of your research: (supported codes: en (english, pt(portuguese)): ")
    theme = input("Write the theme of your homework research: ")
    searchData = search(theme, language)
    themeTags = textProcessing(searchData)
    images = imagesDownload(themeTags)
    generateLatex(studentData, theme, searchData, images)

if __name__ == '__main__':
    core()