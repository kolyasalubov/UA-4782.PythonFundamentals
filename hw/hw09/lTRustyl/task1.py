import pygame
import random
import sys
 
pygame.init()
 
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
W, H = screen.get_size()
pygame.display.set_caption("Guess the Number")
clock = pygame.time.Clock()
 
BG      = (30, 30, 30)
WHITE   = (255, 255, 255)
GRAY    = (150, 150, 150)
DARK    = (55, 55, 55)
GREEN   = (80, 200, 120)
RED     = (220, 80, 80)
YELLOW  = (230, 190, 60)
BLUE    = (80, 160, 230)
BTN_COL = (70, 70, 70)
 
def fs(n): return max(12, int(H * n / 900))
 
F_TITLE = pygame.font.SysFont("Arial", fs(64), bold=True)
F_BIG   = pygame.font.SysFont("Arial", fs(56), bold=True)
F_MED   = pygame.font.SysFont("Arial", fs(30))
F_SMALL = pygame.font.SysFont("Arial", fs(22))
 
def txt(surf, text, font, color, cx, cy):
    s = font.render(text, True, color)
    surf.blit(s, s.get_rect(center=(cx, cy)))
 
def box(surf, color, x, y, w, h, r=8):
    pygame.draw.rect(surf, color, (x, y, w, h), border_radius=r)
 
MAX_TRIES = 10
 
def new_game():
    return {
        "secret": random.randint(1, 100),
        "tries": 0,
        "input": "",
        "msg": "Type a number and press Enter",
        "msg_color": GRAY,
        "history": [],
        "state": "playing",
    }
 
g = new_game()
tick = 0
ROW_H = fs(38)
HIST_TOP = int(H * 0.32)
INPUT_Y  = int(H * 0.67)
BTN_Y    = int(H * 0.77)
MSG_Y    = int(H * 0.87)
 
INPUT_W, INPUT_H = 220, fs(62)
BTN_W, BTN_H    = 240, fs(52)
 
cx = W // 2
 
