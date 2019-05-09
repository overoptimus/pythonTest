import pygame
import sys

pygame.init()

size = width, height = 1500, 800
speed = [-8, 4]
bg = (255, 255, 255)

# 创建指定窗口的大小
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption('初次见面，请大家多多关照！')

# 加载图片
# turtle = pygame.image.load('turtle.jpg')
# position = turtle.get_rect()
with open('record.txt', 'w') as f:
    while True:
        for event in pygame.event.get():
            f.write(str(event) + '\n')
            if event.type == pygame.QUIT:
                sys.exit()

    # 移动图像
    # position = position.move(speed)
    #
    # if position.left < 0 or position.right > width:
    #     # 反转图像
    #     turtle = pygame.transform.flip(turtle, True, False)
    #     # 反方向移动
    #     speed[0] = -speed[0]
    #
    # if position.top < 0 or position.bottom > height:
    #     speed[1] = -speed[1]
    #
    # # 填充背景色
    # screen.fill(bg)
    # # 更新图片位置
    # screen.blit(turtle, position)
    # # 更新界面
    # pygame.display.flip()
    # # 延迟10毫秒
    # pygame.time.delay(10)
