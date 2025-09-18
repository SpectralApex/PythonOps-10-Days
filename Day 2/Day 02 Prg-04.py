# 4. Simple Login System with User Creation

create_username = input("Create a username: ")
create_password = input("Create a password: ")

username = input("Enter username: ")
password = input("Enter password: ")

if username == create_username and password == create_password:
    print("Login Successful")
else:
    print("Invalid Credentials")