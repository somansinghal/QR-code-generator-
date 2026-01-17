import qrcode

url = input("Enter the URL: ").strip()
file_path = "user\downloads\qrcode_generator\\qrcode.png"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print(f"QR code generated and saved to {file_path}")
qr.make(fit=True)