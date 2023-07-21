import json
import sqlite3

import pandas as pd

class ChatDAO:
    def __init__(self, db_name='../server/db/data.db'):
        self.conn = sqlite3.connect(db_name)

    def insert_chat(self, **chatinfo):
        """
        채팅 내용 추가
        :param chatinfo : 로그 정보
        :return:
        """
        df = pd.DataFrame(chatinfo)
        df.to_sql('tb_chat', self.conn, if_exists='append', index=False)
        self.conn.commit()

    def get_all_chat(self):
        query = "SELECT * FROM tb_chat"
        df = pd.read_sql(query, self.conn)
        return df

    def get_chat_by_col(self, col, value):
        query = f"SELECT * FROM tb_chat WHERE {col} = '{value}'"
        df = pd.read_sql(query, self.conn)
        return df

    def close_connection(self):
        self.conn.close()


if __name__ == "__main__":
    dao = ChatDAO('../db/data.db')
    data = dao.get_all_chat()
    dao.close_connection()

    reverse_data = data.iloc[::-1]

    max_fifty_data = reverse_data.iloc[:50]

    dict_data = max_fifty_data.to_dict('records')

    json_data = json.dumps(dict_data)





