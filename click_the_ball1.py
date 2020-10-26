import pygame
import random
import numpy as np


FPS = 10
N = 8
'''
N - число шаров
'''
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (105, 105, 105)
X_SHIFT = 45
Y_SHIFT = 320


class Balls():
    '''
    класс, в котором хранятся все шары
    '''
    def __init__(self, n_balls):
        self.n_balls = n_balls
        '''
        self.n_balls - число создаваемых шаров
        '''
        self.balls = list([[random.randint(52, 948), random.randint(52, 548),
                            random.randint(10, 50), (random.randint(0, 255),
                            random.randint(0, 255), random.randint(0, 255)), 0] for i in range(n_balls)])
        '''
        self.balls: создаёт массив шаров: массив списков со случ. [коорд. х, коорд. у, радиус, цвет RGB, порван ли (не случ.)]
        '''
        self.velocities = list([[random.randint(-50, 50), random.randint(-50, 50)] for i in range(n_balls)])
        '''
        self.velocities: массив скоростей шаров из списоков со случ. [скорость по х, скорость по у]
        '''
    def iterate(self, tick):
        '''
        метод обновления шаров
        '''
        for i, ball in enumerate(self.balls):
            if self.balls[i][4] == 0:
                '''
                если шарик не порван собачкой
                '''
                for k in range(2):
                    self.balls[i][k] += int(self.velocities[i][k] * tick)
                if self.balls[i][0] < 2 + self.balls[i][2]:
                    self.velocities[i][0] *= (-1)
                if self.balls[i][0] > 998 - self.balls[i][2]:
                    self.velocities[i][0] *= (-1)
                if self.balls[i][1] < 2 + self.balls[i][2]:
                    self.velocities[i][1] *= (-1)
                if self.balls[i][1] > 598 - self.balls[i][2]:
                    self.velocities[i][1] *= (-1)

    def draw(self, screen):
        '''
        метод рисования шаров
        '''
        for ball in self.balls:
            pygame.draw.circle(screen, ball[3], (ball[0], ball[1]), ball[2])


score = 0
'''
cчёт изначально нулевой
'''

