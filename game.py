import os
from re import S
import sys
import cv2
import random
import pygame


agh = [[1, 2], [2, 3], [22, 3], [23, 3], [23, 2], [23, 1], [22, 1], [21, 1], [21, 2], [21, 3], [12, 12], [0, 13]]
lst = []

image = pygame.image.load('fon.jpg')
image1 = pygame.image.load('39.png')
image2 = pygame.image.load('56.png')
image3 = pygame.image.load('coin2.png')
image4 = pygame.image.load('portal.png')
image5 = pygame.image.load('ronz.png')
image6 = pygame.image.load('sword1.png')
image7 = pygame.image.load('ук.png')
image8 = pygame.image.load('крылья.png')
image13 = pygame.image.load('bc3.jpg')
image38 = pygame.image.load('mon1.png')
image18 = pygame.image.load('we12.png')
image67 = pygame.image.load('cityc.png')
image56 = pygame.image.load('d1.jpg')
image511 = pygame.image.load('bron1.png')
image5112 = pygame.image.load('tar.png')
image512 = pygame.image.load('меч1.png')
images = pygame.image.load('i.jpg')
imagef = pygame.image.load('sword91.jpg')
imageb = pygame.image.load('armor.jpg')
image1d = pygame.image.load('od.jpg')
imageyes = pygame.image.load('monetka.png')
imageno = pygame.image.load('monetka13.png')

all_sprites = pygame.sprite.Group()

