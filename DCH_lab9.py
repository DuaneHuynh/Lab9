#this is Duane Huynh's code
def encoder(password):
    encoded_pass=''
    for char in password:
        encoded_pass = encoded_pass+ str(int(char)+3)%10
    return encoded_pass


def decode(password):
    decoded_password = ''
    for char in password:
        decoded_password += str((int(char) + 7) % 10)
    return decoded_password
