class ShareBehavior:
    @staticmethod
    def share():
        print('sharing basic')


class ShareFb(ShareBehavior):
    @staticmethod
    def share():
        print('sharing to fb')


class ShareIg(ShareBehavior):
    @staticmethod
    def share():
        print('sharing to ig')


class PhoneCameraApp:
    shareBehavior = None

    def setShareBehavior(self, sb):
        self.shareBehavior: ShareBehavior = sb

    def take(self):
        return 'taking photo'

    def edit(self):
        return 'editing'

    def save(self):
        return 'saving'

    def performShare(self):
        self.shareBehavior.share()


class BasicCameraApp(PhoneCameraApp):
    def __init__(self) -> None:
        self.setShareBehavior(ShareFb)

    def edit(self):
        return 'editing for poor people'


class CameraAppPlus(PhoneCameraApp):
    def __init__(self) -> None:
        self.setShareBehavior(ShareIg)

    def edit(self):
        return 'editing for rich people'


if __name__ == '__main__':
    basic = BasicCameraApp()
    plus = CameraAppPlus()
    basic.performShare()
    plus.performShare()