def make_bingo(ty):
    res = list()
    resy = random.sample(range(0, 14 * 26 - 1), ty)
    resy = resy[:ty // 2] + [0] + resy[ty // 2:]
    res.append(resy[:])
    return res

def cv2ImageToSurface(cv2Image):
    size = cv2Image.shape[1::-1]
    format = 'RGBA' if cv2Image.shape[2] == 4 else 'RGB'
    cv2Image[:, :, [0, 2]] = cv2Image[:, :, [2, 0]]
    surface = pygame.image.frombuffer(cv2Image.flatten(), size, format)
    return surface.convert_alpha() if format == 'RGBA' else surface.convert()

def loadGIF(filename):
    gif = cv2.VideoCapture(filename)
    frames = []
    while True:
        ret, cv2Image = gif.read()
        if not ret:
            break
        pygameImage = cv2ImageToSurface(cv2Image)
        frames.append(pygameImage)
    return frames




class Board:
    colors = ["black", "white"]
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.board[3][4] = 2
        self.board[6][7] = 2
        self.board[9][7] = 2
        self.board[0][1] = 2
        self.board[5][2] = 2
        self.board[1][6] = 2
        self.board[2][9] = 2
        self.board[4][11] = 2
        self.board[9][1] = 2
        self.board[12][2] = 2
        self.board[0][13] = 2
        self.board[10][10] = 2
        self.board[9][4] = 2
        self.board[23][1] = 2
        self.board[18][0] = 2
        self.board[21][3] = 2
        self.board[23][6] = 2
        self.board[21][10] = 2
        self.board[2][9] = 2
        self.board[15][5] = 2
        self.board[16][11] = 2
        self.board[12][7] = 2
        self.board[7][9] = 2
        self.board[24][11] = 2
        self.board[12][12] = 2
        self.board[6][5] = 2
        self.board[17][2] = 2
        self.board[18][9] = 2
        self.board[15][1] = 2
        self.board[15][8] = 2
        self.board[19][12] = 2
        self.board[18][5] = 3
        self.board[19][5] = 3
        self.board[20][5] = 3
        self.board[18][6] = 3
        self.board[19][6] = 3
        self.board[20][6] = 3
        self.board[18][7] = 3
        self.board[19][7] = 3
        self.board[20][7] = 3
        self.left = 10
        self.top = 10
        self.size = 70

    def render(self, screen, d):
        global s
        s = 0
        if d == 9:
            for r in lst[0]:
                j = r // 26
                i = r % 26
                dog_surf1 = pygame.transform.scale(image1d, (68, 68))
                dog_surf1.set_colorkey((255, 255, 255))
                dog_rect1 = dog_surf1.get_rect(bottomright=(i * self.size + 69, j * self.size + 69))
                screen.blit(dog_surf1, dog_rect1)
        if d == 0:
            pygame.draw.rect(screen, (0, 0, 0),
                                     (0, 0, width, height), 0)
        for j in range(0, self.width):
            for i in range(0, self.height):
                pygame.draw.rect(screen, (255, 255, 255),
                                     (i * self.size, j * self.size, self.size, self.size), 1)
        for j in range(0, self.width):
            for i in range(0, self.height):
                if self.board[i][j] == 1 and d == 0:
                    s = 1
                    pygame.draw.rect(screen, (0, 0, 0),
                                     (i * self.size, j * self.size, self.size, self.size), 1)
                    dog_surf1 = pygame.transform.scale(image1, (68, 68))
                    dog_surf1.set_colorkey((255, 255, 255))
                    dog_rect1 = dog_surf1.get_rect(bottomright=(i * self.size + 69, j * self.size + 69))
                    screen.blit(dog_surf1, dog_rect1)
                elif self.board[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (i * self.size, j * self.size, self.size, self.size), 1)
                elif self.board[i][j] == 1 and d >= 1:
                    pygame.draw.rect(screen, (0, 0, 0),
                                     (i * self.size, j * self.size, self.size, self.size), 1)
                    dog_surf1 = pygame.transform.scale(image2, (68, 68))
                    dog_surf1.set_colorkey((255, 255, 255))
                    dog_rect1 = dog_surf1.get_rect(bottomright=(i * self.size + 69, j * self.size + 69))
                    screen.blit(dog_surf1, dog_rect1)
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (i * self.size, j * self.size, self.size, self.size), 1)
                elif self.board[i][j] == 2 and d == 0:
                    pygame.draw.line(screen, (255, 255, 0), (i * self.size + 1, j * self.size + 1), (i * self.size + 69, j * self.size + 69), 5)
                    pygame.draw.line(screen, (255, 255, 0), (i * self.size + 1, j * self.size + 69), (i * self.size + 69, j * self.size + 1), 5)
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (i * self.size, j * self.size, self.size, self.size), 1)
                elif self.board[i][j] == 2 and d == 1:
                    pygame.draw.rect(screen, (0, 0, 0),
                                     (i * self.size, j * self.size, self.size, self.size), 1)
                    dog_surf1 = pygame.transform.scale(image3, (38, 38))
                    dog_surf1.set_colorkey((255, 255, 255))
                    dog_rect1 = dog_surf1.get_rect(bottomright=(i * self.size + 53, j * self.size + 53))
                    screen.blit(dog_surf1, dog_rect1)
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (i * self.size, j * self.size, self.size, self.size), 1)
                elif self.board[i][j] == 3 and d == 0:
                    pygame.draw.line(screen, (0, 0, 255), (i * self.size + 1, j * self.size + 1), (i * self.size + 69, j * self.size + 69), 5)
                    pygame.draw.line(screen, (0, 0, 255), (i * self.size + 1, j * self.size + 69), (i * self.size + 69, j * self.size + 1), 5)
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (i * self.size, j * self.size, self.size, self.size), 1)
        if d == 2:
            global agh
            for t in agh:
                i = t[0]
                j = t[1]
                pygame.draw.rect(screen, (0, 0, 0),
                                     (i * self.size, j * self.size, self.size, self.size), 1)
                dog_surf1 = pygame.transform.scale(image3, (38, 38))
                dog_surf1.set_colorkey((255, 255, 255))
                dog_rect1 = dog_surf1.get_rect(bottomright=(i * self.size + 53, j * self.size + 53))
                screen.blit(dog_surf1, dog_rect1)
                pygame.draw.rect(screen, (255, 255, 255),
                                 (i * self.size, j * self.size, self.size, self.size), 1)
        if d == 9:
            for j in range(0, self.width):
                for i in range(0, self.height):
                    pygame.draw.rect(screen, (0, 0, 255),
                                         (i * self.size, j * self.size, self.size, self.size), 1)




    def set_view(self, left, top, size):
        self.left = left
        self.top = top
        self.size = size

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pouse):
        x = (mouse_pouse[1] - self.left) // self.size
        y = (mouse_pouse[0] - self.top) // self.size
        if 0 <= x < self.width and 0 <= y < self.height:
            return x, y
        return None

    def on_click(self, cell_coords):
        y, x = cell_coords
        for j in range(0, self.width):
            for i in range(0, self.height):
                self.board[i][j] = 0
        self.board[x][y] = (self.board[x][y] + 1) % 2
        self.board[7][9] = 2
        self.board[9][7] = 2
        self.board[24][11] = 2
        self.board[15][8] = 2
        self.board[19][12] = 2
        self.board[12][12] = 2
        self.board[6][5] = 2
        self.board[17][2] = 2
        self.board[18][9] = 2
        self.board[15][1] = 2
        self.board[3][4] = 2
        self.board[6][7] = 2
        self.board[0][1] = 2
        self.board[5][2] = 2
        self.board[1][6] = 2
        self.board[2][9] = 2
        self.board[4][11] = 2
        self.board[9][1] = 2
        self.board[12][2] = 2
        self.board[0][13] = 2
        self.board[10][10] = 2
        self.board[9][4] = 2
        self.board[23][1] = 2
        self.board[18][0] = 2
        self.board[21][3] = 2
        self.board[23][6] = 2
        self.board[21][10] = 2
        self.board[2][9] = 2
        self.board[15][5] = 2
        self.board[16][11] = 2
        self.board[12][7] = 2
        self.board[18][5] = 3
        self.board[19][5] = 3
        self.board[20][5] = 3
        self.board[18][6] = 3
        self.board[19][6] = 3
        self.board[20][6] = 3
        self.board[18][7] = 3
        self.board[19][7] = 3
        self.board[20][7] = 3


    def n(self):
        for j in range(0, self.width):
            for i in range(0, self.height):
                if self.board[i][j] == 1:
                    return i, j

    def g(self):
        y = []
        for j in range(0, self.width):
            for i in range(0, self.height):
                if self.board[i][j] == 2:
                    z = [i, j]
                    y.append(z)
        return y

    def fm(self, x1, y1):
        self.board[x1][y1] = 0
        self.board[x1][y1 + 1] = 1

    def fp(self, x1, y1):
        self.board[x1][y1] = 0
        self.board[x1][y1 - 1] = 1

    def rm(self, x1, y1):
        self.board[x1][y1] = 0
        self.board[x1 + 1][y1] = 1

    def rp(self, x1, y1):
        self.board[x1][y1] = 0
        self.board[x1 - 1][y1] = 1



