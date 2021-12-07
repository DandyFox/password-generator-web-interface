import eel
import random

eel.init('web')

@eel.expose
def pass_gen(number,length):
    if number == '' or length == '': 
        return "Ok, Throw me some numbers… O U T W I T H I T ! ! !"
    elif number == '0' or length == '0':
        return "Zero? Try again"
    else:   
        y = 0
        passwords = ''
        chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        for n in range(int(number)):
            password = ''
            for i in range(int(length)):
                password += random.choice(chars)
            y += 1    
            passwords += (password + " ")
        return passwords

eel.start('main.html', size=(600,650))
    