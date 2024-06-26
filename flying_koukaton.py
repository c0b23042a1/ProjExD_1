import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_flp = pg.transform.flip(bg_img, True, False)
    kk = pg.image.load("fig/3.png")
    kk = pg.transform.flip(kk, True, False)
    kk_rct = kk.get_rect()      #こうかとんRectの抽出
    kk_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_flp, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bg_flp, [-x+4800, 0])
        key_lst = pg.key.get_pressed()
        tate = 0
        yoko = -1

        if key_lst[pg.K_UP]:
            tate = -1
            screen.blit(kk, kk_rct)
        if key_lst[pg.K_DOWN]:
            tate = 1
            screen.blit(kk, kk_rct)
        if key_lst[pg.K_LEFT]:
            yoko = -1
            screen.blit(kk, kk_rct)
        if key_lst[pg.K_RIGHT]:
            yoko = 2
            screen.blit(kk, kk_rct)
        kk_rct.move_ip(yoko, tate)
        screen.blit(kk, kk_rct)     #birdをbird_rctの設定に従って貼付け
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()