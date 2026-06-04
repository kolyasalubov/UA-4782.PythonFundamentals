import pygame, random

pygame.init()
screen = pygame.display.set_mode((800, 500))
font = lambda s: pygame.font.SysFont("Century Gothic", s, True)

BG, TXT = (255, 240, 245), (74, 20, 140)
sec, att, val, msg, run = random.randint(1, 100), 0, "", "Enter a number (1-100)", True

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if att >= 10 or msg.startswith("Win"):
                sec, att, val, msg = random.randint(1, 100), 0, "", "Enter a number (1-100)"
            elif e.key == pygame.K_RETURN and val.isdigit():
                att += 1
                guess = int(val)
                if guess == sec: msg = f"Win! It was {sec}."
                elif att >= 10: msg = f"Game Over! It was {sec}."
                else: msg = f"Too {'low' if guess < sec else 'high'}! Try again."
                val = ""
            elif e.key == pygame.K_BACKSPACE: val = val[:-1]
            elif e.unicode.isdigit() and len(val) < 3: val += e.unicode

    screen.fill(BG)
    for t, s, y, c in [("Guess the Number", 44, 40, TXT), (f"Attempts: {att} / 10", 26, 120, TXT), (msg, 26, 290, TXT), ("Press Enter to submit" if att < 10 and not msg.startswith("Win") else "Press any key to restart", 18, 410, BG)]:
        txt_surf = font(s).render(t, True, c)
        screen.blit(txt_surf, (400 - txt_surf.get_width() // 2, y))

    pygame.draw.rect(screen, BG, (300, 185, 200, 65), 0, border_radius=20)
    pygame.draw.rect(screen, TXT, (300, 185, 200, 65), 3, border_radius=20)
    inp_surf = font(40).render(val, True, TXT)
    screen.blit(inp_surf, (400 - inp_surf.get_width() // 2, 218 - inp_surf.get_height() // 2))

    pygame.display.flip()

pygame.quit()