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
    chunk_size = 470
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



#im_unen = [cv2.imread(file) for file in glob.glob(r"C:\Users\c00221719\Documents\GitHub\Flask-File-Transfer\Try1\src\crypto\*.png")]
im_unen = (r"C:\Users\c00221719\Documents\GitHub\Flask-File-Transfer\Try1\src\crypto\images_unencrypted\*.png")
with open(im_unen,"rb") as file:
    unencrypted_blob_whole = file.read()
    encrypted_blob_whole = encrypt_blob(unencrypted_blob_whole, public_key)
    
    
    
im_en = cv2.imread(r'\crypto\images_encrypted')
with open(im_en, "wb") as file:
    cv2.imwrite(encrypted_blob_whole)
    



end = time.time()
eTime = end - start

print(eTime)