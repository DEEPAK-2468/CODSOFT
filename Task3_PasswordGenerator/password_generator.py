import string as s
import random as r

choice="y"
while (choice=="y"):
    try:
        length=int(input("\nEnter length of the Password: "))
        if (length<=0):
            print("Password length must be greater than 0.")
            continue
        characters=(s.ascii_letters+s.digits+s.punctuation)
        password=""
        for i in range(length):
            password+=r.choice(characters)
        print(f"Generated Password: {password}")
        choice=input("\nGenerate another Password (y/n): ").lower()
    except ValueError:
        print("Enter a Valid number.")