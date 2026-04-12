import pygame
pygame.init()

SCREEN_W,SCREEN_H = 500,500
display_surface = pygame.display.set_mode((SCREEN_W,SCREEN_H))
pygame.display.set_caption("adding a image and background image")

bg = pygame.transform.scale(pygame.image.load("back.png").convert(),(SCREEN_W,SCREEN_H))
img = pygame.transform.scale(pygame.image.load("image.png").convert_alpha(),(200,200))
x = img.get_rect(center = (SCREEN_W//2,SCREEN_H//2-30))
text = pygame.font.Font(None,36).render("Messi is the goat",True,pygame.Color("red"))
y =  text.get_rect(center = (SCREEN_W//2,SCREEN_H//2+110))

done = False
while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    display_surface.blit(bg,(0,0))
    display_surface.blit(img,x)
    display_surface.blit(text,y)
    pygame.display.flip()
pygame.quit()