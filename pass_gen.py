import random 
import hashlib
import string

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'

password = ''

sha256 = hashlib.sha256

number_of_chars = int(input("how long password do you want(4-16): "))

if number_of_chars >=4 and number_of_chars <=16:
    for i in range(0,number_of_chars):

        num = random.randint(0,len(characters)-1)

        password += characters[num]
    print(f"password is : {password}")
    hashed_password = sha256(password.encode()).hexdigest()
    print(f"hashed password is : {hashed_password}")
else:
    print("not correct number of digits specified")


def check_pass_strength(password) :
    pass_length = len(password)

    if pass_length >= 8:
        for i in password:
            if i in string.punctuation:
                print("Strong Password")
            else:
                print("medium password")
    else:
        print("weak password")


