from pyzbar.pyzbar import decode
from PIL import Image
code = decode(Image.open("QR.png"))
print(code[0].data.decode())
