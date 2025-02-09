def main():
    min_length = 8

    while True:
        password = get_password()
        if len(password) < min_length:
            break
        print("Password too short!")
    print("*"*len(password))


def get_password():
    password = input('Enter a password: ')
    return password


if __name__ == '__main__':
    main()