class ChatDTO:
    def __init__(self, chat: dict):
        self.no = chat['no']
        self.id = chat['id']
        self.content = chat['content']
        self.time = chat['time']

    def get_no(self):
        return self.no

    def set_no(self, no):
        self.no = no

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time



