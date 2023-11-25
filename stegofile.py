import cv2
import os

def encrypt_message(img, message):
    char_mapping = {}
    
    for i in range(255):
        char_mapping[chr(i)] = i

    n, m, z = 0, 0, 0

    for char in message:
        img[n, m, z] = char_mapping[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    cv2.imwrite("EncryptedMsg.jpg", img)
    os.system("start EncryptedMsg.jpg")

def decrypt_message(img, password):
    char_inverse_mapping = {}
    
    for i in range(255):
        char_inverse_mapping[i] = chr(i)

    message = ""
    n, m, z = 0, 0, 0

    passcode = input("Enter passcode for Decryption: ")

    if password == passcode:
        for i in range(len(message)):
            message += char_inverse_mapping[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3
        print("Decryption message:", message)
    else:
        print("Not a valid key")

# Example usage:
img = cv2.imread("mypic.jpg")
secret_message = input("Enter secret message: ")
password = input("Enter password: ")

encrypt_message(img, secret_message)

# Example decryption (assuming you have the 'img' from the encryption step):
# decrypt_message(img, password)
