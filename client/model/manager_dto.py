class UserDTO:
    def __init__(self, **kwargs):
        if 'id_' in kwargs:
            self.id_ = kwargs['id_']
        if 'pw_' in kwargs:
            self.pw_ = kwargs['pw_']
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'nick' in kwargs:
            self.nick = kwargs['nick']
        if 'depart' in kwargs:
            self.depart = kwargs['depart']
        if 'position' in kwargs:
            self.position = kwargs['position']

    def get_id_(self):
        return self.id_

    def set_id_(self, id_):
        self.id_ = id_

    def get_pw_(self):
        return self.pw_

    def set_pw_(self, pw_):
        self.pw_ = pw_

    def get_id(self):
        return self.name

    def set_id(self, name):
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


