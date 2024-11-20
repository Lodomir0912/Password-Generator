# Password-Generator
This is a simple Python-based password generator that offers three levels of password strength: weak, medium, and strong. The generator uses a mix of randomization techniques and allows you to choose the length and complexity of the generated passwords.

## Features
Weak Password: Randomly selects a common password from a list of frequently used passwords.\n
Medium Password: Builds a password from a common word (from the list) and modifies it by replacing certain characters with special characters (e.g., a -> @, o -> 0, etc.), and appends a random digit and special character.\n
Strong Password: Generates a secure password of your desired length by combining random letters, digits, and optionally, special characters.
## Requirements
A text file containing the 1000 most common passwords (1000-most-common-passwords.txt). The file should be located in the resource directory.
## Usage
Clone this repository to your local machine.
Ensure you have the required text file (1000-most-common-passwords.txt) in the resource folder.
## Run the script:
```bash
python password-generator.py
```
Choose the strength of the password:\n
1 for weak\n
2 for medium\n
3 for strong\n
If you choose a strong password, specify the length and whether you want special characters included.
# Example Output
```python
Welcome to password generator!
----------------------------------
Choose strength of your password:
1 - weak
2 - medium
3 - strong
----------------------------------
Enter your choice [1/2/3] : 3
Enter length of your password: 12
Use special characters? [Y/n] : y
Password: aA8$zV|4iG7#
```
