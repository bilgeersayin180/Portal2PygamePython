import pygame
import random as portal_pos
pygame.init()
window_x = 600
window_y = 400
wall_x = 0
wall_y = 0
character_x = window_x / 2
character_y = window_y / 2
speed = 3
speed_wall = 30 
run = True
h = 120
w = 100
mouse_x_for_bluePortal = 0
mouse_y_for_bluePortal = 700
mouse_x_for_yellowPortal = 0
mouse_y_for_yellowPortal = 700
class portal:
    def __init__(self,file_location,portal_x,portal_y):
        self.file_location = file_location
        self.portal_x = portal_x
        self.portal_y = portal_y
    def setup(self):
        Portal = pygame.image.load(self.file_location)
        portal_img = pygame.transform.scale(Portal, (w, h))
        window.blit(portal_img, (self.portal_x,self.portal_y))

portalBlue = portal('portalYellow (2).png', mouse_x_for_bluePortal, mouse_y_for_bluePortal)
portalYellow = portal('portalYellow (1).png', mouse_x_for_yellowPortal, mouse_y_for_yellowPortal)
window = pygame.display.set_mode((window_x,window_y))
pygame.display.set_caption("Portal 2")
portalWallpaper = pygame.image.load('wallpaper2.png.jpg')
characterAtlas = pygame.image.load('pBody.png')
Atlas = pygame.transform.scale(characterAtlas, (w, h))
def wallPaper_Right():
    window.blit(portalWallpaper ,(wall_x,wall_y))
    window.blit(portalWallpaper ,(wall_x + window_x, wall_y))
    window.blit(Atlas ,(character_x, character_y))
def wallPaper_Left():
    window.blit(portalWallpaper ,(wall_x,wall_y))
    window.blit(portalWallpaper ,(wall_x - window_x, wall_y))
    window.blit(Atlas ,(character_x, character_y))
def distanceCalc(x1,y1,x2,y2):
    D = (((x1 - x2)**2) + ((y1 - y2)**2))
    return D
while (run):
    pygame.time.delay(35)
    for get_event in pygame.event.get():
        if get_event.type == pygame.QUIT:
            run = False
        if get_event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x_for_bluePortal, mouse_y_for_bluePortal = pygame.mouse.get_pos()
            mouse_x_for_yellowPortal, mouse_y_for_yellowPortal = portal_pos.uniform(w,window_x - w),portal_pos.uniform(h,window_y - h)#pygame.mouse.get_pos()
            portalBlue = portal('portalYellow (2).png', mouse_x_for_bluePortal, mouse_y_for_bluePortal)
            portalYellow = portal('portalYellow (1).png', mouse_x_for_yellowPortal, mouse_y_for_yellowPortal)
    keys = pygame.key.get_pressed()
    wallPaper_Right()
    portalBlue.setup()
    portalYellow.setup()
    if (keys[pygame.K_d] and character_x < (window_x - w - speed)): #right
        wall_x -= speed_wall
        character_x += speed
        mouse_x_for_bluePortal -= speed
        mouse_x_for_yellowPortal -= speed
        portalBlue = portal('portalYellow (2).png', mouse_x_for_bluePortal, mouse_y_for_bluePortal)
        portalYellow = portal('portalYellow (1).png', mouse_x_for_yellowPortal, mouse_y_for_yellowPortal)
        portalBlue.setup()
        portalYellow.setup()
    if (keys[pygame.K_a] and character_x > speed): #left
        wallPaper_Left()        
        wall_x += speed_wall
        character_x -= speed
        mouse_x_for_bluePortal += speed
        mouse_x_for_yellowPortal += speed
        portalBlue = portal('portalYellow (2).png', mouse_x_for_bluePortal, mouse_y_for_bluePortal)
        portalYellow = portal('portalYellow (1).png', mouse_x_for_yellowPortal, mouse_y_for_yellowPortal)
        portalBlue.setup()
        portalYellow.setup()
        if (wall_x == window_x):
            wall_x = 0
    if (keys[pygame.K_w] and character_y > speed): #up
        character_y -= speed
    if (keys[pygame.K_s] and character_y < (window_y - h - speed)): #down
        character_y += speed
    if (wall_x == (-1 * window_x)):
        wall_x = 0
    if (distanceCalc(character_x,character_y,mouse_x_for_bluePortal,mouse_y_for_bluePortal) <= 650):
        character_x = mouse_x_for_yellowPortal
        character_y = mouse_y_for_yellowPortal
    if (distanceCalc(character_x,character_y,mouse_x_for_yellowPortal,mouse_y_for_yellowPortal) <= 650):
        character_x = mouse_x_for_bluePortal + w
        character_y = mouse_y_for_bluePortal + h
    pygame.display.update() 
pygame.quit()

