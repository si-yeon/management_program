import sqlite3
from datetime import datetime

import pandas as pd


class ProductDAO:
    def __init__(self, db_name='../server/db/data.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def insert_product(self, product: dict):
        """
        상품 추가
        :param product : 상품 정보
        :return:
        """
        check_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        product['add_time'] = check_time
        print(product)
        df = pd.DataFrame(product)
        df.to_sql('tb_product', self.conn, if_exists='append', index=False)
        self.conn.commit()

    def update_product(self, product: dict):
        """
        상품 수정
        :param product : 상품 정보
        :return:
        """
        check_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = f"""UPDATE tb_product SET
                    type = '{product['type']}',
                    brand = '{product['brand']}',
                    name = '{product['name']}',
                    purchase_unit_price = '{product['purchase_unit_price']}',
                    sales_unit_price = '{product['sales_unit_price']}',
                    safety_inventory = '{product['safety_inventory']}',
                    inventory = '{product['inventory']}',
                    img = '{product['img']}',
                    update_time = '{check_time}'
                    WHERE code = '{product['code']}'
                """
        self.cursor.execute(query)
        self.conn.commit()

    def delete_product(self, product: dict):
        """
        상품 삭제
        :param product : 상품 정보
        :return:
        """
        query = f"""DELETE FROM tb_product
                    WHERE code = {product['code']}
                """
        self.cursor.execute(query)
        self.conn.commit()

    def get_all_product(self):
        query = "SELECT * FROM tb_product"
        df = pd.read_sql(query, self.conn)
        df = df.fillna('')
        return df

    def get_product_by_col(self, col, value):
        query = f"SELECT * FROM tb_product WHERE {col} = '{value}'"
        df = pd.read_sql(query, self.conn)
        df = df.fillna('')
        return df

    def close_connection(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    dao = ProductDAO('../db/data.db')
    # dict_data = {'img': '1', 'code': 'test', 'type': '1', 'brand': '1', 'name': 'test', 'purchase_unit_price': 'test',
    #              'sales_unit_price': 'test', 'inventory': 'test', 'safety_inventory': 'test'}
    # dao.update_product(dict_data)
    dao.get_all_product()
    dao.close_connection()
    # dict_data = data.to_dict('records')
    # print(dict_data)
    # json_data = json.dumps(dict_data)
    # self.send_json_to_client('log' + self.header_split + json_data)
