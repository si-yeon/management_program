import sqlite3
from datetime import datetime

import pandas as pd


class TakeOutDAO:
    def __init__(self, db_name='../server/db/data.db'):
        self.conn = sqlite3.connect(db_name)

    def insert_take_out(self, take_out_info: dict):
        """
        관리자 추가
        :param take_out_info : 로그 정보
        :return:
        """
        df = pd.DataFrame(take_out_info)
        df.to_sql('tb_take_out', self.conn, if_exists='append', index=False)
        self.conn.commit()

    def get_all_take_out(self):
        query = "SELECT * FROM tb_take_out"
        df = pd.read_sql(query, self.conn)
        return df

    def get_take_out_by_col(self, col, value):
        query = f"SELECT * FROM tb_take_out WHERE {col} = '{value}'"
        df = pd.read_sql(query, self.conn)
        return df

    def close_connection(self):
        self.conn.close()


if __name__ == "__main__":
    dao = TakeOutDAO()
    dao.close_connection()
