import time
def f_username(type):
    while True:
        username = input("\033[94m" + type + " your username: \033[0m")
        if type == "Create" and username in database:
            print("\033[31mUsername already exists.\033[0m")
        else:
            return username
def f_password(type):
    if type == "Create":
        print("Your password must satisfy these conditions:")
        conditions = [
            "   > At least 8 characters long.",
            "   > Contain at least one UPPERCASE character.",
            "   > Contain at least one lowercase character.",
            "   > Contain at least one numerical character.",
            "   > Contain at least one special character."
        ]
        for condition in conditions:
            print("\033[37m" + condition + "\033[0m")
    symbols = set("!@#$%^&*(),.;:?/-_=+`~")
    while True:
        password = input("\033[94m" + type + " your password: \033[0m")
        if type == "Create":
            if (len(password) >= 8 and
                    any(i.isupper() for i in password) and
                    any(i.islower() for i in password) and
                    any(i.isdigit() for i in password) and
                    any(i in symbols for i in password)):
                if password == input("\033[94mConfirm your password: \033[0m"):
                    return password
                else:
                    print("\033[31mPasswords do not match. Please try again.\033[0m")
            else:
                print("\033[37mYour password fails to satisfy the following conditions:\033[0m")
                print("\033[32m" if len(password) >= 8 else "\033[31m",
                      "   > At least 8 characters long.\033[0m", sep='')
                print("\033[32m" if any(i.isupper() for i in password) else "\033[31m",
                      "   > Contain at least one UPPERCASE character.\033[0m", sep='')
                print("\033[32m" if any(i.islower() for i in password) else "\033[31m",
                      "   > Contain at least one lowercase character.\033[0m", sep='')
                print("\033[32m" if any(i.isdigit() for i in password) else "\033[31m",
                      "   > Contain at least one numerical character.\033[0m", sep='')
                print("\033[32m" if any(i in symbols for i in password) else "\033[31m",
                      "   > Contain at least one special character.\033[0m", sep='')
        else:
            return password
database = {'Admin':'Test@123'}
while True:
    time.sleep(2)
    print("\n" * 7)
    print("\n\033[94mOptions\033[0m:")
    print("1. Register")
    print("2. Login")
    print("3. Change Password")
    print("4. Delete Account")
    action = input("\033[94mSelect an option (1-4): \033[0m")
    if action == "1":
        database.update({f_username("Create"): f_password("Create")})
        print("\033[32mAccount has been successfully registered.\033[0m")
    if action == "2":
        username = f_username("Enter")
        password = f_password("Enter")
        if username in database and database[username] == password:
            print("You have successfully logged on as " + username + ".")
            input("Press Enter to logout...")
        else:
            print("\033[31mUsername and/or Password incorrect.\033[0m")
    if action == "3":
        username = f_username("Enter")
        password = f_password("Enter")
        if username in database and database[username] == password:
            print("Verification successful.")
            time.sleep(1)
            database.update({username: f_password("Create")})
        else:
            print("\033[31mUsername and/or Password incorrect.\033[0m")
    if action == "4":
        username = f_username("Enter")
        password = f_password("Enter")
        if username in database and database[username] == password:
            if input("\033[34mDo you want to delete \033[0m" + f"\033[34m{username}\033[0m" + "\033[34m permanently? (\033[32mY\033[34m/\033[31mN\033[34m): \033[0m") == "Y":
                database.__delitem__(username)
            else:
                print("\033[31mOperation cancelled\033[0m")
                break
        else:
            print("\033[31mUsername and/or Password incorrect.\033[0m")