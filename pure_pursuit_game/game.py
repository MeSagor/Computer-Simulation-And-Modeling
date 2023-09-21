import pygame
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fighter-Bomber')

fighterImage = pygame.transform.scale(pygame.image.load('./pure_pursuit_game/images/fighter.png'), (50,40))
bomberImage = pygame.transform.scale(pygame.image.load('./pure_pursuit_game/images/bomber.png'), (60,40))
originalbomberImage = bomberImage.copy()
originalfighterImage = fighterImage.copy()
clock = pygame.time.Clock()

FPS = 60
fighter_speed = 3
bomber_speed = 2
intercept_range = 70

fighter_x = 10
fighter_y = 10
bomber_x = 500
bomber_y = 500

bomber_direction = False
left_key_pressed = False
right_key_pressed = False
up_key_pressed = False
down_key_pressed = False

def fighter_position_calculate():
    global fighter_x, fighter_y, running, fighterImage

    angle_to_rotate = math.degrees(math.atan2(bomber_x - fighter_x, bomber_y - fighter_y))
    fighterImage = originalfighterImage
    fighterImage = pygame.transform.rotate(fighterImage, angle_to_rotate + 280)

    distance = math.sqrt((bomber_x - fighter_x)**2 + (bomber_y - fighter_y)**2)
    if distance <= intercept_range:
        running = False

    time_to_intercept = distance / fighter_speed

    fighter_x += (bomber_x - fighter_x) / time_to_intercept
    fighter_y += (bomber_y - fighter_y) / time_to_intercept


def reset_key_status():
    global left_key_pressed, right_key_pressed, up_key_pressed, down_key_pressed, bomber_direction

    bomber_direction = False
    left_key_pressed = False
    right_key_pressed = False
    up_key_pressed = False
    down_key_pressed = False


def bomber_position_calculate():
    global bomber_x, bomber_y, bomberImage, bomber_direction

    if left_key_pressed:
        bomber_x -= bomber_speed
        if bomber_direction == False:
            bomberImage = originalbomberImage
            bomberImage = pygame.transform.rotate(bomberImage, 90)
            bomber_direction = True
    elif right_key_pressed:
        bomber_x += bomber_speed
        if bomber_direction == False:
            bomberImage = originalbomberImage
            bomberImage = pygame.transform.rotate(bomberImage, 270)
            bomber_direction = True
    elif up_key_pressed:
        bomber_y -= bomber_speed
        if bomber_direction == False:
            bomberImage = originalbomberImage
            bomberImage = pygame.transform.rotate(bomberImage, 0)
            bomber_direction = True
    elif down_key_pressed:
        bomber_y += bomber_speed
        if bomber_direction == False:
            bomberImage = originalbomberImage
            bomberImage = pygame.transform.rotate(bomberImage, 180)
            bomber_direction = True


def draw_window():
    screen.fill((255, 255, 255))
    screen.blit(fighterImage, (fighter_x, fighter_y))
    screen.blit(bomberImage, (bomber_x, bomber_y))
    pygame.display.flip()
    bomber_position_calculate()
    fighter_position_calculate()


running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        reset_key_status()
        up_key_pressed = True
    elif keys[pygame.K_DOWN]:
        reset_key_status()
        down_key_pressed = True
    elif keys[pygame.K_LEFT]:
        reset_key_status()
        left_key_pressed = True
    elif keys[pygame.K_RIGHT]:
        reset_key_status()
        right_key_pressed = True
    
    draw_window()

pygame.quit()