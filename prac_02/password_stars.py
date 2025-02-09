min_length = 8

while True:
    password = input('Enter a password: ')
    if len(password) < min_length:
        break
    print("Password too short!")
print("*"*len(password))