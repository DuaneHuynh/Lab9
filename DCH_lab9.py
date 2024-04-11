def decoder:
    decoded_pass = ''
    for char in password:
        decoded_pass = decoded_pass + str((int(char)-3)%10)
    return decoded_pass