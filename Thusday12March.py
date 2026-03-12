#Code here
# Created by Grant Samson
#Creating a python program that stimulates logging into a system. Set the defualt username and password to:
#username = "admin"
#password = "admin@2026"

username = "admin"
password = "admin@2026"

user=input("Input your username ")
passw=input("input your password ")

invalid=("password is incorrect")
incorrect=("username is incorrect")

if username == user and password == passw:
    print("You have successfully logged in")
elif ( username != user and password != passw):
    print(invalid)
    print(incorrect)
elif (username == user and password != passw):
    print(incorrect)
else:
    print(invalid)
