class notification:

    def get_notification(self):
        pass

class instagram(notification):

    def get_notification(self):
        print("notification from instagram")

class facebook(notification):

    def get_notification(self):
       print("notification from facebook")

instragram=instagram()
instragram.get_notification()