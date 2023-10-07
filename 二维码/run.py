import qrcode
import tkinter as tk
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
import Ui
import sys
import hello
import time
import pygame

def create_code(content="library",fill_color="black",back_color="white",center_img="./22.png"):
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
    icon = Image.open(center_img)
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
    return img

class Main_UI(QtWidgets.QMainWindow, Ui.Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)  # 创建主界面对象
        Ui.Ui_MainWindow.__init__(self)  # 主界面对象初始化
        self.setupUi(self)  # 配置主界面对象
        self.pushButton.clicked.connect(self.inferrence)

    def inferrence(self):
        img_path = self.textEdit.toPlainText()
        fill_color = self.textEdit_2.toPlainText()
        back_color = self.textEdit_3.toPlainText()
        content = self.textEdit_4.toPlainText()
        if back_color == "":
            back_color = "white"
        if fill_color == "":
            fill_color="black"
        if img_path == "":
            img_path = "./22.png"
        if content == "":
            content="library"
        img = create_code(content=content,fill_color=fill_color,back_color=back_color,center_img=img_path)
        self.label_9.setPixmap(QtGui.QPixmap("./qr.png"))

class Hello_UI(QtWidgets.QMainWindow,hello.Ui_MainWindow):
    def __init__(self):
        pygame.mixer.init()
        track = pygame.mixer.music.load("./1.mp3")
        pygame.mixer.music.play()
        QtWidgets.QMainWindow.__init__(self)  # 创建主界面对象
        hello.Ui_MainWindow.__init__(self)  # 主界面对象初始化
        self.setupUi(self)  # 配置主界面对象
        self.pushButton.clicked.connect(self.infer)

    def infer(self):
        self.MainUi = Main_UI()
        print("原神启动")
        self.MainUi.show()
        self.close()
        pygame.mixer.music.stop()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    #MAIN_window = Main_UI()  # 创建主菜单的窗口对象
    Hello_UI = Hello_UI()
    Hello_UI.show()  # 显示主菜单  # 保持显示
    sys.exit(app.exec_())  # 保持显示
