import random 
import hashlib
import string

class colors :
    red = "\033[31m"
    orange = "\033[38;5;208m"
    yellow = "\033[33m"
    green = "\033[32m"
    reset = "\033[0m"




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
            print(colors.green + "very strong password" + colors.reset)
        else:
            print(colors.orange + "good password" + colors.reset)
    else:
        if has_special_char == True:
            print(colors.yellow + "meduium password" + colors.reset)
        else:
            print(colors.red +"weak password" + colors.reset)

check_pass_strength(passkey=password)


f = open("password.txt", "w")
f.write(password)
f.close()
