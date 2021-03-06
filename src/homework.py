import sys
import json
from student import student
from search import search
from images import images
from msword import msword

def askCredentials():
    with open('../credentials/algorithmia.json', 'r') as algorithmiaCredentialsFile:
        credentials = json.load(algorithmiaCredentialsFile)
    if(not credentials['apiKey']):
        credentials['apiKey'] = input("Write your Algorithmia key: ")
        with open('../credentials/algorithmia.json', 'w') as algorithmiaCredentialsFile:
            json.dump(credentials, algorithmiaCredentialsFile)
        

def core():
    studentData = student(input("Write your name: "), input("Write your grade (e.g 1st, 2nd..): "), input("Write your teacher's name: "), input("Write your school's name: "))
    language = input("Write the language code of your research: (supported codes: en (english), pt(portuguese)): ")
    theme = input("Write the theme of your homework research: ")
    searchData = search(theme, language)
    images(theme)
    msword(studentData.getHeader(), theme, searchData['content'].split('\n'), '../downloads')
    print('Your homework is done!!!')


if __name__ == '__main__':
    askCredentials()
    core()