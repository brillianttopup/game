import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clock and FPS
clock = pygame.time.Clock()
FPS = 60

# Player settings
player_width, player_height = 50, 50
player_x, player_y = 100, HEIGHT - player_height - 50
player_velocity = 5
is_jumping = False
jump_height = 10
gravity = 0.5
y_velocity = 0

# Ground
ground_height = 50

# Main game loop
def main():
    global player_y, is_jumping, y_velocity

    running = True
    while running:
        screen.fill(WHITE)

        # Draw ground
        pygame.draw.rect(screen, GREEN, (0, HEIGHT - ground_height, WIDTH, ground_height))

        # Draw player
        pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not is_jumping:
            is_jumping = True
            y_velocity = -jump_height

        # Jump logic
        if is_jumping:
            player_y += y_velocity
            y_velocity += gravity
            if player_y >= HEIGHT - player_height - ground_height:
                player_y = HEIGHT - player_height - ground_height
                is_jumping = False

        # Update screen
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
