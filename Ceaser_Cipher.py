# Ceaser cipher script
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



