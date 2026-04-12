import pygame 
pygame.init()
screen = pygame.display.set_mode((400,400))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.circle(screen,(255,0,0),(100,100),50)
    pygame.draw.circle(screen,(255,0,0),(200,50),50,1)
    pygame.display.flip()
    
