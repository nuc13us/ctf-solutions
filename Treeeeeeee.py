# riceteacatpanda CTF

import os
import Image
# from tesseract import image_to_string
import pytesseract
import hashlib

count = 0
for root, dirs, files in os.walk('bigtree'):
        for fname in files:
            path = os.path.join(root, fname)
            if '.jpg' in path:
                # print path
                # print pytesseract.image_to_string(Image.open(path),lang='eng')
                md5 =  hashlib.md5(open(path,'rb').read()).hexdigest()
                if(md5 == '49390dd9695e7ab7c49fbea6697bc1a9' or md5 == '2d7b81239b77deb7fbda026d9521939b'):
                    continue
                print path
                count = count + 1


print count
