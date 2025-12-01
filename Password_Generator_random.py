import random
import string

def generate_password(length):
    if length<4:
        return "Password length must be at least 4!"
    
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digit = string.digits
    symbols = string.punctuation

    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digit),
        random.choice(symbols)
    ]

    all_chars = upper + lower + digit + symbols
    password +=random.choices(all_chars,k=length-4)

    # random.shuffle(password)
    return ''.join(password)

print("Generated Password :",generate_password(3))