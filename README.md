# Encryption
Simple python scripts to encrypt and decrypt messages.


------ This repository holds simple python scripts to encrypt and decrypt a message ------

# ENCRYPTING - using Encryptor.py
    
   * Any message inputted will be first converted to its ASCII values.
   * Computation will be then done on the ASCII values using a mathematical function.
   * This will generate segments of random numbers representing each character of the message.
   * This can be used as the encrypted form.
   * The key used for encrypting will be generated along with the encrypted from.
   
#  DECRYPTING - using Decryptor.py
   
   * The Decryption key, Total number of characters and the encrypted segments can be provided into the script.
   * The script will then reverse compute each segment using the key to obtain respective ASCII values.
   * These ASCII values will be then converted back to string.
   * The string will be then generated.
