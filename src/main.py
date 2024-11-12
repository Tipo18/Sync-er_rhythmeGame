import pygame

pygame.init()

# init screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Rhythme Game")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# fonts
font = pygame.font.SysFont('Arial', 36)
small_font = pygame.font.SysFont('Arial', 24)

# Game States
running = True
menue = True
Pause = False

clock = pygame.time.Clock()

def draw_text(text, font, color, surface, x, y):
    """Helper function to draw text on the screen."""
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# Start game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_RETURN:
                menue = False
            if event.key == pygame.K_p and menue == False:
                Pause = not Pause

    if menue:
        screen.fill(WHITE)
        draw_text("Main Menu", font, BLACK, screen, WIDTH // 2, HEIGHT // 3)
        draw_text("Press ENTER to Start", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
        draw_text("Press P to Resume", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 40)
        draw_text("Press Q to Quit", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 80)
        pygame.display.flip()
    elif Pause:
        screen.fill(WHITE)
        draw_text("Pause", font, BLACK, screen, WIDTH // 2, HEIGHT // 3)
        draw_text("Press P to Resume", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()
    else:
        screen.fill(BLACK)
        pygame.display.flip()

    clock.tick(60)
pygame.quit()