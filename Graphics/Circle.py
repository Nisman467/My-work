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
points = []
#circle_points = []

def adding_points(x_center, y_center, x, y):
    return [
        (x_center + x, y_center + y),
        (x_center - x, y_center + y),
        (x_center + x, y_center - y),
        (x_center - x, y_center - y),
        (x_center + y, y_center + x),
        (x_center - y, y_center + x),
        (x_center + y, y_center - x),
        (x_center - y, y_center - x)
    ]

def circle_generate(x, y, r):
    #global circle_points
    p = 1 - r
    while x <= y:
        points = adding_points(x_center, y_center, x, y)
        #circle_points.extend(points)
        for px, py in points:
                screen.set_at((px, py), white)
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
