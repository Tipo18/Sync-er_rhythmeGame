import pygame
import random

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
first_line_hg = 650 + 45 + 65
second_line_hg = first_line_hg + 125
only_line_width = 175

missed_disque = 0
validated_disque = 0
points = 0

def draw_text(text, font, color, surface, x, y, align):
    text_obj = font.render(text, True, color)
    if align == "center":
        text_rect = text_obj.get_rect(center=(x, y))
    elif align == "left":
        text_rect = text_obj.get_rect(topleft = (x, y))
    surface.blit(text_obj, text_rect)


class Disque(pygame.sprite.Sprite):
    def __init__(self, line, speed):
        super().__init__()  # Initialize the Sprite base class
        self.image = pygame.Surface((70, 70), pygame.SRCALPHA)  # Transparent surface
        pygame.draw.circle(self.image, (255, 255, 255), (35, 35), 35)  # Draw circle
        self.rect = self.image.get_rect()  # Get rect for positioning
        self.rect.y = first_line_hg-35 if line == 1 else second_line_hg-35
        self.rect.x = 1500
        self.speed = speed

    def update(self):
        """Update the object's position."""
        global missed_disque
        self.rect.x -= self.speed  # Move left by speed
        if self.rect.x < 0:  # Check if the object has moved off the screen
            self.kill()
            missed_disque += 1 

all_disques = pygame.sprite.Group()


def find_closest_disque(line):
    # Filter disques based on the line value
    filtered_disques = [
        disque for disque in all_disques 
        if ((disque.rect.y == first_line_hg - 35 and line == 1) or
            (disque.rect.y == second_line_hg - 35 and line == 2)) 
        and disque.rect.x + 35 > only_line_width - 80          # subjective to be able to valide even if a bit after the line
    ]
    if not filtered_disques:
        return None  # No matching disques found
    
    # Find the instance with the rect.x value closest to 0
    closest_inst = min(filtered_disques, key=lambda x: abs(x.rect.x))
    
    return closest_inst

def point_logic(object):
    if object is not None:
        global validated_disque
        global points
        dist = object.rect.x + 35 - only_line_width
        print(dist)
        if dist < 80:
            object.kill()
            validated_disque += 1
            if abs(dist) <= 3:
                points += 100
            elif abs(dist) <= 20:
                points += 15
            else:
                points += 5
            
clock = pygame.time.Clock()


# Start game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                running = False
            if event.key == pygame.K_RETURN:
                menue = False
            if event.key == pygame.K_p and menue == False:
                Pause = not Pause
            if event.key == pygame.K_a and menue == False and Pause == False:
                disk1 = find_closest_disque(1)
                point_logic(disk1)
            if event.key == pygame.K_z and menue == False and Pause == False:
                disk2 = find_closest_disque(2)
                point_logic(disk2)

    if menue:
        screen.fill(WHITE)
        draw_text("Main Menu", font, BLACK, screen, WIDTH // 2, HEIGHT // 3, "center")
        draw_text("Press ENTER to Start", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2, "center")
        draw_text("Press P to Resume", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 40, "center")
        draw_text("Press M to Quit", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 80, "center")
        pygame.display.flip()
    elif Pause:
        screen.fill(WHITE)
        draw_text("Pause", font, BLACK, screen, WIDTH // 2, HEIGHT // 3, "center")
        draw_text("Press P to Resume", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2, "center")
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

        # Texte
        draw_text(f"fps: {int(clock.get_fps())}", small_font, WHITE, screen, 20, HEIGHT // 8, "left")
        draw_text(f"missed disques: {missed_disque}", small_font, WHITE, screen, 20, HEIGHT // 8 + 40, "left")
        draw_text(f"validated disques: {validated_disque}", small_font, WHITE, screen, 20, HEIGHT // 8 + 80, "left")
        draw_text(f"points: {points}", font, WHITE, screen, 20, HEIGHT // 2, "left")


        # create disc
        framecount += 1
        if framecount % 50 == 0:
            all_disques.add(Disque(random.randint(1,2),4))

        # Update all sprites in the group
        all_disques.update()
        all_disques.draw(screen)
        pygame.display.flip()

        if validated_disque >= 35 or missed_disque >= 3:
            running = False


    clock.tick(60)
pygame.quit()