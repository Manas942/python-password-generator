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


def check_pass_strength(passkey) :
    has_special_char = False
    pass_length = len(passkey)

    if pass_length >= 8:
        for i in passkey:
            if i in string.punctuation:
                has_special_char = True
                break
                
            else:
                has_special_char = False
        

    else:
        for j in passkey:
            if j in string.punctuation:
                has_special_char = True
                break
            else:
                has_special_char = False

    if len(passkey) >= 8:
        if has_special_char == True:
            print("very strong password")
        else:
            print("good password")
    else:
        if has_special_char == True:
            print("meduium password")
        else:
            print("weak password")

check_pass_strength(passkey=password)
