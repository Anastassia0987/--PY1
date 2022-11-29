import random
def get_random_password() -> str:
    symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password = random.sample(symbols, k = 8)
    return password

print(get_random_password())
