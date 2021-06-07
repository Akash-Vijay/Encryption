"""
Project        : Encrpytor.py
Description    : Program to enocode a message
Creator        : Akash Vijay
Date           : 7th June, 2021
Updated        :
""" 


import random # a module to generate random numbers

#Requesting user for the input 
message = input("Enter Your Message :")

#Generating Keys for encryption
key_1 = random.randint(375,475)
key_2 = random.randint(199,299)

#Encrypting the message
encrypted = []
for char in message:
    pre_encoded = ord(char)   # Converts the character into ASCII value
    encoded = pre_encoded + ((key_1 * key_2) - (key_2 + 300) * (75 + key_1))  # Computation on the ASCII value
    encrypted.append(encoded) 

#Generating combined key and output
key = str(key_1) + str(key_2)
print("Your Encrpyted Message is :" +  str(encrypted))
print("Total characters :", len(encrypted))
print("Decryption Key :" + key)