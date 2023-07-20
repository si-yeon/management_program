from PyQt5.QtCore import QObject, pyqtSignal

class SignalController(QObject):
    # 입고
    take_in_signal = pyqtSignal()
    # 출고
    take_out_signal = pyqtSignal()
    # 추가
    add_signal = pyqtSignal()
    # 수정
    update_signal = pyqtSignal()
    # 삭제
    delete_signal = pyqtSignal()
    # 채팅
    chat_signal = pyqtSignal(str, str)
    # 상품 정보 업데이트
    product_signal = pyqtSignal(dict)
    # 타임라인
    timeline_siganl = pyqtSignal(str, str)

