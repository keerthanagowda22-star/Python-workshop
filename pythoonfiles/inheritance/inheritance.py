class Mobile:
    def __init__(self):
        pass

    def calling(self):
        print("invoking calling function")

    def sms(self):
        print("invoking sms method")

    def games(self):
        print("invoking games")


class Vivo_v25(Mobile):
    def cam(self):
        print("invoking cam method")

    def video_calls(self):
        print("invoking video call method")


mob = Mobile()
vivo = Vivo_v25()

vivo.calling()
vivo.sms()
vivo.games()

vivo.cam()
vivo.video_calls()