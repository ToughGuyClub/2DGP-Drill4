from pico2d import *

open_canvas()

Quagsire_walk=load_image('Walk-Anim.png')
Quagsire_idle=load_image('Idle-Anim.png')
Quagsire_shoot=load_image('Shoot-Anim.png')
Quagsire_sleep=load_image('Sleep-Anim.png')


def animation_walk():
    for n in range(0,5):
        for frame in range(4):
            clear_canvas()
            Quagsire_walk.clip_draw(frame*48,200,48,40,400,200,600,600)
            update_canvas()
            delay(0.1)

def animation_idle():
    for n in range(0,5):
        for frame in range(7):
            clear_canvas()
            Quagsire_idle.clip_draw(frame * 48, 398, 48, 56, 400, 200, 600, 600)
            update_canvas()
            delay(0.1)
def animation_shoot():
    for n in range(0,5):
        for frame in range(11):
            clear_canvas()
            Quagsire_shoot.clip_draw(frame * 48, 336, 44, 56, 400, 200, 600, 600)
            update_canvas()
            delay(0.1)

# 여기를 채우세요.
while(True):
    clear_canvas()
    #그림 및 애니메이션
    animation_walk()
    delay(1)
    animation_idle()
    delay(1)
    animation_shoot()
    update_canvas()
    delay(0.01)


close_canvas()

