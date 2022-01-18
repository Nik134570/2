import os
import sys

import pygame

class Board:
    colors = ["black", "white"]
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.size = 100

    def render(self, screen):
        for j in range(0, self.width):
            for i in range(0, self.height):
                if self.board[i][j] == 0:
                    pygame.draw.rect(screen, (255, 0, 0),
                                    (10 + i * self.size, 10 + j * self.size, self.size, self.size), 0)
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (10 + i * self.size, 10 + j * self.size, self.size, self.size), 1)
                elif self.board[i][j] == -1:
                    pygame.draw.rect(screen, (0, 0, 0),
                                     (10 + i * self.size, 10 + j * self.size, self.size, self.size), 0)
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (10 + i * self.size, 10 + j * self.size, self.size, self.size), 1)
                elif self.board[i][j] == 2:
                    pygame.draw.rect(screen, (0, 0, 0),
                                     (10 + i * self.size, 10 + j * self.size, self.size, self.size), 0)
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (10 + i * self.size, 10 + j * self.size, self.size, self.size), 1)
                    
                else:
                    global d
                    d = 0
                    pygame.draw.rect(screen, (0, 0, 255),
                                     (10 + i * self.size, 10 + j * self.size, self.size, self.size), 0)
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (10 + i * self.size, 10 + j * self.size, self.size, self.size), 1)

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
        self.board[x][y] = (self.board[x][y] + 1) % 3

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 553
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game over")
    running = True
    all_sprites = pygame.sprite.Group()
    MYEVENTTYPE = pygame.USEREVENT + 1
    pygame.time.set_timer(MYEVENTTYPE, 10)
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("D:/scale_13.jfif")
    all_sprites.add(sprite)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = -600
    sprite.rect.y = 0
    size = width, height = 800, 553
    screen = pygame.display.set_mode(size)
    pygame.display.flip()
    board = Board(5, 7)
    running = True
    d = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and d == 1:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    running = True
    while running:
        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MYEVENTTYPE:
                sprite.rect.x += 2
                sprite.rect.move(sprite.rect.x, 0)
            if sprite.rect.x >= 0:
                pygame.time.set_timer(MYEVENTTYPE, 0)
        pygame.display.flip()
