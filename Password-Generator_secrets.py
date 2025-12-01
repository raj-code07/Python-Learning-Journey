import secrets
import string

def secure_password(length):
    if length<4:
        return "Password length must be at least 4!"
    
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digit = string.digits
    symbols = string.punctuation

    password = [
        secrets.choice(upper),
        secrets.choice(lower),
        secrets.choice(digit),
        secrets.choice(symbols)
    ]

    Characters = upper + lower + digit + symbols
    password +=[secrets.choice(Characters) for _ in range(length-4)]

    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

print("Secure Password:", secure_password(12))
