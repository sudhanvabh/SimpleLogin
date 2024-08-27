import csv
import string
import time

BL = '\033[94m'
WH = '\033[97m'
GR = '\033[92m'
RD = '\033[91m'
RS = '\033[0m'


def check_file():
    try:
        with open('database.csv', 'r'):
            pass
    except:
        header = ['username', 'password']
        with open('database.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)


def f_username(type):
    while True:
        username = input(f"{BL}{type} your username: {RS}")
        with open('database.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            exists = False
            for row in reader:
                if row[0] == username:
                    exists = True
            if type == "Create" and exists:
                print(f"{RD}    > Username already exists{RS}")
            else:
                return username


def f_password(type):
    if type == "Create":
        print(f"{WH}Your password must satisfy these conditions:{RS}")
        conditions = [
            "   > At least 8 characters long.",
            "   > Contain at least one UPPERCASE character.",
            "   > Contain at least one lowercase character.",
            "   > Contain at least one numerical character.",
            "   > Contain at least one special character."
        ]
        for condition in conditions:
            print(f"{WH}{condition}{RS}")
    while True:
        password = input(f"{BL}{type} your password: {RS}")
        if type == "Create":
            if (len(password) >= 8 and
                    any(i.isupper() for i in password) and
                    any(i.islower() for i in password) and
                    any(i.isdigit() for i in password) and
                    any(i in string.punctuation for i in password)):
                if password == input(f"{BL}Confirm your password: {RS}"):
                    return password
                else:
                    print(f"{RD}Passwords do not match. Please try again.{RS}")
            else:
                print(f"{WH}Your password fails to satisfy the following conditions:{RS}")
                print(f"{GR}" if len(password) >= 8 else f"{RD}",
                      "   > At least 8 characters long.{RS}", sep='')
                print(f"{GR}" if any(i.isupper() for i in password) else f"{RD}",
                      "   > Contain at least one UPPERCASE character.{RS}", sep='')
                print(f"{GR}" if any(i.islower() for i in password) else f"{RD}",
                      "   > Contain at least one lowercase character.{RS}", sep='')
                print(f"{GR}" if any(i.isdigit() for i in password) else f"{RD}",
                      "   > Contain at least one numerical character.{RS}", sep='')
                print(f"{GR}" if any(i in string.punctuation for i in password) else f"{RD}",
                      "   > Contain at least one special character.{RS}", sep='')
        else:
            return password


def check_password():
    username = f_username('Enter')
    password = f_password('Enter')
    with open('database.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        if any(row[0] == username and row[1] == password for row in reader):
            print(f'{GR}Login Successful. Welcome {username}{RS}')
            return(username,password,1)
        else:
            print(f'{RD}Incorrect username or password.{RS}')
            time.sleep(2)
            return(1,1,0)

def action_menu():
    print("\n" * 7)
    print(f"\n{BL}Options:{RS}")
    print("1. Register")
    print("2. Login")
    print("3. Change Password")
    while True:
        action = input(f"{BL}Select an option (1-3): {RS}")
        if action in ('123'):
            return action
        else:
            print(f'{RD}Choice invalid. Please type 1, 2 or 3.{RS}')


def text_editor(username):
    filename = f'{username}.txt'

    while True:
        print(f"Opening {username}.txt")
        time.sleep(.5)
        print(f"{BL}Options :{RS}")
        print("  1. Read file")
        print("  2. Append text")
        print("  3. Overwrite file")
        print("  4. Exit")
        action = input(f"{BL}Select an option (1-4): {RS}")

        if action == "1":
            with open(filename, 'r') as file:
                content = file.read()
                print(f"\nCurrent content of {filename}:\n")
                print(content)
                input(f"{BL}Press ENTER to exit{RS}")

        elif action == "2":
            with open(filename, 'a') as file:
                print(f"\nEnter your text below. Type {BL}'SAVE'{RS} on a new line to save and exit.")
                while True:
                    line = input()
                    if line.upper() == 'SAVE':
                        break
                    file.write(line + '\n')
            print(f"{GR}\nText has been appended to {BL}{filename}{RS}.")

        elif action == "3":
            with open(filename, 'w') as file:
                print(f"\nEnter your text below to overwrite {filename}. Type 'SAVE' on a new line to save and exit.")
                file.write(f"{username}'s document\n")
                file.write("==============================\n")
                while True:
                    line = input()
                    if line.upper() == 'SAVE':
                        break
                    file.write(line + '\n')
            print(f"\n{filename} has been overwritten successfully.")

        elif action == "4":
            print("Exiting the text editor.")
            break

        else:
            print("Invalid option. Please select a valid option.")

check_file()

while True:
    action = action_menu()

    if action == "1":
        with open('database.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([f_username("Create"), f_password("Create")])
        print(f"{GR}Account has been successfully registered.{RS}")
        time.sleep(2)

    if action == "2":
        (username, password, status) = check_password()
        if status == 1:
            try:
                with open(f'{username}.txt', 'r'):
                    pass
            except:
                with open(f"{username}.txt", "w") as file:
                    file.write(f"{username}'s document\n")
                    file.write("==============================\n")
            text_editor(username)
        else:
            pass
    if action == "3":
        (username, old_password, dummy) = check_password()
        print('To change the password, please follow the following steps:')
        time.sleep(1)
        new_password = f_password('Create')

        with open('database.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        for row in rows:
            if row[0] == username:
                row[1] = new_password

        with open('database.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print(f"{GR}Password successfully updated for {BL}{username}{GR}.{RS}")
        time.sleep(2)
