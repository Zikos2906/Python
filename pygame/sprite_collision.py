import pygame
import random

screen_w,screen_h = 500,400
movement_speed = 5
font_size = 72

pygame.init()

background_image = pygame.transform.scale(pygame.image.load("back.png"),(screen_w,screen_h))

font = pygame.font.SysFont("Times New Roman",font_size)

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(pygame.Color("blue"))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()
    def move(self,x_c,y_c):
        self.rect.x = max(min(self.rect.x + x_c,screen_w - self.rect.width),0)
        self.rect.y = max(min(self.rect.y + y_c,screen_h - self.rect.height),0)


screen =pygame.display.set_mode((screen_w,screen_h))
all_sprites = pygame.sprite.Group()
sp1 = Sprite(pygame.Color("black"),20,30)
sp1.rect.x,sp1.rect.y = random.randint(0,screen_w-sp1.rect.width),random.randint(0,screen_h-sp1.rect.height)
all_sprites.add(sp1)

sp2 = Sprite(pygame.Color("red"),20,30)
sp2.rect.x,sp2.rect.y = random.randint(0,screen_w-sp2.rect.width),random.randint(0,screen_h-sp2.rect.height)
all_sprites.add(sp2)

Running,won = True,False

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            Running = False
    if not won :
        keys = pygame.key.get_pressed()
        x_c = (keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*movement_speed
        y_c = (keys[pygame.K_DOWN]-keys[pygame.K_UP])*movement_speed
        sp1.move(x_c,y_c)
        if sp1.rect.colliderect(sp2.rect):
            all_sprites.remove(sp2)
            won = True
    screen.blit(background_image,(0,0))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
