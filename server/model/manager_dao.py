import sqlite3

import pandas as pd


class ManagerDAO:
    def __init__(self, db_name='../db/data.db'):
        print("오니?")
        self.conn = sqlite3.connect(db_name)
    def insert_manager(self, **managers):
        """
        관리자 추가
        :param managers : 관리자 정보
        :return:
        """
        df = pd.DataFrame(managers)
        df.to_sql('tb_manager', self.conn, if_exists='append', index=False)
        self.conn.commit()

    def get_all_manager(self):
        query = "SELECT * FROM tb_manager"
        df = pd.read_sql(query, self.conn)
        return df

    def get_manager_by_col(self, col, value):
        query = f"SELECT * FROM tb_manager WHERE {col} = '{value}'"
        df = pd.read_sql(query, self.conn)
        return df

    def close_connection(self):
        self.conn.close()


if __name__ == "__main__":
    dao = ManagerDAO()
