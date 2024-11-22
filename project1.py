while True:
    act_username="NK"
    act_password="NK345"
    username=input("Enter the username:")
    password=input("Enter the password:")
    if (username==act_username) and (password==act_password):
        print("Logged in successfully")
        break
    else:
        print("Invalid credentials.PLEASE TRY AGAIN")