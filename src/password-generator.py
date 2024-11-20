import string
import random
import os

file_path = os.path.join("..", "resource", "1000-most-common-passwords.txt")


def read_password():
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            return random.choice(lines).strip()
    except FileNotFoundError:
        print(f"Error: file {file_path} has not been found.")
        return None


def password_gen(choice):
    def weak_password():
        password = read_password()
        print("Password: " + password)

    def medium_password():
        digit = random.choice(string.digits)
        special = random.choice(string.punctuation)
        swap = {
            'a': '@',
            'o': '0',
            'i': '|',
            'e': '3',
            's': '$',
            't': '7',
            '8': '&',
            'h': '#'
        }
        password = read_password()
        password = ''.join(swap.get(sign, sign) for sign in password.lower())
        print("Password: " + password + digit + special)

    def strong_password(char_number):
        password = ""
        while True:
            char_special = input("Use special characters? [Y/n] : ").lower()
            if char_special == 'y':
                for i in range(1, char_number + 1):
                    letter = random.choice(string.ascii_letters)
                    digit = random.choice(string.digits)
                    special = random.choice(string.punctuation)
                    chars = [letter, digit, special]
                    password += ''.join(random.choice(chars))
                print("Password: " + password)
                break
            elif char_special == 'n':
                for i in range(1, char_number + 1):
                    letter = random.choice(string.ascii_letters)
                    digit = random.choice(string.digits)
                    chars = [letter, digit]
                    password += ''.join(random.choice(chars))
                print("Password: " + password)
                break
            else:
                print("Invalid input! Please choose 'Y' or 'n'.")

    if choice == 1:
        weak_password()
    elif choice == 2:
        medium_password()
    elif choice == 3:
        try:
            char_number = int(input("Enter length of your password: "))
            if char_number < 4:
                print("Password should be at least 4 letters long for better security.")
            elif char_number >= 4:
                strong_password(char_number)
        except ValueError:
            print("Invalid option! Please enter a correct number.")
    else:
        print("Invalid option!")


if __name__ == '__main__':
    print("Welcome to password generator!")
    print("----------------------------------")
    print("Choose strength of your password:\n1 - weak\n2 - medium\n3 - password")
    print("----------------------------------")
    try:
        choice = int(input("Enter your choice [1/2/3] : "))
        password_gen(choice)
    except ValueError:
        print("Invalid option! Please enter a correct input.")
