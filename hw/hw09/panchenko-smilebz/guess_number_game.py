import pygame
from random import randint
import sys

pygame.init()

# Window settings
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Number")

# Colors
WHITE = (252, 242, 232)
BLACK = (34, 23, 11)
GREEN = (0, 180, 0)
RED = (200, 0, 0)
BLUE = (0, 100, 255)

# Fonts
font = pygame.font.SysFont(None, 40, bold=True)
small_font = pygame.font.SysFont(None, 30)

# Random number
secret_number = randint(1, 100)

# Game variables
user_text = ""
message = "Guess a number from 1 to 100"
attempts = 10
game_over = False

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    # Draw title
    title = font.render("Guess the Number", True, BLACK)
    text_rect = title.get_rect(center=(WIDTH // 2, 50))
    screen.blit(title, text_rect.topleft)

    # Draw message
    msg_surface = small_font.render(message, True, BLACK)
    screen.blit(msg_surface, (100, 150))

    # Draw attempts
    attempts_surface = small_font.render(f"Attempts left: {attempts}", True, RED)
    screen.blit(attempts_surface, (100, 200))

    # Draw input box
    pygame.draw.rect(screen, BLACK, (100, 260, 200, 50), 2)

    input_surface = font.render(user_text, True, BLACK)
    screen.blit(input_surface, (110, 270))

    instructions = small_font.render("Press ENTER to submit", True, BLACK)
    screen.blit(instructions, (100, 330))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_RETURN:
                if user_text.isdigit():
                    guess = int(user_text)
                    attempts -= 1

                    if guess == secret_number:
                        message = f"Congratulations! Number was {secret_number}"
                        game_over = True

                    elif guess < secret_number:
                        message = "The secret number is GREATER"

                    else:
                        message = "The secret number is LESS"

                    if attempts == 0 and guess != secret_number:
                        message = f"You lost! Number was {secret_number}"
                        game_over = True

                user_text = ""

            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]

            else:
                if event.unicode.isdigit():
                    user_text += event.unicode

    pygame.display.update()
    clock.tick(60)
