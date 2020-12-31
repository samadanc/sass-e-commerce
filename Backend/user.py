class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __eq__(self, user2):
        return self.username == user2.get_username()

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password
