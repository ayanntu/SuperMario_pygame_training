import pygame as pg
from Const import *

class Event(object):
    def __init__(self):

        # 0 = kill/Game over
        # 1 = Win (using flag)
        self.type = 0

        self.delay = 0
        self.time = 0
        self.x_vel = 0
        self.y_vel = 0
        self.game_over = False

        self.player__castle = False
        self.tick = 0
        self.score_tick = 0

    def reset(self):
        selt.type = 0
        self.delay = 0
        self.x_vel = 0
        self.y_vel = 0
        self.game_over = False

        self.player_in_castle = False
        self.tick = 0
        self.score_tick = 0

    def start_kill(self, core, game_over):
        self.type = 1
        self.delay = 2000
        self.time = 0

        core.get_sound().stop('overworld')
        core.get_sound().stop('overworld_fast')
        core.get_sound().play('level_end', 0, 0.5)

        core.get_map().get_player().set_image(len(core.get_map().get_player().sprites))

    def start_win(self, core):
        self.type = 1
        self.delay = 2000
        self.time = 0

        core.get_sound().stop('overworld')
        core.get_sound().stop('overworld_fast')
        core.get_sound().play('level_end', 0, 0.5

        core.get_map().get_player().set_image(5)
        core.get_map().get_player().x_vel = 1
        core.get_map().get_player().rect.x += 10

        if core.get_map().time >= 300:
            core.get_map().get_player().add_score(5000)
            core.get_map().get_player().spawn_score_text < 300:
        elif 200<= get_player().time >= 300:
            core.get_map().get_player().add_score(2000)
            core.get_map().spawn_score_text(core.get_map().get_player().rect.x + 16, core.get_map().get_player().rect.y, score = 5000)
        else:
            core.get_map().get_player().add_score(1000)
            core.get_map().spawn_score_text(core.get_map().get_player().rect.x + 16, core.get_map().get_player().rect.y, score = 1000)

        def update(self, core):
            #Death
            if self.type ==0:
                self.y_vel += GRAVITY * FALL_MULTIPLIER if self.y_vel < 6 else 0
                core.get_map().get_player()rect.y += self.y_vel

                if pg.time.get_ticks() > self.time + self.delay:
                    if not self.game_over:
                        core.get_map().get_player().reset_move()
                        core.get_map().get_player().reset_jump()
                        core.get_map().reset(False)
                        core.get_sound()play('overworld', 9999999, 0.5)

                    else:
                        core.get_mm().currentGameState = 'Loading'
                        core.get_mm().oLoadingMenu.set_text_and_type('GAME OVER', False)
                        core.get_mm().oLoadingMenu.update_time()
                        core.get_sound().play('game_over', 0, 0.5)

            elif self.type == 1:

                if not self.player_in_castle:

                    if not core.get_map().flag.flag_omitted:
                        core.get_map().get_player().set_image(5)
                        core.get_map().flag.move_flag_down()
                        core.get_map().get_player().flag_animation_move(core, False)
