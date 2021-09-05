def main():
    """Create dictionary of emails and names"""
    emails_dict = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        user_confirmation = input("Is your name {}? (Y/n) ".format(name))
        if user_confirmation.upper() != "Y" and user_confirmation != "":
            name = input("Name: ")
        emails_dict[email] = name
        email = input("Email: ")

    for email, name in emails_dict.items():
        print("{} ({})".format(name, email))


def get_name(email):
    """Get name from email"""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
