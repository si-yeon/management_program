class TemporaryStorage:
    info = {'id': [],
            'name':[],
            'socket': [],
            'connect': [False]}

    header_split = chr(1)
    split_1 = chr(2)
    split_2 = chr(3)


if __name__ == '__main__':
    t = TemporaryStorage()
    print(t.header_split)
    print(t.split_1)
    print(t.split_2)