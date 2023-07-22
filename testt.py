import pygame
import math

# Define the colors for each category
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]

# Define the values for each category
values = [30, 20, 10, 25, 15]

# Initialize Pygame
pygame.init()

# Set up the window
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pie Chart")

# Set up the pie chart properties
radius = min(window_width, window_height) // 2 - 50
center_x, center_y = window_width // 2, window_height // 2
total = sum(values)

# Draw the pie chart
start_angle = 0
for i, value in enumerate(values):
    # Calculate the angle and end angle for the current category
    angle = 2 * math.pi * value / total
    end_angle = start_angle + angle

    # Draw the pie slice
    pygame.draw.arc(window, colors[i], (center_x - radius, center_y - radius, radius * 2, radius * 2), start_angle,
                    end_angle, int(radius / 2))

    # Update the start angle for the next category
    start_angle = end_angle

# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

# Quit the program
pygame.quit()