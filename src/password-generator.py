import string
import random
import os

file_path = os.path.join("..", "resource", "1000-most-common-passwords.txt")


def password_gen(choice):
    def weak_password():
        with open(file_path, "r") as file:
            lines = file.readlines()
            password = random.choice(lines).strip()
        print("Password: " + password)

    def medium_password():
        digit = str(random.choice(string.digits))
        special = str(random.choice(string.punctuation))
        with open(file_path, 'r') as file:
            lines = file.readlines()
            password = random.choice(lines).strip()
        print("Password: " + password.join([digit, special]))

    def strong_password():
        try:
            char_number = int(input("Enter length of your password: "))
            if char_number < 4:
                print("Password should be at least 4 letters long for better security.")
                return
        except ValueError:
            print("Invalid option! Please enter a correct number.")
        password = ""
        char_special = input("Use special characters? [Y/n] : ")
        if char_special =='Y':
            for i in range(1, char_number + 1):
                letter = str(random.choice(string.ascii_letters))
                digit = str(random.choice(string.digits))
                special = str(random.choice(string.punctuation))
                chars = [letter, digit, special]
                password += ''.join(random.choice(chars))
            print("Password = " + password)
        elif char_special == 'n':
            for i in range(1, char_number + 1):
                letter = str(random.choice(string.ascii_letters))
                digit = str(random.choice(string.digits))
                chars = [letter, digit]
                password += ''.join(random.choice(chars))
            print("Password = " + password)
        else:
            raise ValueError

    if choice == 1:
        weak_password()
    elif choice == 2:
        medium_password()
    elif choice == 3:
        strong_password()
    else:
        print("Invalid option!")


if __name__ == '__main__':
    print("Welcome to password generator!")
    try:
        choice = int(input("Choose strength of your password:\n1 - weak\n2 - medium\n3 - password\n"))
        password_gen(choice)
    except ValueError:
        print("Invalid option! Please enter a correct input.")
