import random
import os
#import csv

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
        self.running = True
        self.menu = True
        self.level_lauching = False
        self.pause = False
        self.end_menu = False
        self.player_name = ["-"] * 6
        self.num_key = 0
        self.active_level = None

    def link_active_level(self, active_level):
        self.active_level = active_level

class Active_Level:
    def __init__(self, game_object):
        self.game_object = game_object
        self.active_player = None
        self.active_disk = None
        self.speed = 4
        self.validated_disk = 0
        self.perfect = 0
        self.great = 0
        self.ok = 0
        self.fault = 0
        self.point = 0
        self.nb_click = 0
        self.missed_clicked = 0
        self.active_streak = 0
        self.longest_streak = 0
        self.active_grt_streak = 0
        self.longest_grt_streak = 0
    
    def speed_incr(self):
        self.speed += 1
    
    def validated_disk_incr(self):
        self.validated_disk += 1
        if self.validated_disk % 8 == 0:
            self.speed_incr()

    def perfect_incr(self):
        self.perfect += 1
        self.point += 100
        self.streak_incr()
        self.grt_streak_incr()

    def great_incr(self):
        self.great += 1
        self.point += 20
        self.streak_incr()
        self.grt_streak_incr()

    def ok_incr(self):
        self.ok += 1
        self.point += 5
        self.streak_incr()
        self.active_grt_streat = 0

    def fault_incr(self):
        self.fault += 1
        if self.fault == 3:
            game_object.end_menu = True


    def nb_click_incr(self):
        self.nb_click += 1

    def missed_clicked_incr(self):
        self.missed_clicked += 1
        self.active_streak = 0
        self.active_grt_streak = 0

    def streak_incr(self):
        self.active_streak += 1
        if self.active_streak > self.longest_streak:
            self.longest_streak = self.active_streak

    def grt_streak_incr(self):
        self.active_grt_streak += 1
        if self.active_grt_streak > self.longest_grt_streak:
            self.longest_grt_streak = self.active_grt_streak


    def link_player(self, player):
        self.active_player = player
        self.high_score = 0

    def link_disks(self):
        self.active_disk = pygame.sprite.Group()

class Player():
    def __init__(self, name):
        self.name = name

class Disque(pygame.sprite.Sprite):
    def __init__(self, line, speed, active_level):
        super().__init__()  # Initialize the Sprite base class
        self.image = pygame.Surface((70, 70), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (35, 35), 35) 
        self.rect = self.image.get_rect()
        self.rect.y = horizontal_line_1-35 if line == 1 else horizontal_line_2-35
        self.rect.x = 1500
        self.speed = speed
        self.active_level = active_level

    def update(self):
        self.rect.x -= self.speed 
        if self.rect.x < 0:
            self.kill()
            if hasattr(self, 'active_level') and self.active_level is not None:
                self.active_level.fault_incr()
                self.active_level.active_streak = 0
                self.active_level.active_grt_streak = 0


