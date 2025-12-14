import random 

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'

password = ''

number_of_chars = int(input("how long password do you want(4-16): "))

if number_of_chars >=4 and number_of_chars <=16:
    for i in range(0,number_of_chars):

        num = random.randint(0,len(characters)-1)

        password += characters[num]

print(password)

