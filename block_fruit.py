import pygame
import random

# 1)初始化 Pygame
pygame.init()

# 2)設定遊戲視窗大小
window_width = 800
window_height = 600

# 3)定義顏色
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# 4)創建遊戲視窗
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("block eat fruit")

# 5)設定遊戲時鐘
clock = pygame.time.Clock()

# 6)定義方塊類別
class Block(pygame.sprite.Sprite):
    
    # 6.1)定義初始化函式
    def __init__(self):
        super().__init__()
        self.size = 50
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.center = (window_width // 2, window_height // 2)
        self.speed = 5
        self.dx = 0
        self.dy = 0
    
    # 6.2)定義更新函式
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # 6.2.1)檢查是否碰到邊界
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > window_width:
            self.rect.right = window_width
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > window_height:
            self.rect.bottom = window_height

# 7)定義果實類別
class Fruit(pygame.sprite.Sprite):
    
    # 7.1)定義初始化函式
    def __init__(self):
        super().__init__()
        self.size = 30
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.reset = 0

    # 7.2)定義更新函式
    def update(self):
        if self.reset == 1:
            self.rect.x = random.randint(0, window_width - self.size)
            self.rect.y = random.randint(0, window_height - self.size)
            self.reset = 0

# 8)創建方塊和果實精靈群組
all_sprites = pygame.sprite.Group()
block = Block()
fruit = Fruit()
all_sprites.add(block, fruit)

# 9)設定初始計分和計分標籤
score = 0
font = pygame.font.Font(None, 36)

# 10)遊戲主迴圈
running = True
while running:
    
    # 10.1)檢查使用者輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                block.dy = -block.speed
            elif event.key == pygame.K_DOWN:
                block.dy = block.speed
            elif event.key == pygame.K_LEFT:
                block.dx = -block.speed
            elif event.key == pygame.K_RIGHT:
                block.dx = block.speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                block.dy = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                block.dx = 0

    # 10.2)更新精靈群組
    all_sprites.update()

    # 10.3)檢查是否吃到果實
    if pygame.sprite.collide_rect(block, fruit):
        fruit.reset = 1
        score += 1

    # 10.4)繪製遊戲畫面
    window.fill(white)  # 填滿白色背景
    all_sprites.draw(window)  # 繪製精靈群組

    # 10.5)繪製計分標籤
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    window.blit(score_text, (10, 10))

    # 10.6)更新遊戲畫面
    pygame.display.flip()

    clock.tick(60)  # 控制遊戲速度

# 11)關閉遊戲視窗並結束程式
pygame.quit()
