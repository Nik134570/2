import os
from re import S
import sys

import pygame

image = pygame.image.load('D:/21.jpg')
image1 = pygame.image.load('D:/39.png')
image2 = pygame.image.load('D:/56.png')
image3 = pygame.image.load('D:/coin2.png')
image4 = pygame.image.load('D:/portal.png')
image5 = pygame.image.load('D:/bron1.png')
image6 = pygame.image.load('D:/меч1.png')
image7 = pygame.image.load('D:/ук.png')
image8 = pygame.image.load('D:/крылья.png')

all_sprites = pygame.sprite.Group()


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
        if d == 1:
            dog_surf = pygame.transform.scale(image, (width, height))
            dog_rect = dog_surf.get_rect(bottomright=(width, height))
            screen.blit(dog_surf, dog_rect)
            for i in range(18, 21):
                for j in range(5, 8):
                    pygame.draw.rect(screen, (0, 0, 0),
                                     (i * self.size, j * self.size, self.size, self.size), 1)
                    pygame.draw.line(screen, (0, 0, 0), (i * self.size + 1, j * self.size + 1), (i * self.size + 69, j * self.size + 69), 5)
                    pygame.draw.line(screen, (0, 0, 0), (i * self.size + 1, j * self.size + 69), (i * self.size + 69, j * self.size + 1), 5)
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (i * self.size, j * self.size, self.size, self.size), 1)
        else:
            pygame.draw.rect(screen, (0, 0, 0),
                                     (0, 0, width, height), 0)
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
                elif self.board[i][j] == 1 and d == 1:
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
        if d == 1:
            dog_surf10 = pygame.transform.scale(image4, (420, 210))
            dog_rect10 = dog_surf10.get_rect(bottomright=(23 * self.size - 35, 8 * self.size))
            screen.blit(dog_surf10, dog_rect10)




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

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, 
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

if __name__ == '__main__':
    def stat(x1, y1, p):
        for i in p:
            if i[0] == x1 and i[1] == y1:
                global coins
                coins += 1
                print(coins)
                n = p.index(i)
                del p[n]
    coins = 0
    pygame.init()
    size = width, height = 1820, 980
    screen = pygame.display.set_mode(size)
    board = Board(height // 70, width // 70)
    running = True
    d = 1
    s = 0
    gh = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
    while running == True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
                if event.key == pygame.K_j and x1 == 19 and y1 == 6:
                    running = False
                print(x1, y1)
                #19 6
        board.render(screen, 1)
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
    dragon = AnimatedSprite(load_image("D:/dragon_sheet8x2.png"), 8, 2, 50, 50)
    all_sprites.add(dragon)
    clock = pygame.time.Clock()
    MYEVENTTYPE = pygame.USEREVENT + 1
    pygame.time.set_timer(MYEVENTTYPE, 10)
    while running == True:
        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MYEVENTTYPE:
                dragon.update()
                pygame.display.flip()
        clock.tick(10)
        pygame.display.flip()
    pygame.quit()
