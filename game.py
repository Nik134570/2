import os
import sys

import pygame

image = pygame.image.load('21.jpg')
image1 = pygame.image.load('39.png')
image2 = pygame.image.load('56.png')

class Board:
    colors = ["black", "white"]
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.size = 50

    def render(self, screen, d):
        if d == 1:
            dog_surf = pygame.transform.scale(image, (width, height))
            dog_rect = dog_surf.get_rect(bottomright=(width, height))
            screen.blit(dog_surf, dog_rect)
        else:
            pygame.draw.rect(screen, (0, 0, 0),
                                     (0, 0, width, height), 0)
        for j in range(0, self.width):
            for i in range(0, self.height):
                if self.board[i][j] == 1 and d == 0:
                    pygame.draw.rect(screen, (0, 0, 0),
                                     (i * self.size, j * self.size, self.size, self.size), 1)
                    dog_surf1 = pygame.transform.scale(image1, (48, 48))
                    dog_surf1.set_colorkey((255, 255, 255))
                    dog_rect1 = dog_surf1.get_rect(bottomright=(i * self.size + 49, j * self.size + 49))
                    screen.blit(dog_surf1, dog_rect1)
                elif self.board[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (i * self.size, j * self.size, self.size, self.size), 1)
                else:
                    pygame.draw.rect(screen, (0, 0, 0),
                                     (i * self.size, j * self.size, self.size, self.size), 1)
                    dog_surf1 = pygame.transform.scale(image2, (48, 48))
                    dog_surf1.set_colorkey((255, 255, 255))
                    dog_rect1 = dog_surf1.get_rect(bottomright=(i * self.size + 49, j * self.size + 49))
                    screen.blit(dog_surf1, dog_rect1)
        
                    

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

    def n(self):
        for j in range(0, self.width):
            for i in range(0, self.height):
                self.board[i][j] = 0

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    pygame.init()
    size = width, height =1800, 1000
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
    screen = pygame.display.set_mode(size)
    pygame.display.flip()
    board = Board(height // 50, width // 50)
    running = True
    d = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            running = False
        screen.fill((0, 0, 0))
        board.render(screen, 0)
        pygame.display.flip()
    running = True
    screen.fill((0, 0, 0))
    pygame.display.flip()
    while running == True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        board.render(screen, 1)
        pygame.display.flip()
