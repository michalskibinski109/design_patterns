
class State:
    def pause(self, mediaPlayer):
        print('i am already paused')

    def play(self, mediaPlayer):
        print('i am already playing')

    def stop(self, mediaPlayer):
        print('i am already stopped')


class MediaPlayer:
    def __init__(self) -> None:
        self.state: State = StoppedState()

    def set_state(self, state):
        self.state = state

    def play(self):
        self.state.play(self)

    def pause(self):
        self.state.pause(self)

    def stop(self):
        self.state.stop(self)


class PausedState(State):
    def play(self, mediaPlayer: MediaPlayer):
        mediaPlayer.set_state(PlayingState())
        print('la la la what a terrific song')

    def stop(self, mediaPlayer: MediaPlayer):
        mediaPlayer.set_state(StoppedState())
        print('stopped')


class PlayingState(State):
    def pause(self, mediaPlayer: MediaPlayer):
        mediaPlayer.set_state(PausedState())
        print('paused. . .')

    def stop(self, mediaPlayer: MediaPlayer):
        mediaPlayer.set_state(StoppedState())
        print('stopped. . .')


class StoppedState(State):
    def play(self, mediaPlayer: MediaPlayer):
        mediaPlayer.set_state(PlayingState())
        print('la la la what a terrific song')


player = MediaPlayer()
player.play()
player.pause()
player.stop()
player.stop()
