import sqlite3

import pandas as pd


class ManagerDAO:
    def __init__(self, db_name='../server/db/data.db'):
        self.conn = sqlite3.connect(db_name)
    def insert_manager(self, **managers):
        """
        관리자 추가
        :param managers : 관리자 정보
        :return:
        """
        print(managers)
        df = pd.DataFrame(managers)
        df.to_sql('tb_manager', self.conn, if_exists='append', index=False)
        self.conn.commit()

    def get_all_manager(self):
        """
        관리자 정보 조회
        :return:
        """
        query = "SELECT * FROM tb_manager"
        df = pd.read_sql(query, self.conn)
        return df

    def get_manager_by_col(self, col, value):
        """
        관리자 정보 조건 조회
        :param col:
        :param value:
        :return:
        """
        query = f"SELECT * FROM tb_manager WHERE {col} = '{value}'"
        df = pd.read_sql(query, self.conn)
        return df

    def close_connection(self):
        """
        연결 종료
        :return:
        """
        self.conn.close()


if __name__ == "__main__":
    dao = ManagerDAO('../db/data.db')
    member_info = dao.insert_manager(id= ['test'], pw= ['test'], name= ['test'], depart= ['test'],position= ['test'],img= ['test'])
    dao.close_connection()
