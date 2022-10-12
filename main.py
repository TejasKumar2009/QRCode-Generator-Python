import qrcode
import os

userinp = input("Enter text & generate qr code image : ")
img = qrcode.make(userinp)

index = 1
while True:
   filename1 = f"MyQR({index}).png"
   if filename1 not in os.listdir():
      img.save(filename1)
      break
   index += 1