def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    fg = make_bingo(44)
    print(fg)
    dam = 20000
    prot = 3
    hp = 80
    chance = 20
    def stat(x1, y1, p):
        global d
        global agh
        global coins
        if d == 1:
            for i in p:
                if i[0] == x1 and i[1] == y1:
                    coins += 1
                    print(coins)
                    n = p.index(i)
                    del p[n]
        if d == 2:
            for t in agh:
                if t[0] == x1 and t[1] == y1:
                    coins += 1
                    print(coins)
                    n = agh.index(t)
                    del agh[n]
    coins = 0
    pygame.init()
    size = width, height = 1820, 980
    screen = pygame.display.set_mode(size)
    board = Board(height // 70, width // 70)
    running = True
    d = 1
    s = 0
    gh = 0
    gifFrameList1 = loadGIF(r"ghy1.gif")
    currentFrame1 = 0
    clock = pygame.time.Clock()
    while running:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    running = False
        rect1 = gifFrameList1[currentFrame1].get_rect(center = (530, 300))
        b1 = pygame.transform.scale(gifFrameList1[currentFrame1], (width, height))
        screen.blit(b1, rect1)
        currentFrame1 = (currentFrame1 + 1) % len(gifFrameList1)
        dog_surf1112 = pygame.transform.scale(image38, (200, 200))
        dog_rect1112 = dog_surf1112.get_rect(bottomright=(1010, 500))
        screen.blit(dog_surf1112, dog_rect1112)
        dog_surf11124 = pygame.transform.scale(image18, (500, 300))
        dog_rect11124 = dog_surf11124.get_rect(bottomright=(1160, 800))
        screen.blit(dog_surf11124, dog_rect11124)
        pygame.display.flip()
    running = True
    gifFrameList2 = loadGIF(r"1цу.gif")
    gifFrameList21 = loadGIF(r"fong.gif")
    currentFrame2 = 0
    currentFrame21 = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and s == 1:
                    running = False
        screen.fill((0, 0, 0))
        board.render(screen, 0)
        pygame.display.flip()
    running = True
    screen.fill((0, 0, 0))
    pygame.display.flip()
    x1, y1 = board.n()
    p = board.g()
    print(p)
    life = 10
    while running == True:
        rect21 = gifFrameList21[currentFrame21].get_rect(center = (420, 275))
        b21 = pygame.transform.scale(gifFrameList21[currentFrame21], (width, height))
        b21.set_colorkey((255, 255, 255))
        screen.blit(b21, rect21)
        currentFrame21 = (currentFrame21 + 1) % len(gifFrameList21)
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and y1 != height // 70 - 1 and gh == 0:
                    board.fm(x1, y1)
                    y1 += 1
                    stat(x1, y1, p)
                if event.key == pygame.K_w and y1 != 0 and gh == 0:
                    board.fp(x1, y1)
                    y1 -= 1
                    stat(x1, y1, p)
                if event.key == pygame.K_d and x1 != width // 70 - 1 and gh == 0:
                    board.rm(x1, y1)
                    x1 += 1
                    stat(x1, y1, p)
                if event.key == pygame.K_a and x1 != 0 and gh == 0:
                    board.rp(x1, y1)
                    x1 -= 1
                    stat(x1, y1, p)
                if event.key == pygame.K_m:
                    gh = (gh + 1) % 2
                if x1 >= 18 and x1 <= 20 and y1 >= 5 and y1 <= 7 and event.key == pygame.K_j:
                    running = False
                print(x1, y1)
                #19 6
        font = pygame.font.Font(None, 40)
        text = font.render("Health: " + str(hp), True, (255, 0, 0))
        text_x = 1650 - text.get_width() // 2
        text_y = 30 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        if gh == 0:
            rect2 = gifFrameList2[currentFrame2].get_rect(center = (1400, 485))
            b2 = pygame.transform.scale(gifFrameList2[currentFrame2], (200, 200))
            b2.set_colorkey((255, 255, 255))
            screen.blit(b2, rect2)
            currentFrame2 = (currentFrame2 + 1) % len(gifFrameList2)
            board.render(screen, 1)
            pygame.display.flip()
        if(gh == 1):
            board.render(screen, 1)
            a = width
            b = height
            pygame.draw.rect(screen, (255, 255, 255), (30, 160,
                                           440, 440), 0)
            pygame.draw.rect(screen, (255, 255, 255), (1090, 20,
                                           440, 440), 0)
            pygame.draw.rect(screen, (255, 255, 255), (590, 430,
                                           440, 440), 0)
            pygame.draw.rect(screen, (0, 255, 0), (30, 160,
                                           440, 440), 5)
            pygame.draw.rect(screen, (0, 255, 0), (1090, 20,
                                           440, 440), 5)
            pygame.draw.rect(screen, (0, 255, 0), (590, 430,
                                           440, 440), 5)
            pygame.draw.rect(screen, (255, 255, 255), (1350, 500,
                                           440, 440), 0)
            pygame.draw.rect(screen, (0, 255, 0), (1350, 500,
                                           440, 440), 5)

            pygame.draw.rect(screen, (0, 0, 0), (50, 180,
                                           400, 400), 0)
            pygame.draw.rect(screen, (0, 0, 0), (1110, 40,
                                           400, 400), 0)
            pygame.draw.rect(screen, (0, 0, 0), (610, 450,
                                           400, 400), 0)
            pygame.draw.rect(screen, (0, 255, 0), (50, 180,
                                           400, 400), 3)
            pygame.draw.rect(screen, (0, 255, 0), (1110, 40,
                                           400, 400), 3)
            pygame.draw.rect(screen, (0, 255, 0), (610, 450,
                                           400, 400), 3)
            pygame.draw.rect(screen, (0, 0, 0), (1370, 520,
                                           400, 400), 0)
            pygame.draw.rect(screen, (0, 255, 0), (1370, 520,
                                           400, 400), 3)

            pygame.draw.rect(screen, (0, 0, 0), (600, 80,
                                           400, 300), 0)
            pygame.draw.rect(screen, (0, 255, 0), (600, 80,
                                           400, 300), 5)
            pygame.draw.rect(screen, (0, 0, 0), (50, 670,
                                           400, 200), 0)
            pygame.draw.rect(screen, (0, 255, 0), (50, 670,
                                           400, 200), 5)
            pygame.draw.rect(screen, (0, 0, 0), (1075, 520,
                                           250, 400), 0)
            pygame.draw.rect(screen, (0, 255, 0), (1075, 520,
                                           250, 400), 5)

            pygame.draw.rect(screen, (0, 0, 0), (1600, 100,
                                           140, 200), 0)
            pygame.draw.rect(screen, (0, 255, 0), (1600, 100,
                                           140, 200), 5)
            dog_surf111 = pygame.transform.scale(image3, (70, 70))
            dog_rect111 = dog_surf111.get_rect(bottomright=(1705, 205))
            screen.blit(dog_surf111, dog_rect111)
            font = pygame.font.Font(None, 40)
            text = font.render("Coins:", True, (255, 255, 0))
            text_x = 1672 - text.get_width() // 2
            text_y = 230 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            font = pygame.font.Font(None, 35)
            text = font.render(str(coins), True, (255, 255, 0))
            text_x = 1672 - text.get_width() // 2
            text_y = 260 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            



            font = pygame.font.Font(None, 40)
            text = font.render("Your Stats:", True, (0, 255, 0))
            text_x = 1200 - text.get_width() // 2
            text_y = 550 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            font = pygame.font.Font(None, 40)
            text = font.render("Attack: " + str(dam), True, (255, 0, 255))
            text_x = 1170 - text.get_width() // 2
            text_y = 600 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            font = pygame.font.Font(None, 40)
            text = font.render("HP: " + str(hp), True, (255, 0, 0))
            text_x = 1150 - text.get_width() // 2
            text_y = 650 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            font = pygame.font.Font(None, 40)
            text = font.render("Protection: " + str(prot), True, (33, 240, 248))
            text_x = 1190 - text.get_width() // 2
            text_y = 700 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            font = pygame.font.Font(None, 40)
            text = font.render("Lucky Chance: ", True, (255, 255, 0))
            text_x = 1200 - text.get_width() // 2
            text_y = 770 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            font = pygame.font.Font(None, 40)
            text = font.render(str(chance) + "%", True, (255, 255, 0))
            text_x = 1200 - text.get_width() // 2
            text_y = 820 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))





            dog_surf11 = pygame.transform.scale(image6, (300, 300))
            dog_rect11 = dog_surf11.get_rect(bottomright=(400, 515))
            screen.blit(dog_surf11, dog_rect11)
            dog_surf13 = pygame.transform.scale(image5, (300, 300))
            dog_rect13 = dog_surf13.get_rect(bottomright=(960, 790))
            screen.blit(dog_surf13, dog_rect13)
            dog_surf15 = pygame.transform.scale(image7, (350, 350))
            dog_rect15 = dog_surf15.get_rect(bottomright=(1735, 895))
            screen.blit(dog_surf15, dog_rect15)
            dog_surf16 = pygame.transform.scale(image8, (300, 300))
            dog_rect16 = dog_surf16.get_rect(bottomright=(1463, 385))
            screen.blit(dog_surf16, dog_rect16)
            font = pygame.font.Font(None, 70)
            text = font.render("Your Profile:", True, (100, 255, 100))
            text_x = 800 - text.get_width() // 2
            text_y = 220 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            pygame.draw.rect(screen, (0, 255, 0), (text_x - 20, text_y - 80,
                                                   text_w + 40, text_h + 160), 3)
            font = pygame.font.Font(None, 30)
            text = font.render("press 'm' to return to the game", True, (255, 255, 255))
            text_x = 250 - text.get_width() // 2
            text_y = 770 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            pygame.display.flip()
    running = True
    gifFrameList = loadGIF(r"oie_261348453ESzBD2e.gif")
    gifFrameList3 = loadGIF(r"lava.gif")
    gifFrameListboss = loadGIF(r"boss.gif")
    currentFrameboss = 0
    currentFrame = 0
    timer = pygame.time.get_ticks
    timeout = 7000 # milliseconds
    deadline = timer() + timeout
    while running == True:
        now = timer()
        clock.tick(25)
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        if now > deadline:
            running = False
        rect = gifFrameList[currentFrame].get_rect(center = (800, 400))
        b = pygame.transform.scale(gifFrameList[currentFrame], (400, 400))
        b.set_colorkey((255, 255, 255))
        screen.blit(b, rect)
        currentFrame = (currentFrame + 1) % len(gifFrameList)
        pygame.display.flip()
    running = True
    d = 2
    currentFrame2 = 0
    currentFrame3 = 0
    currentFrame31 = 0
    currentFrame32 = 0
    currentFrame33 = 0
    currentFrame34 = 0
    currentFrame35 = 0
    currentFrame36 = 0
    currentFrame37 = 0
    brona = 0
    sword = 0
    ghj = [[10, 7], [12, 3], [5, 4], [23, 11], [7, 8], [3, 7], [2, 11], [16, 9]]
    while running == True:
        dog_surf = pygame.transform.scale(image56, (width, height))
        dog_rect = dog_surf.get_rect(bottomright=(width, height))
        screen.blit(dog_surf, dog_rect)
        if brona == 0:
            dog_surf23 = pygame.transform.scale(image511, (68, 68))
            dog_rect23 = dog_surf23.get_rect(bottomright=(698, 420))
            screen.blit(dog_surf23, dog_rect23)
        if sword == 0:
            dog_surf23 = pygame.transform.scale(image512, (60, 60))
            dog_rect23 = dog_surf23.get_rect(bottomright=(1601, 205))
            screen.blit(dog_surf23, dog_rect23)
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and y1 != height // 70 - 1 and gh == 0:
                    board.fm(x1, y1)
                    y1 += 1
                    stat(x1, y1, p)
                if event.key == pygame.K_w and y1 != 0 and gh == 0:
                    board.fp(x1, y1)
                    y1 -= 1
                    stat(x1, y1, p)
                if event.key == pygame.K_d and x1 != width // 70 - 1 and gh == 0:
                    board.rm(x1, y1)
                    x1 += 1
                    stat(x1, y1, p)
                if event.key == pygame.K_a and x1 != 0 and gh == 0:
                    board.rp(x1, y1)
                    x1 -= 1
                    stat(x1, y1, p)
                for t in ghj:
                    if x1 == t[0] and y1 == t[1]:
                        hp -= 1
                if event.key == pygame.K_m:
                    gh = (gh + 1) % 2
                if event.key == pygame.K_j and x1 == 19 and y1 == 6:
                    running = False
                if event.key == pygame.K_n and x1 == 9 and y1 == 5:
                    image5 = pygame.image.load('bron1.png')
                    brona = 1
                    prot += 20
                    prot -= 3
                    hp += 50
                    hp -= 30
                    chance += 7
                if event.key == pygame.K_n and x1 == 22 and y1 == 2:
                    image6 = pygame.image.load('меч1.png')
                    sword = 1
                    dam = 55
                    chance += 12
                    prot += 2
                print(x1, y1)
                #19 6
                # life
        font = pygame.font.Font(None, 40)
        text = font.render("Health: " + str(hp), True, (255, 0, 0))
        text_x = 1650 - text.get_width() // 2
        text_y = 30 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        
        if gh == 0:
            rect2 = gifFrameList2[currentFrame2].get_rect(center = (1400, 485))
            b2 = pygame.transform.scale(gifFrameList2[currentFrame2], (200, 200))
            b2.set_colorkey((255, 255, 255))
            screen.blit(b2, rect2)
            currentFrame2 = (currentFrame2 + 1) % len(gifFrameList2)

            rect3 = gifFrameList3[currentFrame3].get_rect(center = (801, 591))
            b3 = pygame.transform.scale(gifFrameList3[currentFrame3], (68, 68))
            b3.set_colorkey((255, 255, 255))
            screen.blit(b3, rect3)
            currentFrame3 = (currentFrame3 + 1) % len(gifFrameList3)

            rect33 = gifFrameList3[currentFrame33].get_rect(center = (801 + 13 * 70, 591 + 4 * 70))
            b33 = pygame.transform.scale(gifFrameList3[currentFrame33], (68, 68))
            b33.set_colorkey((255, 255, 255))
            screen.blit(b33, rect33)
            currentFrame33 = (currentFrame33 + 1) % len(gifFrameList3)

            rect34 = gifFrameList3[currentFrame34].get_rect(center = (801 - 3 * 70, 591 + 70))
            b34 = pygame.transform.scale(gifFrameList3[currentFrame34], (68, 68))
            b34.set_colorkey((255, 255, 255))
            screen.blit(b34, rect34)
            currentFrame34 = (currentFrame34 + 1) % len(gifFrameList3)

            rect35 = gifFrameList3[currentFrame35].get_rect(center = (801 - 7 * 70, 591))
            b35 = pygame.transform.scale(gifFrameList3[currentFrame35], (68, 68))
            b35.set_colorkey((255, 255, 255))
            screen.blit(b35, rect35)
            currentFrame35 = (currentFrame35 + 1) % len(gifFrameList3)

            rect36 = gifFrameList3[currentFrame36].get_rect(center = (801 - 8 * 70, 591 + 4 * 70))
            b36 = pygame.transform.scale(gifFrameList3[currentFrame36], (68, 68))
            b36.set_colorkey((255, 255, 255))
            screen.blit(b36, rect36)
            currentFrame36 = (currentFrame36 + 1) % len(gifFrameList3)

            rect37 = gifFrameList3[currentFrame37].get_rect(center = (801 + 6 * 70, 591 + 2 * 70))
            b37 = pygame.transform.scale(gifFrameList3[currentFrame37], (68, 68))
            b37.set_colorkey((255, 255, 255))
            screen.blit(b37, rect37)
            currentFrame37 = (currentFrame37 + 1) % len(gifFrameList3)

            rect31 = gifFrameList3[currentFrame31].get_rect(center = (941, 311))
            b31 = pygame.transform.scale(gifFrameList3[currentFrame31], (68, 68))
            b31.set_colorkey((255, 255, 255))
            screen.blit(b31, rect31)
            currentFrame31 = (currentFrame31 + 1) % len(gifFrameList3)

            rect32 = gifFrameList3[currentFrame32].get_rect(center = (451, 381))
            b32 = pygame.transform.scale(gifFrameList3[currentFrame32], (68, 68))
            b32.set_colorkey((255, 255, 255))
            screen.blit(b32, rect32)
            currentFrame32 = (currentFrame32 + 1) % len(gifFrameList3)
            board.render(screen, 2)
            if x1 == 9 and y1 == 5 and brona == 0:
                dog_surf11191 = pygame.transform.scale(imageb, (200, 300))
                dog_rect11191 = dog_surf11191.get_rect(bottomright=(900, 400))
                screen.blit(dog_surf11191, dog_rect11191)
            if x1 == 22 and y1 == 2 and sword == 0:
                dog_surf11191 = pygame.transform.scale(imagef, (200, 300))
                dog_rect11191 = dog_surf11191.get_rect(bottomright=(1520, 310))
                screen.blit(dog_surf11191, dog_rect11191)
            pygame.display.flip()
        if(gh == 1):
            board.render(screen, 2)
            a = width
            b = height
            pygame.draw.rect(screen, (255, 255, 255), (30, 160,
                                           440, 440), 0)
            pygame.draw.rect(screen, (255, 255, 255), (1090, 20,
                                           440, 440), 0)
            pygame.draw.rect(screen, (255, 255, 255), (590, 430,
                                           440, 440), 0)
            pygame.draw.rect(screen, (0, 255, 0), (30, 160,
                                           440, 440), 5)
            pygame.draw.rect(screen, (0, 255, 0), (1090, 20,
                                           440, 440), 5)
            pygame.draw.rect(screen, (0, 255, 0), (590, 430,
                                           440, 440), 5)
            pygame.draw.rect(screen, (255, 255, 255), (1350, 500,
                                           440, 440), 0)
            pygame.draw.rect(screen, (0, 255, 0), (1350, 500,
                                           440, 440), 5)

            pygame.draw.rect(screen, (0, 0, 0), (50, 180,
                                           400, 400), 0)
            pygame.draw.rect(screen, (0, 0, 0), (1110, 40,
                                           400, 400), 0)
            pygame.draw.rect(screen, (0, 0, 0), (610, 450,
                                           400, 400), 0)
            pygame.draw.rect(screen, (0, 255, 0), (50, 180,
                                           400, 400), 3)
            pygame.draw.rect(screen, (0, 255, 0), (1110, 40,
                                           400, 400), 3)
            pygame.draw.rect(screen, (0, 255, 0), (610, 450,
                                           400, 400), 3)
            pygame.draw.rect(screen, (0, 0, 0), (1370, 520,
                                           400, 400), 0)
            pygame.draw.rect(screen, (0, 255, 0), (1370, 520,
                                           400, 400), 3)

            pygame.draw.rect(screen, (0, 0, 0), (600, 80,
                                           400, 300), 0)
            pygame.draw.rect(screen, (0, 255, 0), (600, 80,
                                           400, 300), 5)
            pygame.draw.rect(screen, (0, 0, 0), (50, 670,
                                           400, 200), 0)
            pygame.draw.rect(screen, (0, 255, 0), (50, 670,
                                           400, 200), 5)
            pygame.draw.rect(screen, (0, 0, 0), (1075, 520,
                                           250, 400), 0)
            pygame.draw.rect(screen, (0, 255, 0), (1075, 520,
                                           250, 400), 5)

            pygame.draw.rect(screen, (0, 0, 0), (1600, 100,
                                           140, 200), 0)
            pygame.draw.rect(screen, (0, 255, 0), (1600, 100,
                                           140, 200), 5)
            dog_surf111 = pygame.transform.scale(image3, (70, 70))
            dog_rect111 = dog_surf111.get_rect(bottomright=(1705, 205))
            screen.blit(dog_surf111, dog_rect111)
            font = pygame.font.Font(None, 40)
            text = font.render("Coins:", True, (255, 255, 0))
            text_x = 1672 - text.get_width() // 2
            text_y = 230 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            font = pygame.font.Font(None, 35)
            text = font.render(str(coins), True, (255, 255, 0))
            text_x = 1672 - text.get_width() // 2
            text_y = 260 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            

            font = pygame.font.Font(None, 40)
            text = font.render("Your Stats:", True, (0, 255, 0))
            text_x = 1200 - text.get_width() // 2
            text_y = 550 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            font = pygame.font.Font(None, 40)
            text = font.render("Attack: " + str(dam), True, (255, 0, 255))
            text_x = 1170 - text.get_width() // 2
            text_y = 600 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            font = pygame.font.Font(None, 40)
            text = font.render("HP: " + str(hp), True, (255, 0, 0))
            text_x = 1150 - text.get_width() // 2
            text_y = 650 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            font = pygame.font.Font(None, 40)
            text = font.render("Protection: " + str(prot), True, (33, 240, 248))
            text_x = 1190 - text.get_width() // 2
            text_y = 700 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            font = pygame.font.Font(None, 40)
            text = font.render("Lucky Chance: ", True, (255, 255, 0))
            text_x = 1200 - text.get_width() // 2
            text_y = 770 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            font = pygame.font.Font(None, 40)
            text = font.render(str(chance) + "%", True, (255, 255, 0))
            text_x = 1200 - text.get_width() // 2
            text_y = 820 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))


            dog_surf11 = pygame.transform.scale(image6, (300, 300))
            dog_rect11 = dog_surf11.get_rect(bottomright=(400, 515))
            screen.blit(dog_surf11, dog_rect11)
            dog_surf13 = pygame.transform.scale(image5, (300, 300))
            dog_rect13 = dog_surf13.get_rect(bottomright=(960, 790))
            screen.blit(dog_surf13, dog_rect13)
            dog_surf15 = pygame.transform.scale(image7, (350, 350))
            dog_rect15 = dog_surf15.get_rect(bottomright=(1735, 895))
            screen.blit(dog_surf15, dog_rect15)
            dog_surf16 = pygame.transform.scale(image8, (300, 300))
            dog_rect16 = dog_surf16.get_rect(bottomright=(1463, 385))
            screen.blit(dog_surf16, dog_rect16)
            font = pygame.font.Font(None, 70)
            text = font.render("Your Profile:", True, (100, 255, 100))
            text_x = 800 - text.get_width() // 2
            text_y = 220 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            pygame.draw.rect(screen, (0, 255, 0), (text_x - 20, text_y - 80,
                                                   text_w + 40, text_h + 160), 3)
            font = pygame.font.Font(None, 30)
            text = font.render("press 'm' to return to the game", True, (255, 255, 255))
            text_x = 250 - text.get_width() // 2
            text_y = 770 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            pygame.display.flip()
    running = True
    currentFrame = 0
    timer = pygame.time.get_ticks
    timeout = 7000 # milliseconds
    deadline = timer() + timeout
    while running == True:
        now = timer()
        clock.tick(25)
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        if now > deadline:
            running = False
        rect = gifFrameList[currentFrame].get_rect(center = (800, 400))
        b = pygame.transform.scale(gifFrameList[currentFrame], (400, 400))
        b.set_colorkey((255, 255, 255))
        screen.blit(b, rect)
        currentFrame = (currentFrame + 1) % len(gifFrameList)
        pygame.display.flip()
    running = True
    screen.fill((0, 0, 0))
    gifFrameListbo = loadGIF(r"fonforboss.gif")
    currentFramebo = 0
    cou = 2
    timer = pygame.time.get_ticks
    timeout = 3000 # milliseconds
    deadline = timer() + timeout
    timeout1 = 5000
    deadline1 = timer() + timeout1
    can = 1
    lst = make_bingo(cou)
    bosshp = 500
    e = []
    for i in range(100):
        e.append(0)
    for i in range(chance):
        e[i] = 1
    while running == True:
        now = timer()
        rectbo = gifFrameListbo[currentFramebo].get_rect(center = (177, 250))
        bbo = pygame.transform.scale(gifFrameListbo[currentFramebo], (width, height))
        bbo.set_colorkey((255, 255, 255))
        screen.blit(bbo, rectbo)
        currentFramebo = (currentFramebo + 1) % len(gifFrameListbo)
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if hp <= 0 or coins == 0:
                running = False
                itog = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and y1 != height // 70 - 1 and gh == 0:
                    board.fm(x1, y1)
                    y1 += 1
                    stat(x1, y1, p)
                if event.key == pygame.K_w and y1 != 0 and gh == 0:
                    board.fp(x1, y1)
                    y1 -= 1
                    stat(x1, y1, p)
                if event.key == pygame.K_d and x1 != width // 70 - 1 and gh == 0:
                    board.rm(x1, y1)
                    x1 += 1
                    stat(x1, y1, p)
                if event.key == pygame.K_a and x1 != 0 and gh == 0:
                    board.rp(x1, y1)
                    x1 -= 1
                    stat(x1, y1, p)
                if x1 == 10 and y1 == 7:
                    hp -= 1
                if x1 == 12 and y1 == 3:
                    hp -= 1
                if x1 == 5 and y1 == 4:
                    hp -= 1
                if event.key == pygame.K_m:
                    gh = (gh + 1) % 2
                if event.key == pygame.K_e and can == 1:
                    can = 0
                    random_index = random.randint(0,len(e)-1)
                    if e[random_index] == 1:
                        bosshp -= dam
                    coins -= 1
                
                    #life
        board.render(screen, 9)
        font = pygame.font.Font(None, 40)
        text = font.render("Health: " + str(hp), True, (255, 0, 0))
        text_x = 1650 - text.get_width() // 2
        text_y = 30 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        font = pygame.font.Font(None, 40)
        text = font.render("Health Boss: " + str(bosshp), True, (255, 0, 0))
        text_x = 1650 - text.get_width() // 2
        text_y = 230 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        if can == 0:
            dog_surf1 = pygame.transform.scale(imageno, (150, 150))
            dog_rect1 = dog_surf1.get_rect(bottomright=(1700, 700))
            screen.blit(dog_surf1, dog_rect1)
        else:
            dog_surf1 = pygame.transform.scale(imageyes, (150, 150))
            dog_rect1 = dog_surf1.get_rect(bottomright=(1700, 700))
            screen.blit(dog_surf1, dog_rect1)
        rectboss = gifFrameListboss[currentFrameboss].get_rect(center = (990, 435))
        bboss = pygame.transform.scale(gifFrameListboss[currentFrameboss], (400, 400))
        bboss.set_colorkey((255, 255, 255))
        screen.blit(bboss, rectboss)
        currentFrameboss = (currentFrameboss + 1) % len(gifFrameListboss)
        for r in lst[0]:
            if y1 == r // 26 and x1 == r % 26:
                hp -= 1
        if(gh == 1):
            a = width
            b = height
            pygame.draw.rect(screen, (255, 255, 255), (30, 160,
                                           440, 440), 0)
            pygame.draw.rect(screen, (255, 255, 255), (1090, 20,
                                           440, 440), 0)
            pygame.draw.rect(screen, (255, 255, 255), (590, 430,
                                           440, 440), 0)
            pygame.draw.rect(screen, (0, 255, 0), (30, 160,
                                           440, 440), 5)
            pygame.draw.rect(screen, (0, 255, 0), (1090, 20,
                                           440, 440), 5)
            pygame.draw.rect(screen, (0, 255, 0), (590, 430,
                                           440, 440), 5)
            pygame.draw.rect(screen, (255, 255, 255), (1350, 500,
                                           440, 440), 0)
            pygame.draw.rect(screen, (0, 255, 0), (1350, 500,
                                           440, 440), 5)

            pygame.draw.rect(screen, (0, 0, 0), (50, 180,
                                           400, 400), 0)
            pygame.draw.rect(screen, (0, 0, 0), (1110, 40,
                                           400, 400), 0)
            pygame.draw.rect(screen, (0, 0, 0), (610, 450,
                                           400, 400), 0)
            pygame.draw.rect(screen, (0, 255, 0), (50, 180,
                                           400, 400), 3)
            pygame.draw.rect(screen, (0, 255, 0), (1110, 40,
                                           400, 400), 3)
            pygame.draw.rect(screen, (0, 255, 0), (610, 450,
                                           400, 400), 3)
            pygame.draw.rect(screen, (0, 0, 0), (1370, 520,
                                           400, 400), 0)
            pygame.draw.rect(screen, (0, 255, 0), (1370, 520,
                                           400, 400), 3)

            pygame.draw.rect(screen, (0, 0, 0), (600, 80,
                                           400, 300), 0)
            pygame.draw.rect(screen, (0, 255, 0), (600, 80,
                                           400, 300), 5)
            pygame.draw.rect(screen, (0, 0, 0), (50, 670,
                                           400, 200), 0)
            pygame.draw.rect(screen, (0, 255, 0), (50, 670,
                                           400, 200), 5)
            pygame.draw.rect(screen, (0, 0, 0), (1075, 520,
                                           250, 400), 0)
            pygame.draw.rect(screen, (0, 255, 0), (1075, 520,
                                           250, 400), 5)

            pygame.draw.rect(screen, (0, 0, 0), (1600, 100,
                                           140, 200), 0)
            pygame.draw.rect(screen, (0, 255, 0), (1600, 100,
                                           140, 200), 5)
            dog_surf111 = pygame.transform.scale(image3, (70, 70))
            dog_rect111 = dog_surf111.get_rect(bottomright=(1705, 205))
            screen.blit(dog_surf111, dog_rect111)
            font = pygame.font.Font(None, 40)
            text = font.render("Coins:", True, (255, 255, 0))
            text_x = 1672 - text.get_width() // 2
            text_y = 230 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            font = pygame.font.Font(None, 35)
            text = font.render(str(coins), True, (255, 255, 0))
            text_x = 1672 - text.get_width() // 2
            text_y = 260 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            
            font = pygame.font.Font(None, 40)
            text = font.render("Your Stats:", True, (0, 255, 0))
            text_x = 1200 - text.get_width() // 2
            text_y = 550 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            font = pygame.font.Font(None, 40)
            text = font.render("Attack: " + str(dam), True, (255, 0, 255))
            text_x = 1170 - text.get_width() // 2
            text_y = 600 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            font = pygame.font.Font(None, 40)
            text = font.render("HP: " + str(hp), True, (255, 0, 0))
            text_x = 1150 - text.get_width() // 2
            text_y = 650 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            font = pygame.font.Font(None, 40)
            text = font.render("Protection: " + str(prot), True, (33, 240, 248))
            text_x = 1190 - text.get_width() // 2
            text_y = 700 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            font = pygame.font.Font(None, 40)
            text = font.render("Lucky Chance: ", True, (255, 255, 0))
            text_x = 1200 - text.get_width() // 2
            text_y = 770 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            font = pygame.font.Font(None, 40)
            text = font.render(str(chance) + "%", True, (255, 255, 0))
            text_x = 1200 - text.get_width() // 2
            text_y = 820 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))


            dog_surf11 = pygame.transform.scale(image6, (300, 300))
            dog_rect11 = dog_surf11.get_rect(bottomright=(400, 515))
            screen.blit(dog_surf11, dog_rect11)
            dog_surf13 = pygame.transform.scale(image5, (300, 300))
            dog_rect13 = dog_surf13.get_rect(bottomright=(960, 790))
            screen.blit(dog_surf13, dog_rect13)
            dog_surf15 = pygame.transform.scale(image7, (350, 350))
            dog_rect15 = dog_surf15.get_rect(bottomright=(1735, 895))
            screen.blit(dog_surf15, dog_rect15)
            dog_surf16 = pygame.transform.scale(image8, (300, 300))
            dog_rect16 = dog_surf16.get_rect(bottomright=(1463, 385))
            screen.blit(dog_surf16, dog_rect16)
            font = pygame.font.Font(None, 70)
            text = font.render("Your Profile:", True, (100, 255, 100))
            text_x = 800 - text.get_width() // 2
            text_y = 220 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            pygame.draw.rect(screen, (0, 255, 0), (text_x - 20, text_y - 80,
                                                   text_w + 40, text_h + 160), 3)
            font = pygame.font.Font(None, 30)
            text = font.render("press 'm' to return to the game", True, (255, 255, 255))
            text_x = 250 - text.get_width() // 2
            text_y = 770 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
        pygame.display.flip()
        if now > deadline:
            timer = pygame.time.get_ticks
            timeout = 3000 # milliseconds
            deadline = timer() + timeout
            cou += 2
            cou %= 26 * 14
            lst = make_bingo(cou)
        if now > deadline1:
            timeout1 = 5000
            deadline1 = timer() + timeout1
            can = 1
        if bosshp <= 0:
            running = False
            itog = 1
    running = True
    if itog == 1:
        gifFrameListbo = loadGIF(r"youwin.gif")
        a = 187
        b = 140
    else:
        gifFrameListbo = loadGIF(r"youlose.gif")
        a = 378
        b = 214
    currentFramebo = 0
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
        rectbo = gifFrameListbo[currentFramebo].get_rect(center = (a, b))
        bbo = pygame.transform.scale(gifFrameListbo[currentFramebo], (width, height))
        bbo.set_colorkey((255, 255, 255))
        screen.blit(bbo, rectbo)
        currentFramebo = (currentFramebo + 1) % len(gifFrameListbo)
        pygame.display.flip()

