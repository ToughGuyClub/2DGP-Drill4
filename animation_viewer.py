from pico2d import *

open_canvas()

Quagsire_walk=load_image('Walk-Anim.png')
Quagsire_idle=load_image('Idle-Anim.png')
Quagsire_shoot=load_image('Shoot-Anim.png')
Quagsire_sleep=load_image('Sleep-Anim.png')


def animation_walk():
    for n in range(0,500):
        frame = 0
        for x in range(4):
            clear_canvas()
            Quagsire_walk.clip_draw(frame*48,200,48,40,400,200,300,300)
            frame=(frame+1)%4
            update_canvas()
            delay(0.1)


# 여기를 채우세요.
while(True):
    clear_canvas()
    #그림 및 애니메이션
    animation_walk()

    update_canvas()
    delay(0.01)


close_canvas()