btn_guess_rect    = pygame.Rect(cx - BTN_W//2, BTN_Y,          BTN_W, BTN_H)
btn_restart_rect  = pygame.Rect(cx - BTN_W//2, int(H * 0.72),  BTN_W, BTN_H)
 
while True:
    clock.tick(60)
    tick += 1
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit(); sys.exit()
 
            if g["state"] == "playing":
                if event.key == pygame.K_BACKSPACE:
                    g["input"] = g["input"][:-1]
                elif event.key == pygame.K_RETURN:
                    raw = g["input"].strip()
                    if raw.isdigit():
                        n = int(raw)
                        if 1 <= n <= 100:
                            g["tries"] += 1
                            g["input"] = ""
                            if n == g["secret"]:
                                g["state"] = "won"
                                g["msg"] = f"Correct! The number was {g['secret']}."
                                g["msg_color"] = GREEN
                                g["history"].append((n, "Correct!", GREEN))
                            elif g["tries"] >= MAX_TRIES:
                                g["state"] = "lost"
                                g["msg"] = f"Game over! The number was {g['secret']}."
                                g["msg_color"] = RED
                                g["history"].append((n, "Too high" if n > g["secret"] else "Too low", RED))
                            else:
                                left = MAX_TRIES - g["tries"]
                                if n > g["secret"]:
                                    g["msg"] = f"Too high!  {left} {'try' if left==1 else 'tries'} left."
                                    g["msg_color"] = YELLOW
                                    g["history"].append((n, "Too high", YELLOW))
                                else:
                                    g["msg"] = f"Too low!   {left} {'try' if left==1 else 'tries'} left."
                                    g["msg_color"] = BLUE
                                    g["history"].append((n, "Too low", BLUE))
                        else:
                            g["msg"] = "Please enter a number between 1 and 100."
                            g["msg_color"] = YELLOW
                    else:
                        g["msg"] = "Numbers only!"
                        g["msg_color"] = YELLOW
                elif event.unicode.isdigit() and len(g["input"]) < 3:
                    g["input"] += event.unicode
            else:
                if event.key == pygame.K_RETURN:
                    g = new_game()
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if g["state"] == "playing" and btn_guess_rect.collidepoint(mx, my):
                pygame.event.post(pygame.event.Event(pygame.KEYDOWN,
                    key=pygame.K_RETURN, mod=0, unicode='\r'))
            elif g["state"] != "playing" and btn_restart_rect.collidepoint(mx, my):
                g = new_game()
 
    screen.fill(BG)
 
    txt(screen, "Guess the Number", F_TITLE, WHITE, cx, int(H * 0.08))
    txt(screen, "Range: 1 – 100   |   10 tries", F_SMALL, GRAY, cx, int(H * 0.15))
 
    dot_r = fs(11)
    spacing = dot_r * 3
    total_w = MAX_TRIES * spacing
    dx0 = cx - total_w // 2 + spacing // 2
    dy  = int(H * 0.22)
    for i in range(MAX_TRIES):
        dx = dx0 + i * spacing
        if i < g["tries"]:
            fill = GREEN if (g["state"] == "won" and i == g["tries"]-1) \
                   else RED if (g["state"] == "lost" and i == g["tries"]-1) \
                   else (100, 100, 100)
        else:
            fill = DARK
        pygame.draw.circle(screen, fill, (dx, dy), dot_r)
        pygame.draw.circle(screen, GRAY,  (dx, dy), dot_r, 1)
 
    txt(screen, "— history —", F_SMALL, GRAY, cx, HIST_TOP - fs(40))
    hist = g["history"][-5:]
    for i in range(5):
        ry = HIST_TOP + i * ROW_H
        if i < len(hist):
            gv, lbl, col = hist[i]
            box(screen, DARK, cx - 180, ry - ROW_H//2 + 4, 360, ROW_H - 6, r=6)
            txt(screen, f"{gv:>3}  —  {lbl}", F_SMALL, col, cx, ry)
        else:
            box(screen, (38, 38, 38), cx - 180, ry - ROW_H//2 + 4, 360, ROW_H - 6, r=6)
 
    if g["state"] == "playing":
        # Input box
        ix = cx - INPUT_W // 2
        box(screen, (50, 50, 50), ix, INPUT_Y, INPUT_W, INPUT_H, r=10)
        pygame.draw.rect(screen, GRAY, (ix, INPUT_Y, INPUT_W, INPUT_H), 2, border_radius=10)
        cursor = "|" if (tick // 30) % 2 == 0 else " "
        txt(screen, g["input"] + cursor, F_BIG, WHITE, cx, INPUT_Y + INPUT_H // 2)
 
        hover = btn_guess_rect.collidepoint(pygame.mouse.get_pos())
        box(screen, (95, 95, 95) if hover else BTN_COL,
            btn_guess_rect.x, btn_guess_rect.y, BTN_W, BTN_H, r=10)
        txt(screen, "GUESS  (Enter)", F_MED, WHITE, cx, BTN_Y + BTN_H // 2)
 
        txt(screen, g["msg"], F_MED, g["msg_color"], cx, MSG_Y)
 
    else:
        result = "You won!" if g["state"] == "won" else "Game over!"
        result_col = GREEN if g["state"] == "won" else RED
        txt(screen, result,   F_BIG, result_col, cx, int(H * 0.63))
        txt(screen, g["msg"], F_MED, g["msg_color"], cx, int(H * 0.63) + fs(60))
 
        hover2 = btn_restart_rect.collidepoint(pygame.mouse.get_pos())
        box(screen, (95, 95, 95) if hover2 else BTN_COL,
            btn_restart_rect.x, btn_restart_rect.y, BTN_W, BTN_H, r=10)
        txt(screen, "Play Again  (Enter)", F_MED, WHITE, cx, int(H * 0.72) + BTN_H // 2)
 
    txt(screen, "ESC to quit", F_SMALL, (70, 70, 70), cx, H - fs(24))
 
    pygame.display.flip()
 
