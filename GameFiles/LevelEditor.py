import pygame
import csv
import os


pygame.init()



clock = pygame.time.Clock()
FPS = 60


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.isPressed = False

    def draw(self):
        action = False
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.isPressed:
                self.isPressed = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.isPressed = False
        

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


screen_width = 640
screen_height = 480
boundary = 250

screen = pygame.display.set_mode((screen_width, screen_height + boundary))



# some colors

PURPLE = (255, 0, 255)
BLUE = (0, 0, 240)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0 ,0, 0)
font = pygame.font.SysFont('Futura', 30)



# image variables

ROWS = 10
COLS_MAX = 1300
TILE_SIZE = screen_height // ROWS
current_level = 1


level = []
for row in range(ROWS):
    row = [-1] * COLS_MAX
    level.append(row)

# create the ground
for tile in range(0, COLS_MAX):
    level[ROWS - 1][tile] = 2

scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1



# image loading

background = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'background_image.jpg')).convert_alpha()
player = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'player.png')).convert_alpha()
player = pygame.transform.scale(player, (TILE_SIZE, TILE_SIZE))
coin = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'coin.png')).convert_alpha()
coin = pygame.transform.scale(coin, (TILE_SIZE, TILE_SIZE))
bug = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'bug.png')).convert_alpha()
bug = pygame.transform.scale(bug, (TILE_SIZE, TILE_SIZE))

# floor and platforms
floor = pygame.Surface((TILE_SIZE, TILE_SIZE))
floor.fill((255,0,0))

platform = pygame.Surface((TILE_SIZE, TILE_SIZE))
platform.fill((255,255,0))

end = pygame.Surface((TILE_SIZE, TILE_SIZE))
end.fill(PURPLE)

# save button
save = pygame.Surface((3 * TILE_SIZE, TILE_SIZE / 2))
save.fill(GREEN)
save_button = Button((screen_width // 2) - 75, screen_height + boundary - 40, save)

# store image tiles in list
img_list = []


img_list.append(coin)
img_list.append(bug)
img_list.append(floor)
img_list.append(platform)
img_list.append(end)


tile_list = []
for i in range(len(img_list)):
    tile = Button(100 * i + 100, screen_width - 50, img_list[i])
    tile_list.append(tile)

def draw_background():

    screen.fill(BLUE)
    width = background.get_width()

    for i in range(100):
     screen.blit(background, ((i * width) - scroll, 0))



def draw_grid():

    for i in range(COLS_MAX + 1):
        pygame.draw.line(screen, WHITE, (i*TILE_SIZE - scroll, 0), (i*TILE_SIZE - scroll, screen_height))

    for i in range(ROWS + 1):
        pygame.draw.line(screen, WHITE, (0, i*TILE_SIZE), (screen_width, i*TILE_SIZE))


def draw_level():
    for y, row in enumerate(level):
        for x, tile in enumerate(row):
            if tile >= 0:
                screen.blit(img_list[tile], (x * TILE_SIZE - scroll, y * TILE_SIZE))

def draw_text(text, font, col, x, y):
    image = font.render(text, True, col)
    screen.blit(image, (x,y))



pygame.display.set_caption("Level Editor")

tile = 0

while True:

    clock.tick(FPS)

    # draw background image

    draw_background()
    draw_grid()
    draw_level()
    draw_text(f"Level: {current_level}", font, WHITE, screen_width - 100, screen_height + boundary - 40)

    # saving & load data for the level
    if save_button.draw():
         with open(f"level_{current_level}.csv", "w", newline='') as csv_file:
             writer = csv.writer(csv_file, delimiter = ',')
             for row in level:
                 writer.writerow(row)

    draw_text(f"SAVE", font, BLACK, screen_width // 2 - 29, screen_height + boundary - 37)

    

    count = 0
    for count, i in enumerate(tile_list):
        if i.draw():
            tile = count

    pygame.draw.rect(screen, WHITE, tile_list[tile].rect, 3)



    # scroll map

    if scroll_left == True and scroll > 0:
        scroll -= 10 * scroll_speed



    if scroll_right == True and scroll < (COLS_MAX * TILE_SIZE) - screen_width:
        scroll += 10 * scroll_speed


    # add tiles to the screen w/ mouse click
    mouse_pos = pygame.mouse.get_pos()
    x = (mouse_pos[0] + scroll) // TILE_SIZE
    y = (mouse_pos[1]) // TILE_SIZE

    # check boundaries of level window
    if mouse_pos[0] < screen_width and mouse_pos[1] < screen_height:

        if pygame.mouse.get_pressed()[0] == 1:
            if level[y][x] != tile:
                level[y][x] = tile

        if pygame.mouse.get_pressed()[2] == 1:
            level[y][x] = -1


    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and current_level < 3:
                current_level += 1

            if event.key == pygame.K_DOWN and current_level > 1:
                current_level -= 1

            if event.key == pygame.K_LEFT:
                scroll_left = True

            if event.key == pygame.K_RIGHT:
                scroll_right = True

            if event.key == pygame.K_LSHIFT:
                scroll_speed = 5



        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                scroll_left = False

            if event.key == pygame.K_RIGHT:
                scroll_right = False

            if event.key == pygame.K_LSHIFT:
                scroll_speed = 1





        



    



    pygame.display.update()


