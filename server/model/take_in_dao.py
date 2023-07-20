import sqlite3
from datetime import datetime

import pandas as pd


class TakeInDAO:
    def __init__(self, db_name='../server/db/data.db'):
        self.conn = sqlite3.connect(db_name)

    def insert_take_in(self, take_in_info: dict):
        """
        관리자 추가
        :param take_in_info : 로그 정보
        :return:
        """
        df = pd.DataFrame(take_in_info)
        df.to_sql('tb_take_in', self.conn, if_exists='append', index=False)
        self.conn.commit()

    def get_all_take_in(self):
        query = "SELECT * FROM tb_take_in"
        df = pd.read_sql(query, self.conn)
        return df

    def get_take_in_by_col(self, col, value):
        query = f"SELECT * FROM tb_take_in WHERE {col} = '{value}'"
        df = pd.read_sql(query, self.conn)
        return df

    def close_connection(self):
        self.conn.close()


if __name__ == "__main__":
    dao = TakeInDAO()
    dao.close_connection()
