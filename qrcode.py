import pyqrcode 
from pyqrcode import QRCode 
  
s = input("Please type your message: " )
dosya_adi = input("Please type your file name: ") + ".svg"

url = pyqrcode.create(s)

url.svg(dosya_adi , scale = 8)