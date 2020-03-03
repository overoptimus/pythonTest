import pygame
import sys

pygame.init()

size = width, height = 600, 400
speed = [-8, 4]
bg = (0, 0, 0)

font = pygame.font.Font(None, 20)

# 创建指定窗口的大小
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption('Optimus Demo')
screen.fill(bg)

position = 0
line_height = font.get_linesize()

# 加载图片
# turtle = pygame.image.load('turtle.jpg')
# position = turtle.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        screen.blit(font.render(str(event), True, (0, 255, 0)), (0, position))
        position += line_height

        if position > height:
            position = 0
            screen.fill(bg)

    pygame.display.flip()
