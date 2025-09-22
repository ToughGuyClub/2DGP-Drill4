from pico2d import *

open_canvas()

Quagsire_walk=load_image('Walk-Anim.png')
Quagsire_idle=load_image('Idle-Anim.png')
Quagsire_shoot=load_image('Shoot-Anim.png')
Quagsire_sleep=load_image('Sleep-Anim.png')

# 여기를 채우세요.
for x in range(0,800):
    clear_canvas()
    Quagsire_shoot.draw(400, 30)
    update_canvas()
    delay(0.01)


close_canvas()

