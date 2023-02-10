# Ceaser cipher encryption and decryption program script
# The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
# encrypts letters by shifting them over by a 
# certain number of places in the alphabet. We 
# call the length of shift the key. For example, if the 
# key is 3, then A becomes D, B becomes E, C becomes 
# F, and so on. To decrypt the message, you must shift 
# the encrypted letters in the opposite direction. This 
# program lets the user encrypt and decrypt messages 
# according to this algorithm.
user_choice = input("Do you want to (e)ncrypt or (d)ecrypt: ")

key = int(input("Please enter the key (0 to 25) to use: "))

if user_choice == "e":
    text = input("Please enter the message to encrypt: ")
    encrypt_text = ""
    for element in text:
        x = chr(ord(element) + key)
        if x == "$":
            x = " "
        encrypt_text += x
    print(encrypt_text)

elif user_choice == "d":
    text = input("Please enter the message to decrypt: ")
    decrypt_text = ""
    for element in text:
        x = chr(ord(element) - key)
        if x == "$":
            x = " "
        decrypt_text += x
    print(decrypt_text)



