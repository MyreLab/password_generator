#importing modules
import string as s
import secrets

#creating password function
def generate_password(length: int, symbols: bool, uppercase: bool):

    #combination of lowercase letters and numbers
    combination = s.ascii_lowercase + s.digits

    #use punctuation string for symbols
    if symbols:
        combination += s.punctuation

    #use uppercase string for uppercase characters
    if uppercase:
        combination += s.ascii_uppercase

    combination_length = len(combination)

    #blank string will be populated by new password
    new_password = ""

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password

#Printing password
#Change length, symbols, and uppercase as needed
#Enumerate function creates 5 different passwords in a list form
for _, index in enumerate(range(5)):
    password = generate_password(length=15, symbols=True, uppercase=True)
    print(index + 1, ":", password)