class Dog():
    '''
    класс собачки
    '''
    def __init__(self):
        self.x_pos = random.randint(52, 948)
        '''
        рандомная координата x
        '''
        self.y_pos = random.randint(52, 548)
        '''
        рандомная координата y
        '''
        self.punished = 5
        '''
        наказали ли мы собачку за то, что она лопает шарики
        '''
    def jump(self, x_dir, y_dir):
        '''
        cобачка прыгает в сторону точки (x_dir, y_dir)
        '''
        x = x_dir - self.x_pos
        y = y_dir - self.y_pos
        self.x_pos += int(x / np.sqrt(x**2 + y**2) * 20)
        self.y_pos += int(y / np.sqrt(x**2 + y**2) * 20)
    def draw(self, size=1, reflect=False):
        """
        рисуем собачку
        dog -- draws a dog with the left upper corner at (x, y).
        size provides adjusting of the image scale (1 means equal to origin)
        reflect is a bool for flipping vertically
        """
        surface = pygame.Surface([135, 135], pygame.SRCALPHA)
        pygame.draw.ellipse(surface, GREY, [50 - X_SHIFT, 360 - Y_SHIFT, 20, 50], 0)
        pygame.draw.ellipse(surface, GREY, [90 - X_SHIFT, 380 - Y_SHIFT, 20, 50], 0)
        pygame.draw.ellipse(surface, GREY, [40 - X_SHIFT, 406 - Y_SHIFT, 30, 10], 0)
        pygame.draw.ellipse(surface, GREY, [80 - X_SHIFT, 426 - Y_SHIFT, 30, 10], 0)
        pygame.draw.ellipse(surface, GREY, [55 - X_SHIFT, 345 - Y_SHIFT, 90, 45], 0)
        pygame.draw.ellipse(surface, GREY, [117 - X_SHIFT, 345 - Y_SHIFT, 30, 30], 0)
        pygame.draw.ellipse(surface, GREY, [140 - X_SHIFT, 357 - Y_SHIFT, 30, 30], 0)
        pygame.draw.ellipse(surface, GREY, [122 - X_SHIFT, 345 - Y_SHIFT, 45, 30], 0)
        pygame.draw.ellipse(surface, GREY, [132 - X_SHIFT, 360 - Y_SHIFT, 10, 40], 0)
        pygame.draw.ellipse(surface, GREY, [162 - X_SHIFT, 377 - Y_SHIFT, 10, 40], 0)
        pygame.draw.ellipse(surface, GREY, [118 - X_SHIFT, 397 - Y_SHIFT, 20, 8], 0)
        pygame.draw.ellipse(surface, GREY, [148 - X_SHIFT, 414 - Y_SHIFT, 20, 8], 0)
        pygame.draw.rect(surface, GREY, (55 - X_SHIFT, 330 - Y_SHIFT, 50, 50), 0)
        pygame.draw.polygon(surface, WHITE, [(68 - X_SHIFT, 360 - Y_SHIFT), (71 - X_SHIFT, 372 - Y_SHIFT),
                                         (65 - X_SHIFT, 372 - Y_SHIFT)], 0)
        pygame.draw.polygon(surface, WHITE, [(91 - X_SHIFT, 360 - Y_SHIFT), (94 - X_SHIFT, 372 - Y_SHIFT),
                                         (88 - X_SHIFT, 372 - Y_SHIFT)], 0)
        pygame.draw.polygon(surface, BLACK, [(68 - X_SHIFT, 360 - Y_SHIFT), (71 - X_SHIFT, 372 - Y_SHIFT),
                                         (65 - X_SHIFT, 372 - Y_SHIFT)], 1)
        pygame.draw.polygon(surface, BLACK, [(91 - X_SHIFT, 360 - Y_SHIFT), (94 - X_SHIFT, 372 - Y_SHIFT),
                                         (88 - X_SHIFT, 372 - Y_SHIFT)], 1)
        pygame.draw.ellipse(surface, GREY, [65 - X_SHIFT, 365 - Y_SHIFT, 30, 20], 0)
        pygame.draw.rect(surface, BLACK, (55 - X_SHIFT, 330 - Y_SHIFT, 50, 50), 1)
        pygame.draw.ellipse(surface, GREY, [47 - X_SHIFT, 330 - Y_SHIFT, 12, 14], 0)
        pygame.draw.ellipse(surface, GREY, [101 - X_SHIFT, 330 - Y_SHIFT, 12, 14], 0)
        pygame.draw.ellipse(surface, BLACK, [47 - X_SHIFT, 330 - Y_SHIFT, 12, 14], 1)
        pygame.draw.ellipse(surface, BLACK, [101 - X_SHIFT, 330 - Y_SHIFT, 12, 14], 1)
        pygame.draw.arc(surface, BLACK, [65 - X_SHIFT, 365 - Y_SHIFT, 30, 20], 0, 3.14, 1)
        pygame.draw.ellipse(surface, WHITE, [65 - X_SHIFT, 345 - Y_SHIFT, 12, 6], 0)
        pygame.draw.ellipse(surface, BLACK, [65 - X_SHIFT, 345 - Y_SHIFT, 12, 6], 1)
        pygame.draw.ellipse(surface, BLACK, [69 - X_SHIFT, 346 - Y_SHIFT, 4, 4], 0)
        pygame.draw.ellipse(surface, WHITE, [83 - X_SHIFT, 345 - Y_SHIFT, 12, 6], 0)
        pygame.draw.ellipse(surface, BLACK, [83 - X_SHIFT, 345 - Y_SHIFT, 12, 6], 1)
        pygame.draw.ellipse(surface, BLACK, [87 - X_SHIFT, 346 - Y_SHIFT, 4, 4], 0)
        surface_refl = pygame.transform.flip(surface, reflect, False)
        surface_mod = pygame.transform.scale(surface_refl, (int(size * 135), int(size * 135)))
        screen.blit(surface_mod, [self.x_pos, self.y_pos])
    def catch(self, Balls):
        """
        функция ловли собачкой мячика
        аргументы -- класс самой собачки, экземпляр класса Balls
        """
        for i, ball in enumerate(Balls.balls):
            if np.sqrt((ball[0] + ball[2] - self.x_pos - 40)**2 + (ball[1] + ball[2] - self.y_pos - 40)**2) < 40: #если собачка догнала шарик
                global score
                score -= 1
                '''
                теряем очко
                '''
                Balls.balls[i][4] = 1
                '''
                шарик лопается((((((((((
                '''
                Balls.balls[i][2] = 0
                Balls.balls[i][0] = 0
                Balls.balls[i][1] = 0
    def punish(self, click):
        '''
        проверка удачности наказания
        '''
        if click.pos[0] < 100 + self.x_pos:
            '''
            попали ли по псу по оси х
            '''
            if click.pos[1] < 80 + self.y_pos:
                '''
                попали ли по псу по оси y
                '''
                self.punished += 1
                '''
                если попали, псина наказана
                '''
            
pygame.init()
screen = pygame.display.set_mode((1000, 600))
'''
1000, 600 - размер игрового экрана
'''
screen.fill(WHITE)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

balls = Balls(N)
'''
создаём N шаров
'''
dog = Dog()

while not finished:
    clock.tick(FPS)
    '''
    Мориарти: "Часики тик-так, тик-так"
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            with open('D:\Машулька\players_results.txt', 'w') as file:
                file.write('Player' + str(random.randint(0, 1000)) + ' ' + str(score))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            '''
            если кликнули
            '''
            for ball in balls.balls: 
                if np.sqrt((ball[0] - event.pos[0])**2 + (ball[1] - event.pos[1])**2) < ball[2]:
                    score += 1
                    '''
                    если попали - очко в вашу пользу
                    '''
                if dog.punished < 5:
                    dog.punish(event)
                print(dog.punished)

    string = 'SCORE: ' + str(score)
    '''
    вывод счёта
    '''
    f1 = pygame.font.Font(None, 50)
    text1 = f1.render(string, 1, (0, 0, 0))
    screen.blit(text1, [500, 0])

    balls.iterate(0.3)
    '''
    обновляем шары
    '''
    
    balls.draw(screen)
    '''
    отрисовка новых шаров
    '''

    if score % 10 == 5:
        num = list(enumerate(balls.balls))
        rand = random.randint(0, N - 1)
        while num[rand][1][4] == 1:
            rand = random.randint(0, N - 1)

    if score % 20 == 10:
        if dog.punished == 5:
            dog.punished = 0
            dog.draw()

    if score % 20 > 10:
        x_dir = num[rand][1][0]
        y_dir = num[rand][1][1]
        if dog.punished < 5:
            dog.catch(balls)
            dog.jump(x_dir, y_dir)
            dog.draw()
        
    pygame.display.flip()
    screen.fill(WHITE)
    
pygame.quit()
