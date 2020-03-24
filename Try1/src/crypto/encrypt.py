from Crypto.PublicKey import RSA
import time
from Crypto.Cipher import PKCS1_OAEP
import zlib
import base64
import glob
import cv2
import sys


start = time.time()
#Our Encryption Function
def encrypt_blob(blob, public_key):
    #Import the Public Key and use for encryption using PKCS1_OAEP
    rsa_key = RSA.importKey(public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    #compress the data first
    blob = zlib.compress(blob)
    #In determining the chunk size, determine the private key length used in bytes
    #and subtract 42 bytes (when using PKCS1_OAEP). The data will be in encrypted
    #in chunks
    chunk_size = 86
    offset = 0
    end_loop = False
    encrypted = bytearray()

    while not end_loop:
        #The chunk
        chunk = blob[offset:offset + chunk_size]

        #If the data chunk is less then the chunk size, then we need to add
        #padding with " ". This indicates the we reached the end of the file
        #so we end loop here
        if len(chunk) % chunk_size != 0:
            end_loop = True
            #chunk += b" " * (chunk_size - len(chunk))
            chunk += bytes(chunk_size - len(chunk))
        #Append the encrypted chunk to the overall encrypted file
        encrypted += rsa_key.encrypt(chunk)

        #Increase the offset by chunk size
        offset += chunk_size

    #Base 64 encode the encrypted file
    return base64.b64encode(encrypted)

#Use the public key for encryption
fd = open("public_key.pem", "rb")
public_key = fd.read()
fd.close()

#Our candidate file to be encrypted  
fd = open("image1.jpeg", "rb")
unencrypted_blob = fd.read()
fd.close()

encrypted_blob = encrypt_blob(unencrypted_blob, public_key)

#Write the encrypted contents to a file
fd = open("encrypted_img.jpg", "wb")
fd.write(encrypted_blob)
fd.close()




path = "./images_unencrypted/"
path_2 = "./images_encrypted/"

import os

dirs = os.listdir(path)
for item in dirs:
    if os.path.isfile(path+item):
        fd = open(path+item, 'rb')
        unencrypted_blob = fd.read()
        fd.close
        encrypted_blob = encrypt_blob(unencrypted_blob, public_key)
        f, e = os.path.splitext(path_2+item)
        print(f)
        fd_2 = open(f+'.jpg' ,"wb")
        fd_2.write(encrypted_blob)
        fd_2.close
        


    
    
    
end = time.time()
eTime = end - start

print(eTime)