# ATTRIBUTION
# Code created by :Jaxon Snow
# Art created by: www.kenny.nl
# tutorial found at kidscancode.org


import pygame as pg
import random
from os import *

WIDTH = 480
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
font_name = pg.font.match_font('arial')  # Move to constants

############# GAME constants ##############
# folder var.
game_folder = path.dirname(__file__)
imgs_folder = path.join(game_folder, "imgs")
snds_folder = path.join(game_folder, "snds")
scores_folder = path.join(game_folder, "scores")
background_folder = path.join(imgs_folder, "background")
enemy_imgs_folder = path.join(imgs_folder, "enemy")
players_folder = path.join(imgs_folder, "player")
animation_folder = path.join(imgs_folder,"animations")

# initialize pygame and create window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Shmup!")
clock = pg.time.Clock()
debug = False


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.shield = 100
        self.fuel = 100
        self.lives = 3
        self.hidden = False
        self.hide_timer = pg.time.get_ticks()

        # self.image = pg.Surface((50, 40))
        # self.image.fill(BLACK)
        self.image = ship_img
        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * .75 / 2
        if debug:
            pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.shoot_delay = 250
        self.last_shot = pg.time.get_ticks()

    def shoot(self):
        now = pg.time.get_ticks()
        if  (now - self.last_shot) > self.shoot_delay:
            self.last_shot = now
            b = Bullet(self.rect.centerx, self.rect.top - 1)
            all_sprites.add(b)
            bullet_group.add(b)
            shoot_snd

    def hide(self):
        self.hidden = True
        self.hide_timer = pg.time.get_ticks()
        self.rect.center = (WIDTH/2, HEIGHT + 500)

    def update(self):

        if self.hidden and pg.time.get_ticks() - self.hide_timer>3000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -8
            self.fuel -= .5
        if keystate[pg.K_RIGHT]:
            self.speedx = 8
            self.fuel -= .5
        if keystate[pg.K_SPACE]:
            self.shoot()
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        # self.image = pg.Surface((5, 10))
        # self.image.fill(BLACK)
        self.image = bullet_img

        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(self.image, (6, 12))
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * .75 / 2
        if debug:
            pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -50

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom <= 0:
            self.kill()

#explosions
class Explosions(pg.sprite.Sprite):
    def __init__(self,center,size):
        super(Explosions, self).__init__()
        self.size = size
        self.image = exp_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 50


    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update> self.frame_rate:
            self.last_update = now
            self.frame +=1
            if self.frame == len(exp_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = exp_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class NPC(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # self.image = pg.Surface((30, 40))
        # self.image.fill(WHITE)
        self.image_orig = random.choice(meteor_imgs)

        self.image_orig.set_colorkey(BLACK)
        # self.image_orig = pg.transform.scale(self.image_orig, (50, 50))
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * .75 / 2
        if debug:
            pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.rot = 0
        self.rot_speed = random.randint(-8, 8)
        self.last_update = pg.time.get_ticks()

    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 60:
            self.last_update = now
            # rotate sprite
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pg.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
        # if debug:
        #     pg.draw.circle(self.image, RED, self.rect.center, self.radius)


############load images###################
background = pg.image.load(path.join(background_folder, "bg1.png")).convert()
background = pg.transform.scale(background, (WIDTH, HEIGHT))
background_rect = background.get_rect()
npc_img = pg.image.load(path.join(enemy_imgs_folder, "enemy1.png")).convert()
ship_img = pg.image.load(path.join(players_folder, "player_ship.png")).convert()
bullet_img = pg.image.load(path.join(players_folder, "laser.png")).convert()
meteor_imgs = []
meteor_list = ['enemy1.png', 'enemy2.png', 'enemy3.png', 'enemy4.png']
for img in meteor_list:
    meteor_imgs.append(pg.image.load(path.join(enemy_imgs_folder, img)).convert())
exp_anim = {}
exp_anim["lg"] = []
exp_anim["sm"] = []
for i in range(9):
    filename = "regularExplosion0{}.png".format(i)
    image = pg.image.load(path.join(animation_folder, filename)).convert()
    image.set_colorkey(BLACK)
    image_lg = pg.transform.scale(image,(100,100))
    exp_anim["lg"].append(image_lg)
    image_sm = pg.transform.scale(image, (75, 75))
    exp_anim["sm"].append(image_lg)

#load sounds
####################################################################
shoot_snd = pg.mixer.Sound(path.join(snds_folder,"pew.wav"))
expl_snd = []
for snd in ["expl3.wav","expl6.wav"]:
    expl_snd.append(pg.mixer.Sound(path.join(snds_folder,snd)))

pg.mixer.music.load(path.join(snds_folder,'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pg.mixer.music.set_volume(0.4)
####################################################################

# create Sprite groups
####################################################################
all_sprites = pg.sprite.Group()
players_group = pg.sprite.Group()
npc_group = pg.sprite.Group()
bullet_group = pg.sprite.Group()


####################################################################

def spawn_npc():
    for i in range(1):
        npc = NPC()
        npc_group.add(npc)
        all_sprites.add(npc)


score = 0



def draw_text(surf, text, size, x, y, color):
    font = pg.font.Font(font_name, size)
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surf, text_rect)

def draw_bar(surface,x,y,color,pct):
    if pct <0:
        pct = 0
    bar_length = 100
    bar_height = 40
    fill = (pct/100)*bar_length
    outline =pg.Rect(x,y,bar_length,bar_height)
    fillrect = pg.Rect(x,y,fill,bar_height)
    pg.draw.rect(surface,GREEN,fillrect)
    pg.draw.rect(surface,WHITE,outline, 3)


# create Game Objects
####################################################################
player = Player()
npc = NPC()

for i in range(12):
    npc = NPC()
    npc_group.add(npc)
bullet = Bullet(WIDTH / 2, HEIGHT / 2)

####################################################################

# add objects to sprite groups
####################################################################
players_group.add(player)
npc_group.add(npc)
bullet_group.add(bullet)
all_sprites.add(bullet)

for i in players_group:
    all_sprites.add(i)
for i in npc_group:
    all_sprites.add(i)
# Game loop
running = True
diff = 0
pg.mixer.music.play(loops =-1)
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            # if event.key == pg.K_UP or event.key == pg.K_SPACE:
            #     player.shoot()
            if event.key == pg.K_F12:
                debug = True

    # Update
    hits = pg.sprite.spritecollide(player, npc_group, False, pg.sprite.collide_circle)
    if hits:
        exp = Explosions(hits[0].rect.center,"sm")
        all_sprites.add(exp)
        random.choice(expl_snd).play()
        player.shield-=hits[0].radius*2
        print(player.shield)
        if player.shield<=0:
            exp = Explosions(player.rect.center,"lg")
            all_sprites.add(exp)
            player.hide()
            player.lives -=1
            player.shield = 100
        if player.lives == 0 and not exp.alive():
                running = False


    hits = pg.sprite.groupcollide(npc_group, bullet_group, True, True, pg.sprite.collide_circle)
    for hit in hits:
        if hit.radius < 30:
            size = "sm"
        else:
            size = "lg"
        exp = Explosions(hit.rect.center,"sm")
        all_sprites.add(exp)
        random.choice(expl_snd).play()
        spawn_npc()
        score += 50 - hit.radius
        print(score)

    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    # draw HUD
    draw_text(screen, "Score:" + str(score), 18, WIDTH / 2, 15, WHITE)
    draw_bar(screen, 5, 15, GREEN, player.shield)
    draw_bar(screen, 5, 55, BLUE, player.fuel)

    # *after* drawing everything, flip the display
    pg.display.flip()

pg.quit()
