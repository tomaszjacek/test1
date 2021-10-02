import sys
import pygame
import random

WIDTH = 800
HEIGHT = 600

class GameObject(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        if x == 0 and y ==0:
            x = random.randint(0, WIDTH - 100)
            y = random.randint(0, HEIGHT - 100)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def colliding(self, things):
        # This may be bad form and non-pythonic, not sure if I should have self
        # as an argument to the function call, or if there's a different way
        # of getting it to do this which is better practice.
        if pygame.sprite.spritecollideany(self, things):
            return True
        return False

class Alien(GameObject):
    def __init__(self, x=0, y=0):
        super().__init__("alien.png", x, y)
        self.velocity = [random.randint(-7, 7), random.randint(-7, 7)]

    def update(self):
        self.rect = self.rect.move(self.velocity)

        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.velocity[0] = -self.velocity[0]
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.velocity[1] = -self.velocity[1]

class Player(GameObject):
    def __init__(self, x=0, y=0):
        super().__init__("player.png", x, y)

    def reset(self):
        self.rect.topleft = (50, 50)

    def move_right(self):
        self.rect = self.rect.move((1, 0))
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def move_left(self):
        self.rect = self.rect.move((-1, 0))
        if self.rect.left < 0:
            self.rect.left = 0

    def move_up(self):
        self.rect = self.rect.move((0, -1))
        if self.rect.top < 0:
            self.rect.top = 0

    def move_down(self):
        self.rect = self.rect.move((0, 1))
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self, a_surface):
        a_surface.blit(self.image, self.rect)

class MainWindow:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(3, 3)
        self.player = Player(50, 50)

        self.aliens = pygame.sprite.Group()
        for _ in range(20):
            self.aliens.add(Alien())

        self.DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
        self.purple = (150, 0, 220)
        self.DISPLAYSURF.fill(self.purple)
        pygame.display.set_caption('Dodge the Aliens - Game Making Part 8')

        self.clock = pygame.time.Clock()
        self.time_counter = 0

    def main_game_loop(self):
        while True:
            self.time_counter += self.clock.tick()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.player.move_right()
                    if event.key == pygame.K_LEFT:
                        self.player.move_left()
                    if event.key == pygame.K_UP:
                        self.player.move_up()
                    if event.key == pygame.K_DOWN:
                        self.player.move_down()

            if self.time_counter > 15:
                print(self.time_counter)
                self.DISPLAYSURF.fill(self.purple)

                self.aliens.update()
                if self.player.colliding(self.aliens):
                    self.player.reset()

                self.aliens.draw(self.DISPLAYSURF)
                self.player.draw(self.DISPLAYSURF)

                self.time_counter = 0
            pygame.display.update()

game = MainWindow()
game.main_game_loop()