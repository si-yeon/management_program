my_dict = {'이름': '홍길동', '나이': 30, '성별': '남성'}

keys_to_get = ['이름', '나이']
values = [my_dict for key in keys_to_get]
print(values)  # 출력: ['홍길동', 30]