# Screen
# Menu screen function
def menu_screen(game_object):
    # key listening
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_object.level_lauching = True
            elif event.key == pygame.K_m:
                game_object.running = False

    # display
    screen.fill(WHITE)
    draw_text("Main Menu", font, BLACK, screen, WIDTH // 2, HEIGHT // 3, "center")
    draw_text("A - Q to play", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 3 + 80, "center")
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
    draw_text("ENTER to launch the game", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 120, "center")
    pygame.display.flip()

def pause_screen(game_object):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                game_object.pause = False
            elif event.key == pygame.K_m:
                game_object.running = False

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
                game_object.running = False
            elif event.key == pygame.K_a:
                game_object.active_level.nb_click += 1
                cl_disk1 = find_closest_disque(game_object, 1)
                action_on_disk(game_object, cl_disk1)
            elif event.key == pygame.K_q:
                game_object.active_level.nb_click += 1
                cl_disk2 = find_closest_disque(game_object, 2)
                action_on_disk(game_object, cl_disk2)

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
    draw_text(f"fps: {int(clock.get_fps())}", small_font, WHITE, screen, 20, 10, "left")
    draw_text(f"player: {game_object.active_level.active_player.name}", small_font, WHITE, screen, 20, 50, "left")
    draw_text(f"actual speed: {game_object.active_level.speed}", small_font, WHITE, screen, 20, 80, "left")
    draw_text(f"fault: {game_object.active_level.fault}", small_font, WHITE, screen, 20, 110, "left")
    draw_text(f"ok: {game_object.active_level.ok}", small_font, WHITE, screen, 20, 140, "left")
    draw_text(f"great: {game_object.active_level.great}", small_font, WHITE, screen, 20, 170,"left")   
    draw_text(f"perfect: {game_object.active_level.perfect}", small_font, WHITE, screen, 20, 200, "left")   
    draw_text(f"points: {game_object.active_level.point}", small_font, WHITE, screen, 20, 230, "left")   
    draw_text(f"active_streak: {game_object.active_level.active_streak}", small_font, WHITE, screen, 20, 260, "left")   
    draw_text(f"active_grt_steak: {game_object.active_level.active_grt_streak}", small_font, WHITE, screen, 20, 290, "left")

    # create disc
    global framecount
    framecount += 1
    spawning_rate = int(280 / game_object.active_level.speed)

    if framecount % spawning_rate == 0:
        game_object.active_level.active_disk.add(Disque(random.randint(1,2), game_object.active_level.speed, game_object.active_level))
        
    game_object.active_level.active_disk.update()
    game_object.active_level.active_disk.draw(screen)

    pygame.display.flip()

def end_menu_screen(game_object):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                game_object.running = False
            elif event.key == pygame.K_m:
                game_object.menu = True
                game_object.player_name = ["-"] * 6
                game_object.end_menu = False
            elif event.key == pygame.K_y:
                game_object.end_menu = False
                game_class_init(game_object)

    screen.fill(WHITE)
    draw_text(f"Well play {game_object.active_level.active_player.name}" , font, BLACK, screen, WIDTH // 2, HEIGHT // 3, "center")
    draw_text(f"Final score : {game_object.active_level.point}", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2, "center")

    draw_text("Do you want to play again ? (y/n)", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 120, "center")
    draw_text("Go back to menue M", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 160, "center")

    pygame.display.flip()

# Game logic function
def game_class_init(game_object):
    player_name = "".join(char for char in game_object.player_name if char != "-").strip()
    player_object = Player(player_name)
    active_level_object = Active_Level(game_object)

    active_level_object.link_player(player_object)
    active_level_object.link_disks()
    game_object.link_active_level(active_level_object)  

def find_closest_disque(game_object, line):
    # Filter disques based on the line value
    filtered_disk = [
        disk for disk in game_object.active_level.active_disk 
        if ((disk.rect.y == horizontal_line_1 - 35 and line == 1) or
            (disk.rect.y == horizontal_line_2 - 35 and line == 2)) 
        and disk.rect.x + 35 > vertical_line - 80          # marge to be able to valide even if a bit after the line
    ]
    if not filtered_disk:
        game_object.active_level.missed_clicked_incr()
        return None  
    
    closest_disk = min(filtered_disk, key=lambda x: abs(x.rect.x))
    return closest_disk

def action_on_disk(game_object, disk_object):
    if disk_object is not None:
        dist = disk_object.rect.x + 35 - vertical_line
        if dist < 80:
            disk_object.kill()
            game_object.active_level.validated_disk_incr()
            if abs(dist) <= 3:
                game_object.active_level.perfect_incr()
            elif abs(dist) <= 20:
                game_object.active_level.great_incr()
            else:
                game_object.active_level.ok_incr()
        else:
            game_object.active_level.missed_clicked_incr()
    else:
        game_object.active_level.missed_clicked_incr()


# csv logic

def csv_init():
    print("")

def csv_end():
    print("")


# Game loop
fps = 60
clock = pygame.time.Clock()
game_object = Game()

while game_object.running:
    clock.tick(fps)
    if game_object.menu:
        if not game_object.level_lauching:
            menu_screen(game_object)
        else:
            level_lauching_screen(game_object)
    elif game_object.pause:
        pause_screen(game_object)
    else:
        if not game_object.end_menu:
            level_active_screen(game_object)
        else:
            end_menu_screen(game_object)