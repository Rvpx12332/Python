saved_password = "12345"
saved_username = "user5"

username = input("Enter your username: ")
password = input("Enter you password: ")

if username == saved_username :
    if password == saved_password:
        print("Signed in. Welcome!")
    else:
        print("Wrong password.")
else:
    print("Wrong username.")            