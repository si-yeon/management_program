import sqlite3

import pandas as pd


class ClothesDAO:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)

    def insert_member(self, **clothes):
        """
        관리자 추가
        :param clothes : 관리자 정보
        :return:
        """
        df = pd.DataFrame(clothes)
        df.to_sql('tb_clothes', self.conn, if_exists='append', index=False)
        self.conn.commit()

    def get_all_member(self):
        query = "SELECT * FROM tb_clothes"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()


