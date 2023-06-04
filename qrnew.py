import qrcode
from PIL import Image
qr = qrcode.QRCode(version=1, box_size=10, error_correction = qrcode.constants.ERROR_CORRECT_H, border= 4,)
qr.add_data(input("Enter the data to be Encoded: "))
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color= 'White')
img.save("git.png")



