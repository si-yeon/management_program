from datetime import datetime

from server.model.chat_dao import ChatDAO
from server.model.log_dao import LogDAO


class CommonController():
    def input_log(self, type, content):
        """
        시스템 로그 기록
        :param type: 분류
        :param content: 내용
        :return:
        """
        check_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dao = LogDAO()
        dao.insert_log(type=[type], content=[content], time=[check_time])
        dao.close_connection()

    def input_chat(self, id, name, content):
        """
        채팅 기록
        :param id: 아이디
        :param content: 내용
        :return:
        """
        check_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dao = ChatDAO()
        dao.insert_chat(id=[id], name=[name], content=[content], time=[check_time])
        dao.close_connection()
