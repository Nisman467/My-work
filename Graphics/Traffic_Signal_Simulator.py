import pygame
import random 
pygame .init()

width = 800
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Traffic Signal Simulator")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

#Color
White = (255, 255, 255)
Green = (0, 255, 0)
Yellow = (255, 255, 0)
Red = (255, 0, 0)
Grey = (50, 50, 50)


signal = ["Red", "Red", "Red", "Red"]
current_green = 0
signal[current_green] = "Green"

class Car:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.dir = direction
        self.stress = 0
        self.speed = 2

    def move(self, can_move):
        if can_move:
            self.stress = max(0, self.stress - 0.15)
            if self.dir == 0: self.y += self.speed
            if self.dir == 1: self.x -= self.speed
            if self.dir == 2: self.y -= self.speed
            if self.dir == 3: self.x += self.speed
        else:
            self.stress += 0.15

    def color(self):
        if self.stress < 10 :
            return Green
        elif self.stress < 30 :
            return Yellow
        else:
            return Red

#Define cars 
cars = [] 

def random_car_generate():
    direction = random.randint(0,3)

    if direction == 0:
        return Car(390, 0, 0) #top
    elif direction == 1:
        return Car(410, 600, 2) #bottom
    elif direction == 2:
        return Car(800, 290, 1) #right
    else:
        return Car(0, 310, 3) #left

#calculation of a stress of a certain road \
def road_stress(index):
    return sum(car.stress for car in cars if car.dir == index)


##main running program
running = True
timer = 0   #time means fps: frames
waiting = False

while running:
    screen.fill(Grey)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #change signal based on stress 
    timer += 1

    if not waiting:
        stresses = [road_stress(i) for i in range(4)]
        next_green = stresses.index(max(stresses))
        if next_green != current_green:
            signal = ["Red"] * 4
            waiting = True
            timer = 0

    if timer > 90:     #timer = 120 -> 2 seconds
        cars.append(random_car_generate())
        stresses = [road_stress(i) for i in range(4)]
        current_green = stresses.index(max(stresses))
        signal = ["Red", "Red", "Red", "Red"]       # or ["Red"] * 4
        signal[current_green] = "Green"
        waiting = False
        timer = 0

    
    #Draw a intersection point
    pygame.draw.rect(screen, White, (350, 250, 100, 100))


    #moving the cars now 
    # Moving the cars
    for car in cars:
        can_move = True
        
        # Check signal and position for each direction
        if signal[car.dir] == "Red":
            if car.dir == 0 and 230 > car.y + 20 >= 220: # Top car
                can_move = False
            elif car.dir == 1 and 450 < car.x <= 460:   # Right car
                can_move = False
            elif car.dir == 2 and 350 < car.y <= 360:   # Bottom car
                can_move = False
            elif car.dir == 3 and 330 > car.x + 20 >= 320: # Left car
                can_move = False

        car.move(can_move)
        pygame.draw.rect(screen, car.color(), (car.x, car.y, 20, 20))

    #Displaying the stress value 
    for i in range(4):
        text = font.render(f"Road {i} Stress : {int(road_stress(i))}", True, White)
        screen.blit(text, (10, 10 + i * 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
