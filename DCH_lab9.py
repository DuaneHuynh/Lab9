#this is Duane Huynh's code
def encoder(password):
    encoded_pass=''
    for char in password:
        encoded_pass = encoded_pass+ str(int(char)+3)%10
    return encoded_pass

def decoder(password):
    decoded_pass = ''
    for char in password:
        decoded_pass = decoded_pass + str((int(char)-3)%10)
    return decoded_pass