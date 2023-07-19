import sqlite3

import pandas as pd


class LogDAO:
    def __init__(self, db_name='../server/db/data.db'):
        self.conn = sqlite3.connect(db_name)

    def insert_log(self, **loginfo):
        """
        관리자 추가
        :param loginfo : 로그 정보
        :return:
        """
        df = pd.DataFrame(loginfo)
        df.to_sql('tb_log', self.conn, if_exists='append', index=False)
        self.conn.commit()

    def get_all_log(self):
        query = "SELECT * FROM tb_log"
        df = pd.read_sql(query, self.conn)
        return df

    def get_log_by_col(self, col, value):
        query = f"SELECT * FROM tb_log WHERE {col} = '{value}'"
        df = pd.read_sql(query, self.conn)
        return df

    def close_connection(self):
        self.conn.close()


if __name__ == "__main__":
    dao = LogDAO()
    dao.insert_log(type=['login'], content=['test'], time=['test'])
    df = dao.get_all_log()
    dao.close_connection()
    print(df)
