class ClothesDTO:
    def __init__(self, **kwargs):
        """
        의류 속성
        :param code: 코드
        :param type: 분류(아우터, 상의, 바지, 신발, 잡화)
        :param brand: 브랜드
        :param name: 품목명
        :param purchase_unit_price: 구매단가
        :param sales_unit_price: 판매단가
        :param img: 이미지 경로
        :param inventory: 재고
        :param safety_inventory: 안전재고
        """
        if 'code' in kwargs:
            self.code = kwargs['code']
        if 'type' in kwargs:
            self.type = kwargs['type']
        if 'brand' in kwargs:
            self.brand = kwargs['brand']
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'purchase_unit_price' in kwargs:
            self.purchase_unit_price = kwargs['purchase_unit_price']
        if 'sales_unit_price' in kwargs:
            self.sales_unit_price = kwargs['sales_unit_price']
        if 'img' in kwargs:
            self.img = kwargs['img']
        if 'inventory' in kwargs:
            self.inventory = kwargs['inventory']
        if 'safety_inventory' in kwargs:
            self.safety_inventory = kwargs['safety_inventory']

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def get_division(self):
        return self.type

    def set_division(self, type):
        self.code = type

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_purchase_unit_price(self):
        return self.purchase_unit_price

    def set_purchase_unit_price(self, purchase_unit_price):
        self.purchase_unit_price = purchase_unit_price

    def get_sales_unit_price(self):
        return self.sales_unit_price

    def set_sales_unit_price(self, sales_unit_price):
        self.sales_unit_price = sales_unit_price

    def get_img(self):
        return self.img

    def set_img(self, img):
        self.img = img

    def get_inventory(self):
        return self.inventory

    def set_inventory(self, inventory):
        self.inventory = inventory

    def get_safety_inventory(self):
        return self.safety_inventory

    def set_safety_inventory(self, safety_inventory):
        self.safety_inventory = safety_inventory
