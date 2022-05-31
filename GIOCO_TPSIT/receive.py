import numpy as np
import sys
import serial, time
import pygame as pg
import threading, queue
import time


width = 1200
height = 800
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
muro1 = pg.image.load(".\muro1.png")
muro2 = pg.image.load(".\muro2.png")
muro3 = pg.image.load(".\muro3.png")
muro4 = pg.image.load(".\muro3.png")
muro5 = pg.image.load(".\muro3.png")
muro6 = pg.image.load(".\muro3.png")
muro7 = pg.image.load(".\muro3.png")
muro8 = pg.image.load(".\muro3.png")
muro9 = pg.image.load(".\muro3.png")
muro10 = pg.image.load(".\muro3.png")
muro11 = pg.image.load(".\muro3.png")
muro12 = pg.image.load(".\muro4.png")
muro13 = pg.image.load(".\muro5.png")
muro14 = pg.image.load(".\muro5.png")
muro15 = pg.image.load(".\muro5.png")
muro16 = pg.image.load(".\muro6.png")
muro17 = pg.image.load(".\muro6.png")
muro18 = pg.image.load(".\muro6.png")
muro19 = pg.image.load(".\muro7.png")
muro20 = pg.image.load(".\muro8.png")
muro21 = pg.image.load(".\muro9.png")
muro22 = pg.image.load(".\muro10.png")
muro23 = pg.image.load(".\muro11.png")
muro24 = pg.image.load(".\muro11.png")
muro25 = pg.image.load(".\muro2.png")
muro26 = pg.image.load(".\muro12.png")
muro27 = pg.image.load(".\muro13.png")
muro28 = pg.image.load(".\muro14.png")
muro29 = pg.image.load(".\muro15.png")
muro30 = pg.image.load(".\muro16.png")
muro31 = pg.image.load(".\muro17.png")
muro32 = pg.image.load(".\muro18.png")
muro33= pg.image.load(".\muro19.png")
muro34 = pg.image.load(".\muro20.png")
nero = pg.image.load(".\snero.jpg")
ball = pg.image.load(".\pallina.png")
buco = pg.image.load(".\pbuco.png")
muro1vis = screen.blit(muro1,(0,110))
muro2vis = screen.blit(muro2,(373,0))
muro3vis = screen.blit(muro3,(230,82))
muro4vis = screen.blit(muro4,(133,170))
muro5vis = screen.blit(muro5,(100,466))
muro6vis = screen.blit(muro6,(247,514))
muro7vis = screen.blit(muro7,(385,180))
muro8vis = screen.blit(muro8,(400,440))
muro9vis = screen.blit(muro9,(655,150))
muro10vis = screen.blit(muro10,(655,310))
muro11vis = screen.blit(muro11,(665,500))
muro12vis = screen.blit(muro12,(0,343))
muro13vis = screen.blit(muro13,(112,706))
muro14vis = screen.blit(muro14,(496,262))
muro15vis = screen.blit(muro15,(736,655))
muro16vis = screen.blit(muro16,(350,730))
muro17vis = screen.blit(muro17,(660,730))
muro18vis = screen.blit(muro18,(850,730))
muro19vis = screen.blit(muro19,(274,298))
muro20vis = screen.blit(muro20,(196,415))
muro21vis = screen.blit(muro21,(523,358))
muro22vis = screen.blit(muro22,(775,400))
muro23vis = screen.blit(muro23,(760,377))
muro24vis = screen.blit(muro24,(770,157))
muro25vis = screen.blit(muro25,(508,100))
muro26vis = screen.blit(muro26,(508,77))
muro27vis = screen.blit(muro27,(886,0))
muro28vis = screen.blit(muro28,(745,247))
muro29vis = screen.blit(muro29,(909,415))
muro30vis = screen.blit(muro30,(1033,664))
muro31vis = screen.blit(muro31,(1056,712))
muro32vis = screen.blit(muro32,(1033,553))
muro33vis = screen.blit(muro33,(1066,136))
muro34vis = screen.blit(muro34,(994,187))
muro1rect = muro1.get_rect()
muro2rect = muro2.get_rect()
muro3rect = muro3.get_rect()
muro4rect = muro4.get_rect()
muro5rect = muro5.get_rect()
muro6rect = muro6.get_rect()
muro7rect = muro7.get_rect()
muro8rect = muro8.get_rect()
muro9rect = muro9.get_rect()
muro10rect = muro10.get_rect()
muro11rect = muro11.get_rect()
muro12rect = muro12.get_rect()
muro13rect = muro13.get_rect()
muro14rect = muro14.get_rect()
muro15rect = muro15.get_rect()
muro16rect = muro16.get_rect()
muro17rect = muro17.get_rect()
muro18rect = muro18.get_rect()
muro19rect = muro19.get_rect()
muro20rect = muro20.get_rect()
muro21rect = muro21.get_rect()
muro22rect = muro22.get_rect()
muro23rect = muro23.get_rect()
muro24rect = muro24.get_rect()
muro25rect = muro25.get_rect()
muro26rect = muro26.get_rect()
muro27rect = muro27.get_rect()
muro28rect = muro28.get_rect()
muro29rect = muro29.get_rect()
muro30rect = muro30.get_rect()
muro31rect = muro31.get_rect()
muro32rect = muro32.get_rect()
muro33rect = muro33.get_rect()
muro34rect = muro34.get_rect()
ballrect = ball.get_rect()
bucorect = buco.get_rect()
ballrect.centerx = 1150
ballrect.centery = 50

