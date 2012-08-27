import threading
from bloodyhell.resourceloader import ResourceLoader


class JukeBox(object):

    _instance = None

    def __new__(self):
        if self._instance is None:
            self._instance = object.__new__(self)
            self._instance.initialize()
        return self._instance

    def initialize(self):
        self._current_track = None
        self._current_track_name = None
        self._loop_timer = None

    def reload(self):
        if self._current_track is not None:
            self._current_track.stop()
            self._current_track.play()

    def play(self, track_name):
        return
        if self._current_track_name == track_name:
            return
        track = None
        try:
            track = ResourceLoader().get_raw_resource(track_name)
        except Exception, e:
            print e
            track = None
        if track is not None:
            if self._current_track is not None:
                self._current_track.stop()
                if self._timer:
                    self._timer.cancel()
            self._current_track_name = track_name
            self._current_track = track
            self._current_track.play()
            delay = self._current_track.get_length()
            self._timer = threading.Timer(delay, self.reload)
            self._timer.start()

