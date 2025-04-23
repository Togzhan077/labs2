import pygame
import os
import datetime

_image_library = {}

def get_image(path):
    global _image_library 
    image = _image_library.get(path)
    if image is None:
        canonicalized_path = path.replace("/", os.sep).replace("\\", os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[canonicalized_path] = image
    return image

def blit_rotate(screen, img, pos, angle):
    rotated_img = pygame.transform.rotate(img, angle)
    new_rect = rotated_img.get_rect(center=img.get_rect(center=pos).center)
    screen.blit(rotated_img, new_rect.topleft)

pygame.init()
done = False

screen = pygame.display.set_mode((1200, 800))
w, h = screen.get_size()
bg = pygame.transform.scale(get_image(r"c:/Users/User/Downloads/mainclock.png"), (w, h))
pygame.display.set_caption("Mickey's Clock")

angle_min = 0
angle_sec = 0
topleft = (w // 2, h // 2)

# Load the arm images
left_arm_img = get_image(r"c:/Users/User/Downloads/leftarm (1).png")
right_arm_img = get_image(r"c:/Users/User/Downloads/rightarm.png")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    today = datetime.datetime.now()
    minutes = int(datetime.datetime.strftime(today, '%M'))
    seconds = int(datetime.datetime.strftime(today, '%S'))

    # Position for Mickey's clock center (the center of the screen)
    pos = (screen.get_width() / 2, screen.get_height() / 2)

    # Clear the screen and draw the background image
    screen.blit(bg, (0, 0))

    # Calculate angles for the arms
    angle_min = -6 * minutes + 90  # Adjust for a better starting position for minutes hand
    angle_sec = -6 * seconds + 90  # Adjust for a better starting position for seconds hand

    # Draw Mickey's arms rotated to the correct angles
    blit_rotate(screen, left_arm_img, pos, angle_sec)
    blit_rotate(screen, right_arm_img, pos, angle_min)

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Limit the frame rate to 60 FPS

pygame.quit()
