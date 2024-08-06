import sys
from turtle import down
import pygame as pg
import numpy as np

pg.init()

a = 0
WIDTH = 700
ROWS = 1030
REGULARWIDTH = 5

screen = pg.display.set_mode((ROWS,WIDTH))
pg.display.set_caption("그림판 2D")
screen.fill((0,0,0))
pg.display.flip()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.display.quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            a = 1
        if event.type == pg.MOUSEBUTTONUP:
            a = 0
    if a == 1:
        inpos = pg.mouse.get_pos()
        pg.draw.line(screen,(255,255,255),inpos,inpos,REGULARWIDTH)
        pg.display.flip()