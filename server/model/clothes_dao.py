import json
import sqlite3

import pandas as pd


class ClothesDAO:
    def __init__(self, db_name='../server/db/data.db'):
        self.conn = sqlite3.connect(db_name)

    def insert_clothes(self, **clothes):
        """
        관리자 추가
        :param clothes : 관리자 정보
        :return:
        """
        df = pd.DataFrame(clothes)
        df.to_sql('tb_clothes', self.conn, if_exists='append', index=False)
        self.conn.commit()

    def get_all_clothes(self):
        query = "SELECT * FROM tb_clothes"
        df = pd.read_sql(query, self.conn)
        return df

    def get_clothes_by_col(self, col, value):
        query = f"SELECT * FROM tb_clothes WHERE {col} = '{value}'"
        df = pd.read_sql(query, self.conn)
        return df

    def close_connection(self):
        self.conn.close()

if __name__ == '__main__':
    dao = ClothesDAO('../db/data.db')
    data = dao.get_all_clothes()
    dao.close_connection()

    dict_data = data.to_dict('records')

    print(dict_data)
    json_data = json.dumps(dict_data)

    # self.send_json_to_client('log' + self.header_split + json_data)
