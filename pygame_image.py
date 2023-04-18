import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img_lst = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)]

    tmr = 0
    kk_idx = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1

        bg_x_count = tmr % 1600
        screen.blit(bg_img, [-bg_x_count, 0])
        screen.blit(bg_img, [1600 - bg_x_count, 0])

        if tmr % 100 == 0:
            kk_idx = (kk_idx + 1) % len(kk_img_lst)

        screen.blit(kk_img_lst[kk_idx], [300, 200])

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()