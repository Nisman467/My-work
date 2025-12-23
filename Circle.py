import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Circle Generation")

white = (255, 255, 255)
black = (0, 0, 0)

# Taking inputs from user
print("Enter the center points : ")
x_center = int(input())
y_center = int(input())
print("Enter the radius of a circle : ")
r = int(input())

x = 0
y = r


def circle_generate(x, y, r):
    #global circle_points
    p = 1 - r
    while x <= y:
        
        screen.set_at((x_center + x,y_center + y),white)
        screen.set_at((x_center + x,y_center - y),"RED")
        screen.set_at((x_center - x,y_center + y),"BLUE")
        screen.set_at((x_center - x,y_center - y),"GREEN")
        screen.set_at((y_center + y,x_center + x),"YELLOW")
        screen.set_at((y_center + y,x_center - x),"PINK")
        screen.set_at((y_center - y,x_center + x),"ORANGE")
        screen.set_at((y_center - y,x_center - x),"PURPLE")
        
        x =x + 1
        if p < 0:
            p =p + 2 * x + 3
        else:
            y = y - 1
            p = p + 2 * (x - y) + 5

def main():
    screen.fill(black)
    circle_generate(x, y, r)
    pygame.display.flip()

    # Keep window open
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
