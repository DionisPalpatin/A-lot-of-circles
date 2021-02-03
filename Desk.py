import pygame as pg
from random import randint


rad = 5
size = rad * 2 * 50
quantity = 200


pg.init()
window = pg.display.set_mode((size, rad * 2 * 50), pg.SHOWN)
window.fill((255, 255, 255))


circles = {}
for i in range(quantity):
    circles[i] = {
        "coord" : rad + i % 100 % 50 * 10,
        "direction" : 1 - i // 100 * 2
    }
for i in range(50):
    pg.draw.circle(window, (randint(0, 254), randint(0, 254), randint(0, 254)), (i * 2 * rad + rad, i * 2 * rad + rad), rad)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()


    for i in range(quantity):
        if not (rad - 1 < circles[i]["coord"] < size - rad + 1):
            circles[i]["direction"] *= -1
        circles[i]["coord"] += 1 * circles[i]["direction"]
    

    window.fill((255, 255, 255))
    for i in range(quantity):
        if not i // 50 % 2:
            pg.draw.circle(window, (randint(0, 254), randint(0, 254), randint(0, 254)), (circles[i]["coord"], i % 100 % 50 * 2 * rad + rad), rad)
        else:
            pg.draw.circle(window, (randint(0, 254), randint(0, 254), randint(0, 254)), (i % 100 % 50 * 2 * rad + rad, circles[i]["coord"]), rad)


    pg.display.update()
    pg.time.delay(10)