"""
Project        : Decrpytor.py
Description    : Program to decode a message, encrypted using 'Encryptor'
Creator        : Akash Vijay
Date           : 7th June, 2021
Updated        :
""" 

#Requesting for inputs
characters = int(input("Enter the number of characters :"))
key = int(input("Enter the Decryption key :"))

#Resolving the key into actual keys
key_1 , key_2 = key // 1000 , key % 1000

#Storing the encrypted segments in a list
encrypted = []
char = 0
for char in range(characters):        #Stores the Encrypted segments into a list
    encrypted_val = int(input("Enter the segment: "))
    encrypted.append(encrypted_val)

#Decrypting
decrypted = ''
for char in encrypted:
    decoded = char - ((key_1 * key_2) - (key_2 + 300) * (75 + key_1))  # Reverse Computing to obtain ASCII value
    message_segment = chr(decoded)    # Converting ASCII value to string
    decrypted += str(message_segment)

#Generating the output
print("The message is : " + decrypted)
