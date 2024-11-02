import string
import random

def password_gen(choice):
    def weak_password():
        password = random.choice(.readlines)

    def medium_password():
        password = "ez"

    def strong_password(char_number):
        password = ""
        char_number = int(input("Enter length of password: "))
        for i in range(1, char_number+1):
            letter = str(random.choice(string.ascii_letters))
            digit = str(random.choice(string.digits))
            special = str(random.choice(string.punctuation))
            list = [letter,  digit, special]
            password += ''.join(random.choice(list))
        print("Password = "+password)
        strong_password(char_number)


if __name__ == '__main__':
    print("Welcome to strong password generator!")
    choice = int(input("Choose strength of your password:\n1 - weak\n2 - medium\n3 - password"))
    if choice == 1:
        weak_password()
    elif choice == 2:

    elif choice == 3:
        strong

