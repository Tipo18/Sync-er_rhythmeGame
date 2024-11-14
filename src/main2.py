import random
import pygame

# Game initialisation
pygame.init()
WIDTH, HEIGHT = 1500, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Rhythme Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

font = pygame.font.SysFont('Arial', 36)
small_font = pygame.font.SysFont('Arial', 24)

framecount = 0
clock = pygame.time.Clock()
horizontal_line_1 = 650 + 45 + 65
horizontal_line_2 = horizontal_line_1 + 125
vertical_line = 175

# Help to draw text on the screen, align : "center" or "left" to choose the text alignement
def draw_text(text, font, color, surface, x, y, align):
    text_obj = font.render(text, True, color)
    if align == "center":
        text_rect = text_obj.get_rect(center=(x, y))
    elif align == "left":
        text_rect = text_obj.get_rect(topleft = (x, y))
    surface.blit(text_obj, text_rect)


# Classe
class Game():
    def __init__(self):
        self.runnig = True
        self.menu = True
        self.level_lauching = False
        self.pause = False
        self.player_name = ["-"] * 6
        self.num_key = 0
        self.active_level = None

    def link_active_level(self, active_level):
        self.active_level = active_level

class Active_Level:
    def __init__(self):
        self.active_player = None
        self.active_disk = None
        self.perfect = 0
        self.great = 0
        self.ok = 0
        self.fault = 0

    def link_player(self, player):
        self.active_player = player

    def link_disks(self):
        self.active_disk = pygame.sprite.Group()

class Player():
    def __init__(self, name):
        self.name = name

class Disque(pygame.sprite.Sprite):
    def __init__(self, line):
        super().__init__()  # Initialize the Sprite base class
        self.image = pygame.Surface((70, 70), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (35, 35), 35) 
        self.rect = self.image.get_rect()
        self.rect.y = horizontal_line_1-35 if line == 1 else horizontal_line_2-35
        self.rect.x = 1500
        self.speed = 6

    def update(self):
        self.rect.x -= self.speed 
        if self.rect.x < 0:
            self.kill()


# Screen
# Menu screen function
def menu_screen(game_object):
    # key listening
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_object.level_lauching = True
            elif event.key == pygame.K_m:
                game_object.runnig = False

    # display
    screen.fill(WHITE)
    draw_text("Main Menu", font, BLACK, screen, WIDTH // 2, HEIGHT // 3, "center")
    draw_text("Press ENTER to Start", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2, "center")
    draw_text("Press P to Resume", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 40, "center")
    draw_text("Press M to Quit", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 80, "center")
    pygame.display.flip()

def level_lauching_screen(game_object):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_object.player_name[0] != "-":
                    game_object.level_lauching = False
                    game_object.menu = False
                    game_class_init(game_object)
            elif event.key == pygame.K_BACKSPACE:
                game_object.player_name[game_object.num_key] = "-"
                if game_object.num_key > 0:
                    game_object.num_key -= 1
            else:
                game_object.player_name[game_object.num_key] = event.unicode
                if game_object.num_key < 5:
                    game_object.num_key += 1

    screen.fill(WHITE)
    draw_text("Enter your name (max 6 chars):", font, BLACK, screen, WIDTH // 2, HEIGHT // 3, "center")
    display_text = "".join(game_object.player_name).strip()
    draw_text(display_text, font, BLACK, screen, WIDTH // 2, HEIGHT // 2, "center")
    pygame.display.flip()

def pause_screen(game_object):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                game_object.pause = False
            elif event.key == pygame.K_m:
                game_object.runnig = False

    screen.fill(WHITE)
    draw_text("Pause", font, BLACK, screen, WIDTH // 2, HEIGHT // 3, "center")
    draw_text("Press P to Resume", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2, "center")
    draw_text("Press M to Quit", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 40, "center")
    pygame.display.flip()

def level_active_screen(game_object):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                game_object.pause = True
            elif event.key == pygame.K_m:
                game_object.runnig = False

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (0, 650, 1500, 350), width=6, border_radius=35)
    # White bar
    pygame.draw.rect(screen, WHITE, (0, horizontal_line_1-1, 1500, 3)) # -1 to have the middle of correct shift due to line width
    pygame.draw.rect(screen, WHITE, (0, horizontal_line_2-1, 1500, 3))
    pygame.draw.rect(screen, WHITE, (vertical_line-3, 650, 3, 350)) # +/- to correct shift due to width
    pygame.draw.rect(screen, WHITE, (vertical_line+1, 650, 3, 350))
    # Target circle
    pygame.draw.circle(screen, WHITE, (vertical_line,horizontal_line_1), 45, width=4)
    pygame.draw.circle(screen, WHITE, (vertical_line,horizontal_line_2 ), 45, width=4)

    # Text
    draw_text(f"fps: {int(clock.get_fps())}", small_font, WHITE, screen, 20, HEIGHT // 8, "left")
    draw_text(f"player: {game_object.active_level.active_player.name}", small_font, WHITE, screen, 20, HEIGHT // 8 + 40, "left")

    # create disc
    global framecount
    framecount += 1

    if framecount % 70 == 0:
        game_object.active_level.active_disk.add(Disque(random.randint(1,2)))
        
    game_object.active_level.active_disk.update()
    game_object.active_level.active_disk.draw(screen)

    pygame.display.flip()


# Game logic function

def game_class_init(game_object):
    player_name = "".join(char for char in game_object.player_name if char != "-").strip()
    player_object = Player(player_name)
    active_level_object = Active_Level()

    active_level_object.link_player(player_object)
    active_level_object.link_disks()
    game_object.link_active_level(active_level_object)  

fps = 60  # Target frame rate
clock = pygame.time.Clock()

# Game loop
game_object = Game()

while game_object.runnig:
    clock.tick(fps)
    if game_object.menu:
        if not game_object.level_lauching:
            menu_screen(game_object)
        else:
            level_lauching_screen(game_object)
    elif game_object.pause:
        pause_screen(game_object)
    else:
        level_active_screen(game_object)


