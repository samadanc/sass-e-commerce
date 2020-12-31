from Backend.user import User


class Buyer(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def __str__(self):
        return self.username + "," + self.password + "," + str(self.is_seller())

    def is_seller(self):
        return False
