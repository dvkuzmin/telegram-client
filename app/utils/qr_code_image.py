import qrcode


def display_url_as_qr(url: str):
    """Отрисовка QR кода"""
    qr = qrcode.QRCode()

    qr.add_data(url)
    qr.make()
    img = qr.make_image(fill='black', back_color='white')
    img = img.convert("RGB")
    img.show()
