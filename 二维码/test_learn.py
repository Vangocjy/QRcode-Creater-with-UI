import qrcode

def mk_qr(txt,dst):
    img = qrcode.make(txt)
    img.save(dst)

mk_qr("Fucking crazy Thursday!","test.png")
