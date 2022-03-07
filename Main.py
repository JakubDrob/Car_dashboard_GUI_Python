import pygame
import time
pygame.init()

win = pygame.display.set_mode((850, 600))
pygame.display.set_caption("Car Dashboard")

bg = pygame.image.load('frame.png')
bar = pygame.image.load('speed_bar.png')
bat = pygame.image.load('battery.png')
ce = pygame.image.load('check_engine.png')
ct = pygame.image.load('coolant_temp.png')
fan = pygame.image.load('fan.png')
fuel = pygame.image.load('fuel.png')
fuel_meter = pygame.image.load('fuel_meter.png')
oil = pygame.image.load('oil.png')
left_sig = pygame.image.load('turn_signal_left.png')
right_sig = pygame.image.load('turn_signal_right.png')
camera_frame = pygame.image.load('camera_frame.jpg')
camera_view = pygame.image.load('camera_view.jpg')
radio = pygame.image.load('radio.png')
blink = pygame.image.load('blink.png')
clock = pygame.time.Clock()

width = 88
height = 19

velocity = 0
global Isrightvisable
Isrightvisable = True
Isrightpressed = False
Isleftpressed = False
global Isleftvisable
Isleftvisable = True
global Timesincelastblink
Timesincelastblink = time.time()
global Timesincelastblink2
Timesincelastblink2 = time.time()


def redrawGameWindow():
    global Isrightvisable
    global Isleftvisable
    global Timesincelastblink
    global Timesincelastblink2
    text = font.render(str(int(velocity)) + ' km/h ', 1, (255, 255, 255))
    win.blit(bg, (0, 0))
    win.blit(fuel_meter, (60, 350))
    win.blit(camera_frame, (400, 250))
    win.blit(camera_view, (405, 255))
    win.blit(radio, (500, 50))
    win.blit(bat, (50, 50))
    win.blit(ce, (120, 50))
    win.blit(ct, (190, 50))
    win.blit(fuel, (260, 50))
    win.blit(oil, (330, 50))
    win.blit(fan, (400, 50))
    win.blit(bar, (200, 250))
    win.blit(text, (208, 220))
    if velocity > 20:
        pygame.draw.rect(win, (0, 255, 0), (212, 500, width, height))
    if velocity > 40:
        pygame.draw.rect(win, (0, 255, 0), (212, 479, width, height))
    if velocity > 60:
        pygame.draw.rect(win, (0, 255, 0), (212, 458, width, height))
    if velocity > 80:
        pygame.draw.rect(win, (255, 255, 0), (212, 437, width, height))
    if velocity > 100:
        pygame.draw.rect(win, (255, 255, 0), (212, 416, width, height))
    if velocity > 120:
        pygame.draw.rect(win, (255, 255, 0), (212, 395, width, height))
    if velocity > 140:
        pygame.draw.rect(win, (255, 100, 10), (212, 374, width, height))
    if velocity > 160:
        pygame.draw.rect(win, (255, 100, 10), (212, 353, width, height))
    if velocity > 180:
        pygame.draw.rect(win, (255, 100, 10), (212, 332, width, height))
    if velocity > 200:
        pygame.draw.rect(win, (255, 0, 0), (212, 311, width, height))
    if velocity > 220:
        pygame.draw.rect(win, (255, 0, 0), (212, 290, width, height))
    if velocity > 240:
        pygame.draw.rect(win, (255, 0, 0), (212, 269, width, height))
    if Isleftvisable:
        win.blit(left_sig, (120, 150))
    else:
        win.blit(blink, (120, 150))
    if Isrightvisable:
        win.blit(right_sig, (330, 150))
    else:
        win.blit(blink, (330, 150))

    if Isleftpressed:
        currenttime = time.time()
        if currenttime - Timesincelastblink > 0.5:
            if Isleftvisable:
                Isleftvisable = False
            else:
                Isleftvisable = True
            Timesincelastblink = time.time()

    if Isrightpressed:
        currenttime2 = time.time()
        if currenttime2 - Timesincelastblink2 > 0.5:
            if Isrightvisable:
                Isrightvisable = False
            else:
                Isrightvisable = True
            Timesincelastblink2 = time.time()

    pygame.display.update()

#mainloop
font = pygame.font.SysFont('comicsans', 30, True)
run = True
while run:
    clock.tick(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        velocity += 1
    if (keys[pygame.K_SPACE] == False and velocity>0):
        if keys[pygame.K_b]:
            velocity -= 1
        else:
            velocity -= 0.3
    if keys[pygame.K_LEFT]:
        if Isleftpressed:
            Isleftpressed = False
            pygame.time.wait(250)
        else:
            Isleftpressed = True
            pygame.time.wait(250)

    if keys[pygame.K_RIGHT]:
        if Isrightpressed:
            Isrightpressed = False
            pygame.time.wait(250)
        else:
            Isrightpressed = True
            pygame.time.wait(250)
    redrawGameWindow()

pygame.quit()