import string
import random

def password_gen(char_number):
    password = ""
    for i in range(1, char_number+1):
        letter = str(random.choice(string.ascii_letters))
        digit = str(random.choice(string.digits))
        special = str(random.choice(string.punctuation))
        list = [letter,  digit, special]
        password += ''.join(random.choice(list))
    print("Password = "+password)


if __name__ == '__main__':
    print("Welcome to strong password generator!")
    char_number = int(input("Enter length of password: "))
    password_gen(char_number)