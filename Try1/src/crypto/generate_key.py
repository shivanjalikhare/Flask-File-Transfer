# -*- coding: utf-8 -*-

#ch9_generate_keys.py
from Crypto.PublicKey import RSA
import time




start = time.time()
#Generate a public/ private key pair using 4096 bits key length (512 bytes)
new_key = RSA.generate(1024, e=65537)

#The private key in PEM format
private_key = new_key.exportKey("PEM")

#The public key in PEM Format
public_key = new_key.publickey().exportKey("PEM")

print (private_key)
fd = open("private_key.pem", "wb")
fd.write(private_key)
fd.close()

print (public_key)
fd = open("public_key.pem", "wb")
fd.write(public_key)
fd.close()

end = time.time()
eTime = end - start

print(eTime)