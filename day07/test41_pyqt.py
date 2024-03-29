# date : 2024-02-06
# file : test41_pyqt.py
# desc : PyQt5 이미지 뷰어

import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        
        pixmap = QPixmap('./images/뭘보노.jpg'). scaledToWidth(600) # 이미지 추가 .scaleToWidth(800) 큰 해상도를 800으로 고정
        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)

        lblSize = QLabel(self)
        lblSize.setFont(QFont('NanumGothicCoding', 20)) # 폰트와 폰트사이즈
        lblSize.setStyleSheet('Color : blue;')
        lblSize.setText(f'{pixmap.width()} X {pixmap.height()}') # 사진의 width x height
        lblSize.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) # 가로중앙정렬 | 세로중앙정렬

        vbox = QVBoxLayout(self) # QtDesigner VerticalLayout 위젯 생성
        vbox.addWidget(lblImage) # VL에 위젯 추가
        vbox.addWidget(lblSize)
        self.setLayout(vbox) # Form에 VL 추가
    
    
    
        self.setWindowIcon(QIcon('./images/iot.png')) # 실행 시 좌측 상단에 나오는 아이콘
        self.setWindowTitle('이미지 뷰어')
        rect = QRect(300, 300, 300, 300) # x, y, w, h
        self.setGeometry(rect) # 같은 이름의 함수를 여러 개 선언해놓고 원하는 것을 골라쓰는 BR(오버로딩)
        # self.setGeometry(300, 300, 300, 300)
        self.setCenter()
        self.show()                 # showFullScreen()는 모니터를 꽉 채워서 출력
    
    def setCenter(self): ## 윈앱을 화면 정중앙에 위치
        gm = self.frameGeometry() # 윈앱 자신 위치값
        cp = QDesktopWidget().availableGeometry().center() # 모니터의 정중앙 값
        gm.moveCenter(cp)
        self.move(gm.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen_rect = app.desktop().screenGeometry() # 모니터 해상도 구하는 법
    width, height = screen_rect.width(), screen_rect.height()
    print(width, 'x', height) # 활용도 높음
    ins = WinApp()
    sys.exit(app.exec_()) # 종료시 리소스 반환 등 효율을 위함

