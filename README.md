# QRcode-Creater-with-UI

这是一个二维码生成器
基于PyQt5与qrcode的二维码生成器的实现
## 1.二维码的现实意义：
    二维码作为一种全新的信息存储、传递和识别技术，自诞生之日起就得到了世界上许多国家的关注。美国、德国、日本等国家，不仅已将二维码技术应用于公安、外交、军事等部门对各类证件的管理，而且也将二维码应用于海关、税务等部门对各类报表和票据的管理，商业、交通运输等部门对商品及货物运输的管理、邮政部门对邮政包裹的管理、工业生产领域对工业生产线的自动化管理。
二维码在商业、交通运输、邮政、工业生产等领域的应用，极大地提高了信息传递的效率和准确性，同时也提升了生产效率和管理效率。
此外，二维码还被广泛应用于移动支付、电子票务、身份识别等领域。例如，通过扫描二维码，消费者可以快速完成支付，避免了传统支付方式需要携带现金或银行卡的不便；电子票务系统通过二维码技术实现了电子化的票据管理，使得用户可以更加方便地管理和使用票据；身份识别领域中，二维码技术也得到了广泛应用，如健康码等。
因此，二维码在现实生活中的意义在于它提供了一种快速、高效、准确的信息传递方式和管理方式，为我们的生活带来了便利和效率。

## 2.课程要求：
二维码生成器的主要功能包括： 
（1）能输入要生成二维码的信息， 
（2）能选择内嵌图片， 
（3）能依据上述信息生成二维码，
（4）能将二维码保存为png格式图片。 
（5）基于上面所设计实现的二维码生成器，设计一套我校校园场所码的编码方案，依据场所码编码方案，在二维码生成工具中输入一个场所的名称，简介等，并选择相应内嵌图像 便可以生成该场所的场所二维码。并用微信扫描解析，测试其正确性

## 3.整个项目的逻辑结构实现：
### 3.1项目的整体架构
1. 首先要有欢迎界面，要有背景图，音乐（气氛组）
2. 再要有主要逻辑界面，实现如下目标
1. 要实现可以生成二维码（其内容可以通过内容设计）
2. 要实现在二维码中插入图片（输入图片路径即可）
3. 显示二维码，并保存为png文件。

### 3.2 项目的实现
#### 3.2.1. 使用PyQt5设计界面：
主要要实现两个界面，一个是欢迎界面，主要逻辑是显示一张欢迎图片，并提供一个按钮，点击按钮进入主要逻辑界面。
图 1 欢迎界面UI设计
欢迎界面：（hello.ui）
设计Qwidge类对象Qmainwindow的stylesheet属性为background-image: url(:/newPrefix/20230928101625.png)；实现背景图片
设计一个Bottom类，其text属性为“二维码生成器启动”。
保存UI文件并通过命令行将UI文件转换为py文件以供主程序调用 
图2 主程序UI设计
 主程序界面：（vs.ui）
#### 3.2.2各界面的逻辑结构：
##### 3.2.2.1 Hello.ui逻辑实现
首先使用pygame包播放欢迎音乐：
pygame.mixer.init()
track = pygame.mixer.music.load("./1.mp3")
pygame.mixer.music.play()
然后点击按钮“二维码生成器启动”音乐播放器暂停，然后关闭当前欢迎窗口：
实现代码如下：
首先将Hello.ui界面中的pushbottom对象与Hello_UI类的infer函数相连接
self.pushButton.clicked.connect(self.infer)
infer函数定义如下：
def infer(self):
        self.MainUi = Main_UI()# 对于主界面的实例化对象
        print("原神启动") 
        self.MainUi.show()# 展现主界面
        self.close() # 关闭当前界面
        pygame.mixer.music.stop() # 停止音乐播放
##### 3.2.2.2 vs.ui 逻辑实现
首先将MainUI类中的pushButtom组件（开始推理按钮）与自身的inference函数连接
self.pushButton.clicked.connect(self.inferrence)
然后利用inference函数进行推理：
def inferrence(self):
    img_path = self.textEdit.toPlainText()
    fill_color = self.textEdit_2.toPlainText()
    back_color = self.textEdit_3.toPlainText()
    content = self.textEdit_4.toPlainText()
这里首先通过各个textEdit类的toPlainText（）函数获得用户在页面中的输入。
然后对于这些属性值缺省的处理
if back_color == "":
    back_color = "white"
if fill_color == "":
    fill_color="black"
if img_path == "":
    img_path = "./22.png"
if content == "":
    content="library"
然后通过create_code函数输入各个属性值产生二维码，并保存在当前目录下的qr.png文件中，然后通过Label对象的setPixmap的方法将二维码图像保存。
create_code(content=content,fill_color=fill_color,back_color=back_color,center_img=img_path)
self.label_9.setPixmap(QtGui.QPixmap("./qr.png"))
#### 3.2.3 二维码生成逻辑实现
主要逻辑如下：
1.	通过内容，二维码颜色，以及二维码填充颜色生成二维码。
2.	其次通过二维码的宽度长度，将所要插入的图片进行尺寸的缩放。
3.	最后通过img.paste方法将插入图片粘贴在二维码中。
函数定义如下：
def create_code(content="library",fill_color="black",back_color
="white",center_img="./22.png"):
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
    // 给二维码加图片
    // 把颜色模式转换为RGBA，它表示带透明度掩模的真彩色
    img = img.convert("RGBA")
    // 从文件里加载二维码中心logo图片，用Image函数的open方法
    icon = Image.open(center_img)
    // 得出二维码的宽高
    img_w, img_h = img.size
    factor = 4
    // 通过二维码宽高计算出logo图片宽和高的最大限度
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    // 获取logo的宽和高
    icon_w, icon_h = icon.size
    // 比较logo宽高和最大限度宽高，如果超过最大限度就将logo尺寸调整到最大限度
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h))
    // 根据logo和图片的长宽确定logo的位置
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    icon = icon.convert("RGBA")
    // 将logo图片粘贴到二维码的指定位置
    img.paste(icon, (w, h), icon)

    // 保存二维码
    img.save("qr.png")
    return img

### 3.3 项目展现
欢迎界面：
 
点击“二维码生成器启动”按钮生成如下界面：
 
输入特征：
1.	插入图片路径为“./22.png”
2.	二维码颜色为“red”
3.	二维码填充颜色为“blue”
4.	所要生成内容为“library”
点击“开始生成”按钮，图片展现如下：
 
手机扫描结果如下：
 
