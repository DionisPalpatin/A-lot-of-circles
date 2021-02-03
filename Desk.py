import pygame as pg
from random import randint


rad = 5
quantity = 200   #тут число точно должно быть кратно 4, потому что это высота (и ширина) в кругах, умноженная на 4
size = rad * 2 * quantity // 4


pg.init()
window = pg.display.set_mode((size, rad * 2 * 50), pg.SHOWN)
window.fill((255, 255, 255))


circles = {}
for i in range(quantity):
    circles[i] = {
        "coord" : rad + i % 100 % 50 * 10,
        "direction" : 1 - i // 100 * 2
    }
for i in range(quantity // 4):
    temporary = i * 2 * rad + rad   #ради уменьшения количества вычислений за один проход цикла
    pg.draw.circle(window, (randint(0, 254), randint(0, 254), randint(0, 254)), (temporary, temporary), rad)


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
        temporary = i % 100 % 50 * 2 * rad + rad    #и вновь ради уменьшения кол-ва вычислений за один проход цикла
        if not i // 50 % 2:
            pg.draw.circle(window, (randint(0, 254), randint(0, 254), randint(0, 254)), (circles[i]["coord"], temporary), rad)
        else:
            pg.draw.circle(window, (randint(0, 254), randint(0, 254), randint(0, 254)), (temporary, circles[i]["coord"]), rad)


    pg.display.update()
    pg.time.delay(10)
