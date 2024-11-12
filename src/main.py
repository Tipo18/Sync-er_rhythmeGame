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

    screen.fill(WHITE)
    #pygame.display.update()
    draw_text("Press Q to ", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()