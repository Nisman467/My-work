import pygame
import sys
pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Mid-point Ellipse Generation")

white = (255,255,255)
black = (0,0,0)

#taking inputs from users
print("Enter the center of the ellipse : ")
x_c = int(input())
y_c = int(input())

r_x = int(input("Enter the radius of x-aixs : "))
r_y = int(input("Enter the radius of y-aixs : "))

x = 0
y = r_y

def ellipse_generation(x, y, r_x, r_y):
    p1 = r_y * r_y - r_x * r_x * r_y + 0.25 * r_x * r_x

    while (2 * r_y * r_y * x < 2 * r_x * r_x * y):

        screen.set_at((x_c + x , y_c + y),"RED")
        screen.set_at((x_c + x , y_c - y),"BLUE")
        screen.set_at((x_c - x , y_c + y),"PURPLE")
        screen.set_at((x_c - x , y_c - y),"ORANGE")


        x = x + 1
        if p1 < 0:
            p1 = p1 + 2 * r_y * r_y * x + r_y * r_y
        else:
            y = y - 1
            p1 = p1 + 2 * r_y * r_y * x - 2 * r_x * r_x * y + r_y * r_y 

    while y > 0:

        x1 = x
        y1 = y
        x = (2 * x + 1)/2
        y = y - 1

        p2 = r_y * r_y * x * x + r_x * r_x * y * y - r_x * r_x * r_y * r_y
        x = x1
        y = y1

        y = y - 1
        if p2 < 0:
            p2 = p2 + 2 * r_y * r_y * x - 2 * r_x * r_x * y + r_x * r_x
            x = x + 1
        else:
            p2 = p2 - 2 * r_x * r_x * y + r_x * r_x

        screen.set_at((x_c + x , y_c + y),"PINK")
        screen.set_at((x_c + x , y_c - y),"YELLOW")
        screen.set_at((x_c - x , y_c + y),"GREEN")
        screen.set_at((x_c - x , y_c - y),white)


def main():
    screen.fill(black)
    ellipse_generation(x, y, r_x, r_y)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()