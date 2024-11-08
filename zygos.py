import pygame
import sys
from pygame import mixer
from fighter import Fighter


class Game:
    def __init__(self):
    
        pygame.init()
        WIDTH, HEIGHT = 640,480
        pygame.display.set_caption('Zygos')
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()

        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img_pos = [160, 260]
        self.img.set_colorkey((0,0,0))
        self.movement = [False, False]

        self.collision_area = pygame.Rect(50,50,300,50)
    
    def run(self):
        while True:
            self.screen.fill((14,219,248))
            self.img_pos[1] += (self.movement[1] - self.movement[0])*5
            self.screen.blit(self.img, self.img_pos)
            self.clock.tick(60)

            img_r = pygame.Rect(self.img_pos[0],self.img_pos[1], self.img.get_width(),self.img.get_height())
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0,100,255), self.collision_area)
            else:
                 pygame.draw.rect(self.screen, (0,50,155), self.collision_area)
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
               
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False             
           
           
            pygame.display.update()

Game().run()



#Level 3
mixer.init()
pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Zygos rahhhhh (Keyboard dedo)")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define colours
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

#define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]#player scores. [P1, P2]
round_over = False
ROUND_OVER_COOLDOWN = 2000

#define fighter variables
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

#load music and sounds
pygame.mixer.music.load("Assets/music_bakchodi.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
sword_fx = pygame.mixer.Sound("Assets/sword_hit.wav")
sword_fx.set_volume(0.5)
magic_fx = pygame.mixer.Sound("Assets/magic.wav")
magic_fx.set_volume(0.75)

#load background image
bg_image = pygame.image.load("Assets/Background.png").convert_alpha()
