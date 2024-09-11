import string
import random

length = int(input("Enter password length: "))

print('''Choose character set for password from these:
1. Digits
2. Letters
3. Special characters
4. Exit''')

characterList = ""
while True:
    choice = int(input("Pick a number: "))
    if choice == 1:
        characterList += string.digits
    elif choice == 2:
        characterList += string.ascii_letters
    elif choice == 3:
        characterList += string.punctuation
    elif choice == 4:
        if not characterList:
            print("No character sets selected. Exiting.")
            break
        else:
            break
    else:
        print("Invalid option, please choose again.")

if characterList:
    password = ''.join(random.choice(characterList) for _ in range(length))
    print("The random password is: " + password)
else:
    print("No characters selected for password generation.")
