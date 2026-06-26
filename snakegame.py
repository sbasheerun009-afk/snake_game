import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
BLOCK_SIZE = 20
FPS = 10

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 30)
big_font = pygame.font.SysFont("Arial", 50)

high_score = 0


def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def random_food():
    x = random.randrange(0, WIDTH, BLOCK_SIZE)
    y = random.randrange(0, HEIGHT, BLOCK_SIZE)
    return (x, y)


def game():
    global high_score

    snake = [(100, 100)]
    dx = BLOCK_SIZE
    dy = 0

    food = random_food()
    score = 0

    running = True

    while running:

        clock.tick(FPS)

        # Events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -BLOCK_SIZE
                    dy = 0

                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = BLOCK_SIZE
                    dy = 0

                elif event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -BLOCK_SIZE

                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = BLOCK_SIZE

        # Move snake
        head_x, head_y = snake[0]
        new_head = (head_x + dx, head_y + dy)

        # Wall collision
        if (
            new_head[0] < 0
            or new_head[0] >= WIDTH
            or new_head[1] < 0
            or new_head[1] >= HEIGHT
        ):
            break

        # Self collision
        if new_head in snake:
            break

        snake.insert(0, new_head)

        # Eat food
        if new_head == food:
            score += 1
            food = random_food()

            while food in snake:
                food = random_food()
        else:
            snake.pop()

        # Update high score
        if score > high_score:
            high_score = score

        # Draw
        screen.fill(BLACK)

        pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

        for part in snake:
            pygame.draw.rect(screen, GREEN, (part[0], part[1], BLOCK_SIZE, BLOCK_SIZE))

        draw_text(f"Score: {score}", font, WHITE, 10, 10)
        draw_text(f"High Score: {high_score}", font, WHITE, 350, 10)

        pygame.display.update()

    # Game Over Screen
    while True:

        screen.fill(BLACK)

        draw_text("GAME OVER", big_font, RED, 150, 180)
        draw_text(f"Score : {score}", font, WHITE, 220, 260)
        draw_text(f"High Score : {high_score}", font, WHITE, 180, 310)
        draw_text("Press R to Restart", font, GREEN, 160, 380)
        draw_text("Press Q to Quit", font, GREEN, 180, 430)

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    game()
                    return

                if event.key == pygame.K_q:
                    pygame.quit()
                    return


game()