# Full name: Fatema Anishbhai Lokhandwala
# Student number: 101259465


# Importing the pygame multimedia library
import pygame

# Creating a variable to store the RGB values of the color white
white_color = (255, 255, 255)

# Creating a variable to store the RGB values of the color navy blue
navy_blue_color = (42, 52, 67)

# Creating a variable to store the RGB values of the color lavender
lavender_color = (131, 117, 175)

# Creating a pygame window of dimensions 480 × 640
window = pygame.display.set_mode((480, 640))

# Filling the window surface so that it has a background colour of white
window.fill((white_color))

# Creating the navy blue color polygon  
pygame.draw.polygon(window, (navy_blue_color), ((0, 320), (160, 532), (160, 640), (78, 640), (0, 536)))

# Creating the lavender color polygon  
pygame.draw.polygon(window, (lavender_color), ((160, 532), (320, 532), (320, 426), (400, 426), (400, 532), (320, 640), (160, 640)))

# Updating the screen with the drawings
pygame.display.update()

# Saving the window surface
pygame.image.save(window, "assigned_image_for_101259465.png")