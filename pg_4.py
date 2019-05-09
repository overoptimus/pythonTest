import pygame
import sys
from pygame.locals import *

pygame.init()

size = width, height = 1000, 600
speed = [0, 0]
bg = (255, 255, 255)
fullscreen = False

# 创建指定窗口的大小
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption('初次见面，请大家多多关照！')

# 设置放大缩小的比率
ratio = 1.0


# 加载图片
oturtle = pygame.image.load('turtle.jpg')
turtle = oturtle
# 获取图片矩形的位置
oturtle_rect = oturtle.get_rect()
position = turtle_rect = oturtle_rect

l_head = turtle
r_head = turtle = pygame.transform.flip(turtle, True, False)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                oturtle = turtle = l_head
                speed = [-1, 0]
            if event.key == K_RIGHT:
                oturtle = turtle = r_head
                speed = [1, 0]
            if event.key == K_UP:
                speed = [0, -1]
            if event.key == K_DOWN:
                speed = [0, 1]

            # 全屏
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN| pygame.HWSURFACE)
                else:
                    screen = pygame.display.set_mode(size)

            # 放大、缩小小乌龟，空格键恢复原始尺寸
            if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
                # 只能放大一倍，缩小50%
                if event.key == K_EQUALS and ratio < 2:
                    ratio += 0.1
                if event.key == K_MINUS and ratio > 0.5:
                    ratio -= 0.1
                if event.key == K_SPACE:
                    ratio = 1.0

                turtle = pygame.transform.smoothscale(oturtle, (int(oturtle_rect.width * ratio), int(oturtle_rect.height * ratio)))

            # 用户调整窗口尺寸
            if event.type == pygame.VIDEORESIZE:
                size = event.size
                print(size)
                screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    # 移动图像
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        # 反转图像
        turtle = pygame.transform.flip(turtle, True, False)
        # 反方向移动
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    # 填充背景色
    screen.fill(bg)
    # 更新图片位置
    screen.blit(turtle, position)
    # 更新界面
    pygame.display.flip()
    # 延迟10毫秒
    pygame.time.delay(10)
