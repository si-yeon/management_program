from datetime import datetime

from server.model.log_dao import LogDAO
from server.model.chat_dao import ChatDAO

class CommonController():
    def input_log(self, type, content):
        check_time = datetime.now()
        dao = LogDAO()
        dao.insert_log(type=[type], content=[content], tiem=[check_time])
        dao.close_connection()

    def input_chat(self, id_, content):
        check_time = datetime.now()
        dao = ChatDAO()
        dao.insert_chat(id=[id_], content=[content], tiem=[check_time])
        dao.close_connection()

