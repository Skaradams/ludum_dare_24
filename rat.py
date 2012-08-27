from bloodyhell.world.actor import Actor
from platforms.hurtingfloor import *
from jukebox import JukeBox
from bloodyhell.resourceloader import ResourceLoader

class Rat(Actor):

    def __init__(self, position, level, evolution='rat', size=None, base_height=None, track='music.im_gonna_change'):
       
        if size == None:

            size = ResourceLoader().get_width_from_ratio('rat.stance_01', base_height)

        super(Rat, self).__init__(
            evolution, 'stance', (position[0], position[1]), size
        )

        self._level = level
        self._walk_vel = 5.0
        self._jump_vel = 17.5

        self._run_multiple = 1
        self._x_vel = 0

        self._right_on = False
        self._left_on = False

        self._orientation = "right"
        self._pace = "stance"
        self._running = False
        self.listen_key('right')
        self.listen_key('left')
        self.listen_key('space')
        self.listen_key('lshift')
        self.set_hitbox({'left': 17.5, 'top': 3.0})
        JukeBox().play(track)


    def update(self):
        super(Rat, self).update()
        if self._right_on == self._left_on:
            self._x_vel = 0
        elif self._right_on:
            self._x_vel = self._walk_vel
        elif self._left_on:
            self._x_vel = -self._walk_vel
        self.set_x_velocity(self._x_vel * self._run_multiple)

    def on_right_pressed(self):
        self._right_on = True
        if self._pace != "jump":
            if self._left_on:
               self._pace = "stance"
            else:
                if self._pace == "stance" and self._running:
                    self._pace = "run"
                else:
                    self._pace = "walk"

            if not self._left_on:
                self._orientation = "right"
            else:
                self._orientation = "left"
        self.animate()

    def on_right_released(self):
        self._right_on = False
        if self._pace != "jump":
            if self._left_on:
                self._orientation = "left"
                if self._running:
                    self._pace = 'run'
                else:
                    self._pace = 'walk'
            else:
                self._pace = "stance"
        self.animate()

    def on_left_pressed(self):
        print self
        self._left_on = True

        if self._pace != "jump":
            if self._right_on:
               self._pace = "stance"
            else:
                if self._pace == "stance" and self._running:
                    self._pace = "run"
                else:
                    self._pace = "walk"

            if not self._right_on:
                self._orientation = "left"
            else:
                self._orientation = "right"
        self.animate()

    def on_left_released(self):
        self._left_on = False
        if self._pace != "jump":
            if self._right_on:
                self._orientation = "right"
                if self._running:
                    self._pace = 'run'
                else:
                    self._pace = 'walk'
            else:
                self._pace = "stance"
        self.animate()

    def on_space_pressed(self):
        if self.get_y_velocity() < 0.001 and self.get_y_velocity() > -0.001:
            self._pace = 'jump'
            self.set_y_velocity(self._jump_vel)
            self.animate()

    def on_space_released(self):
        if self.get_y_velocity() > 0.001:
            self.set_y_velocity(0.01)

    def on_lshift_pressed(self):
        self._run_multiple = 4
        self._running = True
        if self._right_on or self._left_on:
            self._pace = 'run'
        self.animate()

    def on_lshift_released(self):
        self._run_multiple = 1
        self._running = False

        self.animate()

    def on_collision(self, chunk, point):
        spades = [SpadesDown, SpadesUp, SpadesLeft, SpadesRight]
        if chunk.__class__ in spades:
            self._level.reset(self._level.resolution(), self._level.navigator())
        else:
            if not self._right_on and not self._left_on:
                self._pace = 'stance'
            elif self._running:
                self._pace = 'run'
            elif self._right_on or self._left_on:
                self._pace = 'walk'
            self.animate()

    def animate(self):
        if self._orientation == "left":
            self.loop(self._pace+"_left")
        else:
            self.loop(self._pace)
