# QR Code Generator using Python.....
# Watch Out ...!!
# 31st March 2023


import qrcode

# img = qrcode.make('https://adewuyiportfolio.netlify.app')
inp = input("Enter your link, or anything to be converted to QRCode: ")
img = qrcode.make(inp)
sav = input("Enter the desired filename you want for you QR Code: ")
sav = f"{sav}.PNG"
img.save(sav)

import shutil

current_loc = f'{sav}'
# print(current_loc)
new_loc = 'C:\\Users\\OWNER\\Documents\\QRCodeResults\\' + current_loc
print(f"Your file has been saved here: {new_loc}")
shutil.copy(current_loc, new_loc)
