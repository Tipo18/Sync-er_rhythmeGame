import pygame

pygame.init()

# init screen
WIDTH, HEIGHT = 1500, 1000
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
display_active = False
Pause = False

framecount = 0
disque_arr = []
first_line_hg = 650 + 45 + 65
second_line_hg = first_line_hg + 125
only_line_width = 113

clock = pygame.time.Clock()

def draw_text(text, font, color, surface, x, y):
    """Helper function to draw text on the screen."""
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)


class Disque(pygame.sprite.Sprite):
    def __init__(self, line, speed):
        super().__init__()  # Initialize the Sprite base class
        self.image = pygame.Surface((70, 70), pygame.SRCALPHA)  # Transparent surface
        pygame.draw.circle(self.image, (255, 255, 255), (35, 35), 35)  # Draw circle
        self.rect = self.image.get_rect()  # Get rect for positioning
        self.rect.y = first_line_hg-35 if line == 1 else second_line_hg-35
        self.rect.x = 1465
        self.speed = speed

    def update(self):
        """Update the object's position."""
        self.rect.x -= self.speed  # Move left by speed

all_disques = pygame.sprite.Group()

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
        # Active game Box
        pygame.draw.rect(screen, WHITE, (0, 650, 1500, 350), width=6, border_radius=35)
        # White bar
        pygame.draw.rect(screen, WHITE, (0, first_line_hg-1, 1500, 3)) # -1 to have the middle of correct shift due to line width
        pygame.draw.rect(screen, WHITE, (0, second_line_hg-1, 1500, 3))
        pygame.draw.rect(screen, WHITE, (only_line_width-3, 650, 3, 350)) # +/- to correct shift due to width
        pygame.draw.rect(screen, WHITE, (only_line_width+1, 650, 3, 350))
        # Target circle
        pygame.draw.circle(screen, WHITE, (only_line_width,first_line_hg), 45, width=4)
        pygame.draw.circle(screen, WHITE, (only_line_width,second_line_hg ), 45, width=4)

        # create disc
        framecount += 1
        if framecount % 100 == 0:
            all_disques.add(Disque(1,10))

        # Update all sprites in the group
        all_disques.update()
        all_disques.draw(screen)
        pygame.display.flip()


    clock.tick(60)
pygame.quit()