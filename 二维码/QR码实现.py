import qrcode
import tkinter as tk
from PIL import Image


def create_code():
    content = Entry_input_url.get()
    fill_color = Entry_input_fill_color.get()
    back_color = Entry_input_back_color.get()
    qr = qrcode.QRCode(
        version=2,  # 二维码的边长
        # ERROR_CORRECT_H: 30%的字码可被容错，因为插入了图片，所以增加容错率
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=6,
        border=2,
    )
    qr.make(fit=True)
    qr.add_data(content)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    # 给二维码加图片
    # 把颜色模式转换为RGBA，它表示带透明度掩模的真彩色
    img = img.convert("RGBA")
    # 从文件里加载二维码中心logo图片，用Image函数的open方法
    icon = Image.open("2.png")
    # 得出二维码的宽高
    img_w, img_h = img.size
    factor = 4
    # 通过二维码宽高计算出logo图片宽和高的最大限度
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    # 获取logo的宽和高
    icon_w, icon_h = icon.size
    # 比较logo宽高和最大限度宽高，如果超过最大限度就将logo尺寸调整到最大限度
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h))
    # 根据logo和图片的长宽确定logo的位置
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    icon = icon.convert("RGBA")
    # 将logo图片粘贴到二维码的指定位置
    img.paste(icon, (w, h), icon)

    # 保存二维码
    img.save("qr.png")
    photo = tk.PhotoImage(file="qr.png")
    Label_img = tk.Label(window, image=photo)
    Label_img.place(x=300, y=300)


if __name__ == '__main__':
    window = tk.Tk()
    window.title('二维码生成器')
    window.geometry('900x600')
    label_url = tk.Label(window, text="输入文本：")
    label_url.place(x=50, y=40)

    Entry_input_url = tk.Entry()
    Entry_input_url.place(x=120, y=40)

    label_fill_color = tk.Label(window, text="填充颜色：")
    label_fill_color.place(x=50, y=80)

    Entry_input_fill_color = tk.Entry()
    Entry_input_fill_color.place(x=120, y=80)

    label_fill_color = tk.Label(window, text="背景颜色：")
    label_fill_color.place(x=50, y=120)

    Entry_input_back_color = tk.Entry()
    Entry_input_back_color.place(x=120, y=120)

    button = tk.Button(window, text='开始生成', command=create_code)
    button.place(x=140, y=160)

    window.mainloop()
