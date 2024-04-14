import argparse
import qrcode
import time

def generate_qr(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    timestamp = int(time.time())
    filename = f"qrcode_{timestamp}.png"
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code generated for the entered URL. Saved as {filename}")

def main():
    parser = argparse.ArgumentParser(description="Generate a QR code for a URL.")
    parser.add_argument("url", type=str, help="The URL to encode in the QR code.")

    args = parser.parse_args()
    generate_qr(args.url)

if __name__ == "__main__":
    main()
