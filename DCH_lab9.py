#this is Duane Huynh's code
def encoder(password):
    encoded_pass=''
    for char in password:
        encoded_pass = encoded_pass+ str((int(char)+3)%10)
    return encoded_pass


def decode(password):
    decoded_password = ''
    for char in password:
        decoded_password += str((int(char) + 7) % 10)
    return decoded_password

if __name__ == '__main__':
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = input("PLease enter an option: ")
        if choice == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!")

        if choice == '2':
            print("The encoded passowrd is", encoded_password, "and the original password is", password )

        if choice == '3':
            break