black = 0, 0, 0
dt = 1
gamma = 0.05
q = queue.Queue()

class Read_Microbit(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._running = True
      
    def terminate(self):
        self._running = False
        
    def run(self):
        #serial config
        port = "COM8"
        s = serial.Serial(port)
        s.baudrate = 115200
        while self._running:
            data = s.readline().decode() 
            acc = [float(x) for x in data[1:-3].split(",")]
            q.put(acc)
            time.sleep(0.01)

running = True
rm = Read_Microbit()
rm.start()
pg.init()
speed = [0, 0]
while running:
    acc = q.get()
    speed[0] = (1.-gamma)*speed[0] + dt*acc[0]/1024.
    speed[1] = (1.-gamma)*speed[1] + dt*acc[1]/1024.
    q.task_done()
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    if ballrect.collidepoint(muro1rect.x, muro1rect.y):
        speed[1] = -speed[1]
    if ballrect.collidepoint(muro2rect.x, muro2rect.y):
        speed[1] = -speed[1]
    if ballrect.collidepoint(muro3rect.x, muro3rect.y):
        speed[1] = -speed[1]
    if ballrect.collidepoint(muro4rect.x, muro4rect.y):
        speed[1] = -speed[1]
    if ballrect.collidepoint(muro5rect.x, muro5rect.y):
        speed[1] = -speed[1]
    if ballrect.collidepoint(muro6rect.x, muro6rect.y):
        speed[1] = -speed[1]
    if ballrect.collidepoint(muro7rect.x, muro7rect.y):
        speed[1] = -speed[1]
    if ballrect.collidepoint(muro8rect.x, muro8rect.y):
        speed[1] = -speed[1]
    if ballrect.collidepoint(muro9rect.x, muro9rect.y):
        speed[1] = -speed[1]
    if ballrect.collidepoint(muro10rect.x, muro10rect.y):
        speed[1] = -speed[1]
    if ballrect.collidepoint(muro11rect.x, muro11rect.y):
        speed[1] = -speed[1]
    if ballrect.collidepoint(muro12rect.x, muro12rect.y):
        speed[1] = -speed[1]
    screen.blit(nero, (0,0))
    screen.blit(muro1, muro1vis)
    screen.blit(muro2, muro2vis)
    screen.blit(muro3, muro3vis)
    screen.blit(muro4, muro4vis)
    screen.blit(muro5, muro5vis)
    screen.blit(muro6, muro6vis)
    screen.blit(muro7, muro7vis)
    screen.blit(muro8, muro8vis)
    screen.blit(muro9, muro9vis)
    screen.blit(muro10, muro10vis)
    screen.blit(muro11, muro11vis)
    screen.blit(muro12, muro12vis)
    screen.blit(muro13, muro13vis)
    screen.blit(muro14, muro14vis)
    screen.blit(muro15, muro15vis)
    screen.blit(muro16, muro16vis)
    screen.blit(muro17, muro17vis)
    screen.blit(muro18, muro18vis)
    screen.blit(muro19, muro19vis)
    screen.blit(muro20, muro20vis)
    screen.blit(muro21, muro21vis)
    screen.blit(muro22, muro22vis)
    screen.blit(muro23, muro23vis)
    screen.blit(muro24, muro24vis)
    screen.blit(muro25, muro25vis)
    screen.blit(muro26, muro26vis)
    screen.blit(muro27, muro27vis)
    screen.blit(muro28, muro28vis)
    screen.blit(ball, ballrect)
    screen.blit(buco, (10,10))
    pg.display.flip()
    clock.tick(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
    
rm.terminate()
rm.join()
