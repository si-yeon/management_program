my_dict = {'apple': 1, 'banana': 2, 'orange': 3}

# 딕셔너리의 키와 값을 enumerate 함수를 사용하여 인덱스와 함께 출력
for index, (key, value) in enumerate(my_dict.items()):
    print(f"Index: {index}, Key: {key}, Value: {value}")