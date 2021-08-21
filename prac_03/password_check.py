MIN_LENGTH = 10


def main():
    """Gets password then prints * equal to length of password"""
    password = get_password(MIN_LENGTH)
    print_asterisks(password)
    main()


def print_asterisks(password):
    """Prints * equal to length of password"""
    print("*" * len(password))


def get_password():
    """Gets a password with a minimum length of MIN_LENGTH"""
    password = input("Password: ")
    while len(password) < MIN_LENGTH:
        print("Invalid length.")
        password = input("Password: ")
    return password
