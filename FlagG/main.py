import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Display
width, height = 300, 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Custom Flag")

# Colors
green = (0, 128, 0)
yellow = (255, 223, 0)
blue = (0, 0, 128)

# Draw the flag
screen.fill(green)

# Draw the losange
diamond_points = [(width // 2, 0), (width, height // 2), (width // 2, height), (0, height // 2)]
pygame.draw.polygon(screen, yellow, diamond_points)

# Calculate the center of the diamond
diamond_center = (width // 2, height // 2)

# Calculate the radius of the circle (half the height of the diamond)
circle_radius = height // 4

# Draw the circle
pygame.draw.circle(screen, blue, diamond_center, circle_radius)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
