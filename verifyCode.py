def verifyCode():
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), random.randrange(20, 100))
    width = 100
    height = 50
    # 创建画面对象
    im = Image.new('RGB', (width, height), color=bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point（）函数绘制噪点
    for i in range(0, stop=4, step=1):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, stop=4, step=1):
        rand_str += str[random.randrange(0, len(str))]
    # 构造字体对象
    font = ImageFont.truetype(font=r'C:\Windows\Fonts\Bahnschrift', size=40)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    draw.text((5, 2), rand_str[0], fill=fontcolor, font=font)
    draw.text((25, 2), rand_str[1], fill=fontcolor, font=font)
    draw.text((50, 2), rand_str[2], fill=fontcolor, font=font)
    draw.text((75, 2), rand_str[3], fill=fontcolor, font=font)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    # request.session['verifycode'] = rand_str
    # 内存文件操作
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')
