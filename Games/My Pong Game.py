import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
BALL_SIZE = 20
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SPEED = 5
PADDLE_SPEED = 7

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = random.choice([-1, 1]) * BALL_SPEED
ball_dy = random.choice([-1, 1]) * BALL_SPEED

paddle1_y = (HEIGHT - PADDLE_HEIGHT) // 2
paddle2_y = (HEIGHT - PADDLE_HEIGHT) // 2

score1 = 0
score2 = 0

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_y -= PADDLE_SPEED
    if keys[pygame.K_s]:
        paddle1_y += PADDLE_SPEED
    if keys[pygame.K_UP]:
        paddle2_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN]:
        paddle2_y += PADDLE_SPEED

    # Keep paddles in bounds
    paddle1_y = max(0, min(paddle1_y, HEIGHT - PADDLE_HEIGHT))
    paddle2_y = max(0, min(paddle2_y, HEIGHT - PADDLE_HEIGHT))

    # Move ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collisions
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_dy *= -1

    if ball_x <= 0:
        score2 += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx = BALL_SPEED
        ball_dy = random.choice([-1, 1]) * BALL_SPEED

    if ball_x >= WIDTH - BALL_SIZE:
        score1 += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx = -BALL_SPEED
        ball_dy = random.choice([-1, 1]) * BALL_SPEED

    # Paddle collisions
    if ball_x <= PADDLE_WIDTH and paddle1_y <= ball_y <= paddle1_y + PADDLE_HEIGHT:
        ball_dx *= -1
    if ball_x >= WIDTH - PADDLE_WIDTH - BALL_SIZE and paddle2_y <= ball_y <= paddle2_y + PADDLE_HEIGHT:
        ball_dx *= -1

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, (0, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Draw scores
    font = pygame.font.Font(None, 36)
    score_text1 = font.render(str(score1), True, WHITE)
    score_text2 = font.render(str(score2), True, WHITE)
    screen.blit(score_text1, (WIDTH // 4, 20))
    screen.blit(score_text2, (WIDTH * 3 // 4, 20))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
