import random
import string
import os
print('Do you want:\n a: create a passord \n b: generate a random password \n')
option = input('What do you choice?:\n').lower()

def password_generator(password):
    caracteres = string.ascii_letters + string.digits
    password_typed = ''.join(random.choices(caracteres, k=password))
    return password_typed


while True:
    if option == 'a':
        password = input('Typed your password: \n')
        if len(password) != 8:
            os.system('cls')
            print('Typed a password with 8 or less characters.')
        elif len(password) == 8:
            print('Your password:', password)
            break

    elif option == 'b':
        password_generate = password_generator(8)
        print('Your new password:',password_generate)
        break
        
    elif option != 'a' and 'b':
        os.system('cls')
        print('Invalid value!')
        print('Do you want:\n a: create a passord \n b: generate a random password \n')
        option = input('What do you choice?:\n').lower()
        
