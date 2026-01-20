import math
import pygame
import sys

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bresenham's Line Algorithm")

white = (255, 255, 255)
black = (0, 0, 0)


def line_generation(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if x2 > x1:
        x_inc = 1 
    else :
        x_inc = -1
    if y2 > y1:
        y_inc = 1 
    else:
        y_inc = -1

    x = x1
    y = y1

    if dx > dy:
        p = 2 * dy - dx
        for i in range(dx + 1):
            screen.set_at((x, y), white)
            x = x + x_inc
            if p >= 0:
                y =y + y_inc
                p = p + 2*dy - 2*dx
            else:
                p = p + 2*dy
    else:
        p = 2 * dx - dy
        for i in range(dy + 1):
            screen.set_at((x, y), white)
            y = y + y_inc
            if p >= 0:
                x = x + x_inc
                p = p + 2 * dx - 2 * dy
            else:
                p = p + 2 * dx

def translation(x1, y1, x2, y2, tx, ty):
    x3 = x1 + tx
    y3 = y1 + ty
    x4 = x2 + tx
    y4 = y2 + ty

    line_generation(x3, y3, x4, y4)

def scaling(x1, y1, x2, y2, Sx, Sy, c_x, c_y):
    x3 = int(Sx * (x1 - c_x) + c_x)
    y3 = int(Sy * (y1 - c_y) + c_y)
    x4 = int(Sx * (x2 - c_x) + c_x)
    y4 = int(Sy * (y2 - c_y) + c_y)

    line_generation(x3, y3, x4, y4)

def reflection(x1, y1, x2, y2, axis, c_x, c_y):
    def reflect_points(x, y):
        x = x - c_x 
        y = y - c_y
        if axis == "x":
            y = -y
        elif axis == "y":
            x = -x
        return (x + c_x, y + c_y)
    x3, y3 = reflect_points(x1, y1)
    x4, y4 = reflect_points(x2, y2)
    line_generation(x3, y3, x4, y4)

def rotation(x1, y1, x2, y2, angle, c_x, c_y):
    rad = math.radians(angle)
    def rotate_points(x, y):
        x = x - c_x
        y = y - c_y
        x3 = int(x * math.cos(rad) + y * math.sin(rad))
        y3 = int(x * math.sin(rad) - y * math.cos(rad))
        return(x3 + c_x, y3 + c_y)
    x4, y4 = rotate_points(x1, y1)
    x5, y5 = rotate_points(x2, y2)
    line_generation(x4, y4, x5, y5)

def main():
    screen.fill(black)
    while True:
        # -----Option Displaying------
        print("------Choose the options------")
        print("-"*30)
        print("EnterKey|\tOperation")
        print("-"*30)
        print("1\t|\tTranslation")
        print("2\t|\tScaling")
        print("3\t|\tReflection")
        print("4\t|\tRotation")
        print("5\t|\tExit program")
        choice = int(input(("Enter your choice:")))
    
        match choice:
            case 1:
                # Taking two points from user
                print("Enter the first point (x1, y1):")
                x1 = int(input())
                y1 = int(input())

                print("Enter the second point (x2, y2):")
                x2 = int(input())
                y2 = int(input())
                print("Enter the translating factor : ")
                tx = int(input("tx = "))
                ty = int(input("ty = "))
                line_generation(x1, y1, x2, y2)
                translation(x1, y1, x2, y2, tx, ty)
                break
            case 2:
                # Taking two points from user
                print("Enter the first point (x1, y1):")
                x1 = int(input())
                y1 = int(input())

                print("Enter the second point (x2, y2):")
                x2 = int(input())
                y2 = int(input())
                print("Enter the scaling factor : ")
                Sx = int(input("Sx = "))
                Sy = int(input("Sy = "))
                print("#Recommended to enter (x,y) = (0,0)")
                print("Enter the center : ")
                c_x = int(input("Coordinate of x = "))
                c_y = int(input("Coordinate of y = "))
                line_generation(x1, y1, x2, y2)
                scaling(x1, y1, x2, y2, Sx, Sy, c_x, c_y)
                break
            case 3:
                # Taking two points from user
                print("Enter the first point (x1, y1):")
                x1 = int(input())
                y1 = int(input())

                print("Enter the second point (x2, y2):")
                x2 = int(input())
                y2 = int(input())
                axis = input("Enter the reflection axis : ")
                print("Enter the center : ")
                c_x = int(input("Coordinate of x = "))
                c_y = int(input("Coordinate of y = "))
                line_generation(x1, y1, x2, y2)
                reflection(x1, y1, x2, y2, axis, c_x, c_y)
                break
            case 4:
                # Taking two points from user
                print("Enter the first point (x1, y1):")
                x1 = int(input())
                y1 = int(input())

                print("Enter the second point (x2, y2):")
                x2 = int(input())
                y2 = int(input())
                angle = int(input("Enter the rotation angle : "))
                print("Enter the center : ")
                c_x = int(input("Coordinate of x = "))
                c_y = int(input("Coordinate of y = "))
                line_generation(x1, y1, x2, y2)
                rotation(x1, y1, x2, y2, angle, c_x, c_y)
                break
            case 5:
                exit(0)
            case _:
                print("Invalid Input !!")
                
    
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
