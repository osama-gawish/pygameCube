import pygame
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw a Circle")


# Define the angle of rotation in radians
theta = np.radians(5)  # Convert degrees to radians

# make the coordinates system at the cnter of the screen 
T = np.array([[1, 0, 0, 400],
             [0, 1, 0, 300],
             [0, 0, 1, 0],
             [0, 0, 0, 1]])

# Define the rotation matrixes
R_x = np.array([
    [1, 0, 0, 0],
    [0, np.cos(theta), -np.sin(theta), 0],
    [0, np.sin(theta), np.cos(theta), 0],
    [0, 0, 0, 1]
])
R_y = np.array([
    [np.cos(theta), 0, np.sin(theta), 0],
    [0, 1, 0, 0],
    [-np.sin(theta), 0, np.cos(theta), 0],
    [0, 0, 0, 1]
])
R_z = np.array([
    [np.cos(theta), -np.sin(theta), 0, 0],
    [np.sin(theta), np.cos(theta), 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

# Define the circle parameters
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255,255)

points = np.array([[-100, -100, -100, 1],
                   [100, -100, -100, 1],
                   [100, 100, -100, 1],
                   [-100, 100, -100, 1],
                   [-100, -100, 100, 1],
                   [100, -100, 100, 1],
                   [100, 100, 100, 1],
                   [-100, 100, 100, 1]])

point_radius = 10
point_speed = 1

# Create a clock object to manage the frame rate
clock = pygame.time.Clock()
fps = 15  # Set the desired FPS

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(black)

    # # Draw the circle
    pygame.draw.circle(screen, green,(400, 300), point_radius)
    
    # Rotate each point around the center
    rotated_points = [R_x @ point for point in points]
    transformed_points = [T @ point for point in rotated_points]

    # Update the points for the next frame
    points = rotated_points

    # Draw the circles
    for point in transformed_points:
        pygame.draw.circle(screen, red, point[:2], point_radius)
    
    # num_points = len(transformed_points)
    # for i in range(num_points):
    #     pygame.draw.line(screen, white, transformed_points[i][:2], transformed_points[(i + 1) % num_points][:2])
    
    # Draw lines between the points to form a cube
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom face
        (4, 5), (5, 6), (6, 7), (7, 4),  # Top face
        (0, 4), (1, 5), (2, 6), (3, 7)   # Vertical edges
    ]

    for edge in edges:
        pygame.draw.line(screen, white, transformed_points[edge[0]][:2], transformed_points[edge[1]][:2])
    
    # Update the display
    pygame.display.flip()
    # Cap the frame rate
    clock.tick(fps)

# Quit Pygame
pygame.quit()
sys.exit()

# Ensure the circle stays within the window boundaries
# point1[0] = max(point_radius, min(width - point_radius, point1[0]))
# point1[1] = max(point_radius, min(height - point_radius, point1[1]))
    
# for i, point in enumerate(points):
#     point = R_z @ point 
#     pointo = T @ point
#     pygame.draw.circle(screen, red, pointo[:2], point_radius)
#     points[i] = point
#     print(points)
