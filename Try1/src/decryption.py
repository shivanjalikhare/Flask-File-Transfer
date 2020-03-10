# -*- coding: utf-8 -*-

import cv2 as cv 
import numpy as np
#import png
import imageio 
import time
from tqdm import tqdm 

start = time.time()

img1 = imageio.imread('EnImg.png')
print('\n\nReading Encrypted Image again:\n\n')
print(img1)

#for g in tqdm(range(100)):
img1= img1.tolist()
print('Decrypting....')
for i1 in tqdm(range(len(img1))):
	for j1 in tqdm(range(len(img1[i1]))):
		x1 = img1[i1][j1] 
		x1 = (pow(x1,16971)%25777)
		img1[i1][j1] = x1

img1 = np.array(img1)#.reshape(184,275)
print('\n\nDecrypted Image:\n\n')
print(img1)
#cv.imshow('DeImage', img1)
cv.imwrite('DeImage.png', img1)

end = time.time()
eTime = end - start

print(eTime)