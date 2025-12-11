import pygame
import sys
pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("DDA Algorithm")
white = (255,255,255)   #(R,G,B)
black = (0,0,0)

'''
#Taking points from user
print("Enter the first points:")
x1=int(input())
y1=int(input())
print("Enter the second points:")
x2=int(input())
y2=int(input())
'''

def line_generation(x1,y1,x2,y2):

    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx),abs(dy))

    x_inc = dx/steps
    y_inc = dy/steps

    x = x1
    y = y1

    for i in range(steps+1):
        screen.set_at((round(x),round(y)),white)
        x = x + x_inc
        y = y + y_inc

    
def main():
    screen.fill(black)
    line_generation(100,100,150,50)
    line_generation(150,50,200,100)
    line_generation(100,100,200,100)
    line_generation(100,100,100,200)
    line_generation(200,100,200,200)
    line_generation(100,200,200,200)
    line_generation(130,150,170,150)
    line_generation(130,150,130,200)
    line_generation(170,150,170,200)

    line_generation(300,100,350,50)
    line_generation(350,50,400,100)
    line_generation(300,100,400,100)
    line_generation(300,100,300,200)
    line_generation(400,100,400,200)
    line_generation(300,200,400,200)
    line_generation(330,150,370,150)
    line_generation(330,150,330,200)
    line_generation(370,150,370,200)
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__" :
    main()

