class UserDTO:
    def __init__(self, **kwargs):
        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'pw' in kwargs:
            self.pw = kwargs['pw']
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'nick' in kwargs:
            self.nick = kwargs['nick']
        if 'depart' in kwargs:
            self.depart = kwargs['depart']
        if 'position' in kwargs:
            self.position = kwargs['position']

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_pw_(self):
        return self.pw

    def set_pw_(self, pw):
        self.pw = pw

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_nick(self):
        return self.nick

    def set_nick(self, nick):
        self.nick = nick

    def get_depart(self):
        return self.depart

    def set_depart(self, depart):
        self.depart = depart

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position


