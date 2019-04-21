import pygame


class Trash:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def draw(self):
        if self.type == "glass":
            coller = BLACK
        else:
            coller = GREEN_MATRIX
        pygame.draw.circle(screen, coller, (int(screen_width // 4 + self.x * side_x + side_x // 2),
                                           int(screen_height // 10 + self.y * side_y + side_y // 2)), side_y // 4)


def restartBut():
    levels[0] = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 11, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    levels[1] = [[13, 13, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 13, 13, 13, 0, 0, 15, 0],
               [0, 13, 0, 0, 0, 13, 0, 13, 0, 0],
               [0, 13, 13, 13, 0, 13, 0, 13, 0, 13],
               [0, 0, 0, 13, 0, 0, 0, 0, 0, 0],
               [0, 13, 0, 13, 0, 13, 13, 0, 13, 0],
               [0, 13, 0, 0, 0, 13, 13, 0, 13, 0],
               [11, 13, 0, 13, 0, 13, 0, 0, 0, 0],
               [13, 13, 0, 13, 0, 13, 0, 13, 0, 0],
               [13, 13, 14, 13, 0, 0, 0, 13, 0, 10]]


pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

changeID = 0

menuMusic = pygame.mixer.Sound('res/rassvet.ogg')

screen_height = 800
screen_width = 1000

side_x = (screen_width // 2) // 10
side_y = (screen_height * 8 // 10) // 10

f1 = pygame.font.Font(None, 36)
f2 = pygame.font.Font(None, 70)

size = [screen_width, screen_height]
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

pygame.display.set_caption("IN PROGRESS")

up_red = pygame.image.load('res/up_red.png').convert_alpha()
up_red = pygame.transform.scale(up_red, (side_x, side_y))

down_red = pygame.image.load('res/down_red.png')
down_red = pygame.transform.scale(down_red, (side_x, side_y))

left_red = pygame.image.load('res/left_red.png')
left_red = pygame.transform.scale(left_red, (side_x, side_y))

right_red = pygame.image.load('res/right_red.png')
right_red = pygame.transform.scale(right_red, (side_x, side_y))

up_blue = pygame.image.load('res/up_blue.png').convert_alpha()
up_blue = pygame.transform.scale(up_blue, (side_x, side_y))

down_blue = pygame.image.load('res/down_blue.png')
down_blue = pygame.transform.scale(down_blue, (side_x, side_y))

left_blue = pygame.image.load('res/left_blue.png')
left_blue = pygame.transform.scale(left_blue, (side_x, side_y))

right_blue = pygame.image.load('res/right_blue.png')
right_blue = pygame.transform.scale(right_blue, (side_x, side_y))

restartPict = pygame.image.load('res/restart.png')
restartPict = pygame.transform.scale(restartPict, (side_x, side_y))

startPict = pygame.image.load('res/start.png')
startPict = pygame.transform.scale(startPict, (side_x, side_y))

pausePict = pygame.image.load('res/pause.png')
pausePict = pygame.transform.scale(pausePict, (side_x, side_y))

menuDownLayer = pygame.image.load('res/svalkaPina.png')
menuDownLayer = pygame.transform.scale(menuDownLayer, (screen_width, screen_height))

menuUpperLayer = pygame.image.load('res/stulk.png')
menuUpperLayer = pygame.transform.scale(menuUpperLayer, (screen_width, screen_height))

chel = pygame.image.load('res/chel.png')
chel = pygame.transform.scale(chel, (screen_width//5, screen_height//2))

final = pygame.image.load('res/final.png')
final = pygame.transform.scale(final, (screen_width, screen_height))

picts = [up_red, right_red, down_red, left_red, up_blue, right_blue, down_blue, left_blue]
pictsPos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
isDragIsDrawing = False
dragIndex = 0

level = 0
levelIsDone = False
levelsIsDone = [False, False]

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [32, 58, 39]
GREEN_MATRIX = [0, 128, 0]
GRAY = [128, 128, 128]
RED = [255, 0, 0]
YELLOW = [247, 242, 26]
BLUE = [135, 206, 250]

trashCreatingTimer = 0

first_level = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 11, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

second_level = [[13, 13, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 13, 13, 13, 0, 0, 15, 0],
               [0, 13, 0, 0, 0, 13, 0, 13, 0, 0],
               [0, 13, 13, 13, 0, 13, 0, 13, 0, 13],
               [0, 0, 0, 13, 0, 0, 0, 0, 0, 0],
               [0, 13, 0, 13, 0, 13, 13, 0, 13, 0],
               [0, 13, 0, 0, 0, 13, 13, 0, 13, 0],
               [11, 13, 0, 13, 0, 13, 0, 0, 0, 0],
               [13, 13, 0, 13, 0, 13, 0, 13, 0, 0],
               [13, 13, 14, 13, 0, 0, 0, 13, 0, 10]]
# where 0 - ground 1 - road 2 - place for turret 3 - start 4 - finish 5 - turret(rocket)
levels = [first_level, second_level, first_level]
trashes = []

gameSection = 1  # -1 - menu 0 - playing 1 - first level 2 - second lvl and other and other

flag = False
pygame.mixer.music.set_volume(0.3)
menuMusic.play(-1)
while not flag:
    for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN:
            x_pos = pygame.mouse.get_pos()[0]
            y_pos = pygame.mouse.get_pos()[1]

            if (screen_width // 10 * 7.5 <= x_pos <= screen_width // 10 * 7.5 + playButton.get_width()) and (screen_height // 8 * 3 <= y_pos <= screen_height // 8 * 3 + playButton.get_height()): flag = True
            if (screen_width // 10 * 7.5 <= x_pos <= screen_width // 10 * 7.5 + exitButton.get_width()) and (screen_height // 2 <= y_pos <= screen_height // 2 + exitButton.get_height()):
                pygame.display.quit()
                pygame.quit()

    screen.blit(menuDownLayer, (0, 0))
    screen.blit(menuUpperLayer, (0, 0))

    playButton = f2.render('PLAY', 1, GREEN_MATRIX)
    screen.blit(playButton, (screen_width // 10 * 7.5, screen_height // 8 * 3))

    exitButton = f2.render('EXIT', 1, GREEN_MATRIX)
    screen.blit(exitButton, (screen_width // 10 * 7.5, screen_height // 2))
    pygame.display.flip()
    clock.tick(60)

alphaSurface = 120
flag = False
while not flag:
    screen.blit(menuDownLayer, (0, 0))
    screen.blit(menuUpperLayer, (0, 0))
    menuUpperLayer.fill((255, 255, 255, alphaSurface))
    if alphaSurface >= 5:
        alphaSurface -= 5
    else:
        flag = True
    pygame.display.flip()
    clock.tick(60)

screen.blit(chel, (screen_width // 4 * 3, screen_height // 4))
flag = False
pygame.draw.rect(screen, BLACK, ((0, screen_height//8*6), (screen_width, screen_height//4)))
pygame.draw.line(screen, GRAY, (0, screen_height//8*6),(screen_width, screen_height//8*6), 7)
pygame.draw.line(screen, GRAY, (0, screen_height-3),(screen_width, screen_height-3), 7)
pygame.draw.line(screen, GRAY, (0, screen_height//8*6),(0, screen_height), 7)
pygame.draw.line(screen, GRAY, (screen_width-3, screen_height//8*6),(screen_width-3, screen_height), 7)
t1 = f2.render('КАПРАЛ:', 1, GREEN_MATRIX)
screen.blit(t1, (screen_width//16, screen_height // 8 * 6 + 10))

t1 = f1.render('Ваша машина готова, капитан!', 1, GREEN_MATRIX)
screen.blit(t1, (screen_width//8, screen_height // 8 * 7))
pygame.display.flip()

while not flag:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            flag = True
        if i.type == pygame.MOUSEBUTTONDOWN:
            flag = True
    clock.tick(60)

screen.fill(WHITE)
flag = False
pygame.draw.rect(screen, BLACK, ((0, screen_height//8*6), (screen_width, screen_height//4)))
pygame.draw.line(screen, GRAY, (0, screen_height//8*6),(screen_width, screen_height//8*6), 7)
pygame.draw.line(screen, GRAY, (0, screen_height-3),(screen_width, screen_height-3), 7)
pygame.draw.line(screen, GRAY, (0, screen_height//8*6),(0, screen_height), 7)
pygame.draw.line(screen, GRAY, (screen_width-3, screen_height//8*6),(screen_width-3, screen_height), 7)
t1 = f2.render('ГОЛОС:', 1, GREEN_MATRIX)
screen.blit(t1, (screen_width//16, screen_height // 8 * 6 + 10))

t1 = f1.render('А теперь протестируем машину по сортировке мусора, просим!', 1, GREEN_MATRIX)
screen.blit(t1, (screen_width//8, screen_height // 8 * 7))
pygame.display.flip()
while not flag:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            flag = True
        if i.type == pygame.MOUSEBUTTONDOWN:
            flag = True
    clock.tick(60)


flag = True
while not flag:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            flag = True
        if i.type == pygame.MOUSEBUTTONDOWN:
            x_pos = pygame.mouse.get_pos()[0]
            y_pos = pygame.mouse.get_pos()[1]
            if gameSection == 0:
                if (pictsPos[10] + side_x >= x_pos >= pictsPos[10] and pictsPos[11] + side_y >= y_pos >= pictsPos[11]):
                    gameSection = level + 1
                    trashes = []
            elif gameSection >= 1:
                if (pictsPos[0] + side_x >= x_pos >= pictsPos[0] and pictsPos[1] + side_y >= y_pos >= pictsPos[
                    1] and isDragIsDrawing == False):
                    isDragIsDrawing = True
                    dragIndex = 0
                if (pictsPos[2] + side_x >= x_pos >= pictsPos[2] and pictsPos[3] + side_y >= y_pos >= pictsPos[
                    3] and isDragIsDrawing == False):
                    isDragIsDrawing = True
                    dragIndex = 1
                if (pictsPos[4] + side_x >= x_pos >= pictsPos[4] and pictsPos[5] + side_y >= y_pos >= pictsPos[
                    5] and isDragIsDrawing == False):
                    isDragIsDrawing = True
                    dragIndex = 2
                if (pictsPos[6] + side_x >= x_pos >= pictsPos[6] and pictsPos[7] + side_y >= y_pos >= pictsPos[
                    7] and isDragIsDrawing == False):
                    isDragIsDrawing = True
                    dragIndex = 3
                if (pictsPos[8] + side_x >= x_pos >= pictsPos[8] and pictsPos[9] + side_y >= y_pos >= pictsPos[9]):
                    if changeID == 0:
                        changeID = 1
                    else:
                        changeID = 0
                if (pictsPos[10] + side_x >= x_pos >= pictsPos[10] and pictsPos[11] + side_y >= y_pos >= pictsPos[11]):
                    gameSection = 0
                if(screen_width // 10 * 6 <= x_pos <= screen_width // 10 * 6 + restart.get_width()) and (screen_height//40 <= y_pos <= screen_height//40 + restart.get_height()):
                    levelIsDone = False
                    restartBut()
                if (screen_width // 10 * 8 + nextButton.get_width() >= x_pos >= screen_width // 10 * 8  and screen_height//40 +  nextButton.get_height() >= y_pos >= screen_height//40  and levelIsDone):
                    level += 1
                    levelIsDone = False
                    if level == 2:
                        flag = True

        if i.type == pygame.MOUSEBUTTONUP and isDragIsDrawing and gameSection >= 1:
            x_pos = pygame.mouse.get_pos()[0]
            y_pos = pygame.mouse.get_pos()[1]
            isDragIsDrawing = False
            xMouse = (x_pos - screen_width // 4) // side_x
            yMouse = (y_pos - screen_height // 10) // side_y
            if xMouse >= 0 and xMouse <= 9 and yMouse >= 0 and yMouse <= 9:
                if levels[level][yMouse][xMouse] != 9 and levels[level][yMouse][xMouse] != 10 and levels[level][yMouse][
                    xMouse] != 11 and levels[level][yMouse][xMouse] != 11 and levels[level][yMouse][xMouse] != 13 and levels[level][yMouse][xMouse] != 14 and levels[level][yMouse][xMouse] != 15:
                    levels[level][yMouse][xMouse] = changeID * 4 + dragIndex + 1

    screen.fill(BLUE)

    for y in range(0, 10):
        for x in range(0, 10):
            if levels[level][y][x] == 0:
                pygame.draw.rect(screen, WHITE,
                                 ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y), side_x, side_y))
            elif levels[level][y][x] == 1:
                pygame.draw.rect(screen, WHITE,
                                 ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y), side_x, side_y))
                screen.blit(up_red, ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y)))
            elif levels[level][y][x] == 2:
                pygame.draw.rect(screen, WHITE,
                                 ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y), side_x, side_y))
                screen.blit(right_red, ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y)))
            elif levels[level][y][x] == 3:
                pygame.draw.rect(screen, WHITE,
                                 ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y), side_x, side_y))
                screen.blit(down_red, ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y)))
            elif levels[level][y][x] == 4:
                pygame.draw.rect(screen, WHITE,
                                 ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y), side_x, side_y))
                screen.blit(left_red, ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y)))

            elif levels[level][y][x] == 5:
                pygame.draw.rect(screen, WHITE,
                                 ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y), side_x, side_y))
                screen.blit(up_blue, ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y)))
            elif levels[level][y][x] == 6:
                pygame.draw.rect(screen, WHITE,
                                 ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y), side_x, side_y))
                screen.blit(right_blue, ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y)))
            elif levels[level][y][x] == 7:
                pygame.draw.rect(screen, WHITE,
                                 ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y), side_x, side_y))
                screen.blit(down_blue, ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y)))
            elif levels[level][y][x] == 8:
                pygame.draw.rect(screen, WHITE,
                                 ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y), side_x, side_y))
                screen.blit(left_blue, ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y)))
            elif levels[level][y][x] == 14 or levels[level][y][x] == 15:
                pygame.draw.rect(screen, GREEN_MATRIX,
                                 ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y), side_x, side_y))
            elif levels[level][y][x] == 11 or levels[level][y][x] == 10:
                pygame.draw.rect(screen, BLACK,
                                 ((screen_width // 4 + side_x * x), (screen_height // 10 + side_y * y), side_x, side_y))

    for y in range(0, 10):
        pygame.draw.line(screen, GREEN_MATRIX, (screen_width // 4, screen_height // 10 + side_y * y),
                         (screen_width // 4 + side_x * 10, screen_height // 10 + side_y * y), 2)
        pygame.draw.line(screen, GREEN_MATRIX, (screen_width // 4 + side_x * y, screen_height // 10),
                         (screen_width // 4 + side_x * y, screen_height // 10 + side_y * 10), 2)

    if isDragIsDrawing:
        screen.blit(picts[changeID * 4 + dragIndex], (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))

    levelNumber = f1.render('Level: ' + str(level), 1, GREEN_MATRIX)
    screen.blit(levelNumber, (0, screen_height // 40))
    isDone = f1.render('Completing of level: ' + str(levelIsDone), 1, GREEN_MATRIX)
    screen.blit(isDone, (screen_width // 10 * 2, screen_height // 40))
    restart = f1.render('RESTART', 1, GREEN_MATRIX)
    screen.blit(restart, (screen_width // 10 * 6, screen_height // 40))
    nextButton = f1.render('NEXT LEVEL', 1, GREEN_MATRIX)
    if levelIsDone and level == 0:
        screen.blit(nextButton, (screen_width // 10 * 8, screen_height // 40))
    elif levelsIsDone[0] and levelsIsDone[1] and level == 1:
        levelIsDone = True
        screen.blit(nextButton, (screen_width // 10 * 8, screen_height // 40))

    if changeID == 0:
        screen.blit(up_red, (0, (screen_height // 10 * 9)))
        pictsPos[0] = 0
        pictsPos[1] = screen_height // 10 * 9
        screen.blit(right_red, ((screen_width // 10 * 2), (screen_height // 10 * 9)))
        pictsPos[2] = screen_width // 10 * 2
        pictsPos[3] = screen_height // 10 * 9
        screen.blit(down_red, ((screen_width // 10 * 4), (screen_height // 10 * 9)))
        pictsPos[4] = screen_width // 10 * 4
        pictsPos[5] = screen_height // 10 * 9
        screen.blit(left_red, ((screen_width // 10 * 6), (screen_height // 10 * 9)))
        pictsPos[6] = screen_width // 10 * 6
        pictsPos[7] = screen_height // 10 * 9
        screen.blit(restartPict, ((screen_width // 10 * 8), (screen_height // 10 * 9)))
        pictsPos[8] = screen_width // 10 * 8
        pictsPos[9] = screen_height // 10 * 9
    else:
        screen.blit(up_blue, (0, (screen_height // 10 * 9)))
        pictsPos[0] = 0
        pictsPos[1] = screen_height // 10 * 9
        screen.blit(right_blue, ((screen_width // 10 * 2), (screen_height // 10 * 9)))
        pictsPos[2] = screen_width // 10 * 2
        pictsPos[3] = screen_height // 10 * 9
        screen.blit(down_blue, ((screen_width // 10 * 4), (screen_height // 10 * 9)))
        pictsPos[4] = screen_width // 10 * 4
        pictsPos[5] = screen_height // 10 * 9
        screen.blit(left_blue, ((screen_width // 10 * 6), (screen_height // 10 * 9)))
        pictsPos[6] = screen_width // 10 * 6
        pictsPos[7] = screen_height // 10 * 9
        screen.blit(restartPict, ((screen_width // 10 * 8), (screen_height // 10 * 9)))
        pictsPos[8] = screen_width // 10 * 8
        pictsPos[9] = screen_height // 10 * 9


    if gameSection >= 1:
        screen.blit(startPict, ((screen_width // 10 * 9.3), (screen_height // 10 * 9)))
        pictsPos[10] = screen_width // 10 * 9.3
        pictsPos[11] = screen_height // 10 * 9
    elif gameSection == 0:
        screen.blit(pausePict, ((screen_width // 10 * 9.3), (screen_height // 10 * 9)))
        pictsPos[10] = screen_width // 10 * 9.3
        pictsPos[11] = screen_height // 10 * 9

    if gameSection == 0:
        for i in trashes:
            if i.type == 'glass':
                if levels[level][i.y][i.x] != 10 and levels[level][i.y][i.x] != 11 and levels[level][i.y][i.x] != 1 and levels[level][i.y][i.x] != 2 and levels[level][i.y][i.x] != 3 and levels[level][i.y][i.x] != 4:
                    trashes.remove(i)

                else:
                    if trashCreatingTimer == 100 or trashCreatingTimer == 50:
                        if levels[level][i.y][i.x] == 1 or levels[level][i.y][i.x] == 11:
                            i.y -= 1
                        elif levels[level][i.y][i.x] == 2:
                            i.x += 1
                        elif levels[level][i.y][i.x] == 3:
                            i.y += 1
                        elif levels[level][i.y][i.x] == 4:
                            i.x -= 1
                        elif levels[level][i.y][i.x] == 10:
                            if level == 0:
                                levelIsDone = True
                            else:
                                levelsIsDone[0] = True
                    i.draw()
            elif i.type == 'plaster':
                if levels[level][i.y][i.x] != 15 and levels[level][i.y][i.x] != 14 and levels[level][i.y][i.x] != 13 and levels[level][i.y][i.x] != 5 and levels[level][i.y][i.x] != 6 and levels[level][i.y][i.x] != 7 and levels[level][i.y][i.x] != 8:
                    trashes.remove(i)

                else:
                    if trashCreatingTimer == 100 or trashCreatingTimer == 50:
                        if levels[level][i.y][i.x] == 5 or levels[level][i.y][i.x] == 14:
                            i.y -= 1
                        elif levels[level][i.y][i.x] == 6:
                            i.x += 1
                        elif levels[level][i.y][i.x] == 7:
                            i.y += 1
                        elif levels[level][i.y][i.x] == 8:
                            i.x -= 1
                        elif levels[level][i.y][i.x] == 15:
                            levelsIsDone[1] = True
                    i.draw()

        if trashCreatingTimer == 0:
            if level == 0:
                trashes.append(Trash(2, 7, "glass"))
            elif level == 1:
                trashes.append(Trash(0, 7, "glass"))
                trashes.append(Trash(2, 9, "plaster"))
            trashCreatingTimer = 100
        else:
            trashCreatingTimer -= 1
    pygame.display.flip()
    clock.tick(60)
screen.fill(WHITE)

flag = False
pygame.draw.rect(screen, BLACK, ((0, screen_height//8*6), (screen_width, screen_height//4)))
pygame.draw.line(screen, GRAY, (0, screen_height//8*6),(screen_width, screen_height//8*6), 7)
pygame.draw.line(screen, GRAY, (0, screen_height-3),(screen_width, screen_height-3), 7)
pygame.draw.line(screen, GRAY, (0, screen_height//8*6),(0, screen_height), 7)
pygame.draw.line(screen, GRAY, (screen_width-3, screen_height//8*6),(screen_width-3, screen_height), 7)
t1 = f2.render('ГОЛОС:', 1, GREEN_MATRIX)
screen.blit(t1, (screen_width//16, screen_height // 8 * 6 + 10))

t1 = f1.render('Это устройство понравилось всем судьям, поздравляем!', 1, GREEN_MATRIX)
screen.blit(t1, (screen_width//8, screen_height // 8 * 7))
pygame.display.flip()
while not flag:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            flag = True
        if i.type == pygame.MOUSEBUTTONDOWN:
            flag = True
    clock.tick(60)

screen.blit(final, (0, 0))
screen.blit(chel, (screen_width // 4 * 3, screen_height // 4))
pygame.draw.rect(screen, BLACK, ((0, screen_height//8*6), (screen_width, screen_height//4)))
pygame.draw.line(screen, GRAY, (0, screen_height//8*6),(screen_width, screen_height//8*6), 7)
pygame.draw.line(screen, GRAY, (0, screen_height-3),(screen_width, screen_height-3), 7)
pygame.draw.line(screen, GRAY, (0, screen_height//8*6),(0, screen_height), 7)
pygame.draw.line(screen, GRAY, (screen_width-3, screen_height//8*6),(screen_width-3, screen_height), 7)
t1 = f2.render('КАПРАЛ:', 1, GREEN_MATRIX)
screen.blit(t1, (screen_width//16, screen_height // 8 * 6 + 10))
t1 = f1.render('Хорошая работа, капитан! Мир спасен', 1, GREEN_MATRIX)
screen.blit(t1, (screen_width//8, screen_height // 8 * 7))
pygame.display.flip()

flag = False
while not flag:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            flag = True
        if i.type == pygame.MOUSEBUTTONDOWN:
            flag = True
    clock.tick(60)

pygame.quit()
