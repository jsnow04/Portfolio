import pygame as pg
import random
from colors import *
import math
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"imgs")
player_imgs = os.path.join(img_folder,"playerimgs")
sound_folder = os.path.join(game_folder,"snds")
textdata_folder = os.path.join(game_folder,"textdata")

class NPC(pg.sprite.Sprite):
     def __init__(self):
         super(NPC, self).__init__()
         self.image = pg.Surface((15,15))
         self.image.fill(WHITE)
         self.rect = self.image.get_rect()
         self.rect.center = (WIDTH/2,HEIGHT/2)
         #self.rect.center = (-25,-25)
         self.speedx = 5
         self.speedy = 5

         self.center_x = self.rect.centerx
         self.center_y = self.rect.centery
         #angle in radius
         self.angle = 1
         #far away from the center
         self.radius = 50
         #orbit speed
         self.speed = .1


     def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        #if self.rect.centerx > WIDTH:
        #     self.rect.left = 0
        # if self.rect.centerx < 0:
        #      self.rect.right = WIDTH
        # if self.rect.centery > HEIGHT:
        #      self.rect.top = 0
        # if self.rect.centery < 0:
        #       self.rect.bottom = HEIGHT

        #weird directions
        # if self.rect.left > WIDTH:
        #       self.rect.top = HEIGHT
        #       self.rect.centerx = WIDTH/2
        #       self.speedx = 0
        #       self.speedy = 5
        # if self.rect.bottom < 0:
        #     print(self.rect.right)
        #     self.rect.right = 0
        #     self.rect.centery = HEIGHT / 2
        #     self.speedx = 5
        #     self.speedy = 0

        #square movement
        # if self.rect.right == WIDTH:
        #     self.speedx=0
        #     self.speedy = -5
        # if self.rect.top == 0:
        #     self.speedx = -5
        #     self.speedy = 0
        # if self.rect.left == 0:
        #     self.speedx = 0
        #     self.speedy = 5
        # if self.rect.bottom == HEIGHT and self.rect.right != WIDTH:
        #     self.speedx = 5
        #     self.speedy = 0

        #start outside diaganol
        # if self.rect.centerx >= WIDTH/2:
        #    self.speedx = 5
        #    self.speedy = -5
        # if self.rect.bottomleft[0] > WIDTH and self.rect.bottomleft[1] <= 0:
        #     self.rect.bottomright = (0,0)
        #     self.speedx = 5
        #     self.speedy = 5

        #circle movement
        # if self.angle <= 6.25:
        #     self.rect.centerx = self.radius * math.sin(self.angle) + self.center_x
        #     self.rect.centery = self.radius * math.cos(self.angle) + self.center_y
        #     self.angle += self.speed

        #perfect hit
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.speedx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speedy *=-1

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # self.image = pg.Surface((50, 50))
        # self.image.fill(BLACK)
        self.image = player_imgs
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        # self.rect.center = (-25,-25)
        self.speedx = 0
        self.speedy = 0
        self.keypressed = False


    def toggle_pressed(self):
        self.keypressed = False


    def update(self):

        #mouse movement
        if mouse_btn_held:
            self.rect.center = (mousex,mousey)
        #self.rect.centerx = (mousex)
        #self.rect.centery = (mousey)

        #grid movement
        # keystate = pg.key.get_pressed()
        # if keystate[pg.K_LEFT] and self.keypressed == False:
        #     self.keypressed = True
        #     self.rect.centerx += -50
        # if keystate[pg.K_RIGHT] and self.keypressed == False:
        #     self.keypressed = True
        #     self.rect.centerx += 50
        # if keystate[pg.K_UP] and self.keypressed == False:
        #     self.keypressed = True
        #     self.rect.centery += -50
        # if keystate[pg.K_DOWN] and self.keypressed == False:
        #     self.keypressed = True
        #     self.rect.centery += 50

        #basic movement
        # self.speedx = 0
        # self.speedy = 0
        # keystate = pg.key.get_pressed()
        # if keystate[pg.K_LEFT]:
        #     self.speedx += -5
        # if keystate[pg.K_RIGHT]:
        #     self.speedx += 5
        # if keystate[pg.K_UP]:
        #     self.speedy = -5
        # if keystate[pg.K_DOWN]:
        #     self.speedy = 5
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        #bind to screen
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT











def spawn_player(x,y):
    newplayer = Player()
    newplayer.rect.center = (x,y)
    newplayer.speedx = random.randint(-10,10)
    newplayer.speedy = random.randint(-10,10)
    all_Sprites.add(newplayer)
    players_group.add(newplayer)



WIDTH = 360
HEIGHT = 480
FPS = 30
title = "Template"


# colors (r,g,b)
# BLACK = (0,0,0)
# WHITE = (255,255,255)
# RED = (255,0,0)
# GREEN = (0,255,0)
# BLUE = (0,0,255)
# YELLOW = (255,255,0)
# BROWN = (133, 79, 44)
# ORANGE = (255, 98, 0)
# PURPLE = (255, 0, 255)
# PINK = (255, 0, 93)
mouse_btn_held = False



pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()
#player images
player_imgs = pg.image.load(os.path.join(player_imgs,"pac.png")).convert()



# create sprite groups
all_Sprites = pg.sprite.Group()
players_group = pg.sprite.Group()
npc_group = pg.sprite.Group()

#create game objects
npc = NPC()
player = Player()


#add objects to sprite groups
all_Sprites.add(player,npc)
players_group.add(player)
npc_group.add(npc)

# Game loop
running = True
while running:
     clock.tick(FPS)
    # process input
     mousex,mousey = pg.mouse.get_pos()
     for event in pg.event.get():
         if event.type == pg.KEYUP:
             if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                 player.toggle_pressed()
             if event.key == pg.K_UP or event.key == pg.K_DOWN:
                 player.toggle_pressed()
         if event.type == pg.MOUSEBUTTONDOWN and player.rect.collidepoint(pg.mouse.get_pos()):
             x = pg.mouse.get_pressed()
             if x[0]:
                 print("clicked left")
                 mouse_btn_held = True
             if x[1]:
                 print("clicked middle")
             if x[2]:
                 spawn_player(mousex,mousey)
                 print("clicked right")
         if event.type == pg.MOUSEBUTTONUP and mouse_btn_held == True:
                 print("released left")
                 mouse_btn_held = False



           # if event.type == pg.KEYDOWN:
           #     if event.key == pg.K_RIGHT:
           #         player.speedx = 5
           #     if event.key == pg.K_LEFT:
           #         player.speedx = -5
           #     if event.key == pg.K_UP:
           #             player.speedy = -5
           #     if event.key == pg.K_DOWN:
           #         player.speedy = 5




           #      #basic movement
              # if event.key == pg.K_LEFT or event.key == pg.K_a:
              #     player.rect.x  -= 50
              # if event.key == pg.K_RIGHT or event.key == pg.K_d:
              #     player.rect.x +=50
              # if event.key == pg.K_UP or event.key == pg.K_w:
              #     player.rect.y  -= 50
              # if event.key == pg.K_DOWN or event.key == pg.K_s:
              #     player.rect.y += 50
              # if event.key == pg.K_KP_9:
              #   player.rect.x -= 50
              #   player.rect.y -= 50
              # if event.key == pg.K_KP_3:
              #   player.rect.x -= 50
              #   player.rect.y += 50
              # if event.key == pg.K_KP_1:
              #   player.rect.x += 50
              #   player.rect.y += 50
              # if event.key == pg.K_KP_7:
              #   player.rect.x += 50
              #   player.rect.y -= 50
              # if event.key == pg.K_KP_6:
              #   player.rect.x += 50
              # if event.key == pg.K_KP_6:
              #   player.rect.x -= 50
              # if event.key == pg.K_KP_8:
              #   player.rect.y += 50
              # if event.key == pg.K_KP_6:
              #   player.rect.y -= 50
           # if event.type == pg.KEYUP:
           #    if event.key == pg.K_RIGHT:
           #         player.speedx = 0
           #    if event.key == pg.K_LEFT:
           #         player.speedx = 0
           #    if event.key == pg.K_UP:
           #             player.speedy = 0
           #    if event.key == pg.K_DOWN:
           #         player.speedy = 0

         if event.type == pg.QUIT:
            running = False



    # make updates
     all_Sprites.update()



    # render (Draw)
     screen.fill(GREEN)
     all_Sprites.draw(screen)



    # last thing we do
     pg.display.flip()


pg.quit()