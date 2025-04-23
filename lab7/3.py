import pygame as pg

# Инициализациялау
pg.init()

# Экранды орнату
screen = pg.display.set_mode((700, 700))
clock = pg.time.Clock()

done = False

# Шардың бастапқы координаттары
x = 350
y = 350
radius = 25  # Радиус

while not done:
    screen.fill((255, 255, 255))  # Ақ фон

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    # Пайдаланушы басқан пернелерді алу
    keys = pg.key.get_pressed()

    # Жоғары
    if keys[pg.K_UP]:
        if y - radius - 20 >= 0:
            y -= 20
    # Төмен
    if keys[pg.K_DOWN]:
        if y + radius + 20 <= 700:
            y += 20
    # Солға
    if keys[pg.K_LEFT]:
        if x - radius - 20 >= 0:
            x -= 20
    # Оңға
    if keys[pg.K_RIGHT]:
        if x + radius + 20 <= 700:
            x += 20

    # Шарды сызу
    pg.draw.circle(screen, (255, 0, 0), (x, y), radius)

    clock.tick(60)  # FPS - 60
    pg.display.flip()  # Экранды жаңарту
