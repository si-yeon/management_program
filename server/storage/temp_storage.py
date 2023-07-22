class TempStorage:
    # 서버 포트
    serverport = 5000
    # 클라이언트 접속 제한
    max_clients = 10
    # 구분자
    header_split = chr(1)  # 
    split_1 = chr(2)  # 
    split_2 = chr(3)  # 
    # 접속한 클라이언트
    clients = []
    # 방 리스트
    room_list = []
    # 이미지 정보
    image_data = b""
