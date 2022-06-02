
def validate_password(passwd):      #validate the password
    symbols = ['$', '@', '#', '%']
    value = True

    if len(passwd) < 6:
        print('length should be at least 6')
        value = False

    if len(passwd) > 16:
        print('length should be not be greater than 16')
        value = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        value = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        value = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        value = False

    if not any(char in symbols for char in passwd):
        print('Password should have at least one of the symbols $#@')
        value = False
    if value:
        return value


# Main method
def main():
    passwd = input("Enter Your Password :\n")

    if (validate_password(passwd)):
        print("Password is valid")
    else:
        print("Invalid Password !!")

if __name__ == '__main__':
    main()