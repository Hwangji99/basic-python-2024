# date : 2024-02-05
# file : test36_pyqt.py
# desc : PyQt5 기본화면 만들기

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent, QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget
# print(sys.argv) # argv는 현재 파이썬 파일의 경로 표시

class qtwin_exam(QWidget): # Qwidget을 [상속]받는다는 뜻   # Qwidget이 가진 모든 것을 사용할 수 있다
    # 생성자
    def __init__(self) -> None: # 부모 = Qwidget # 나 = self # self는 Qwidget의 것을 사용할 수 있다
        super().__init__()
        self.initUI() # 화면 초기화 함수를 호출

    def initUI(self): # 화면 초기화 함수
        self.setGeometry((1920 - 400)//2, (1080 - 300)//2, 400, 300) # 화면비율   # 좌측 상단부터 0,0    # x, y, width, height    # x,y는 화면 위치   ## width, height는 화면크기
        self.setWindowTitle('Qt5 Hello World!')
        self.text = ''
        self.show()

    def drawText(self, event, paint):
        paint.setPen(QColor(10, 10, 10)) # dark gray # 0 ~ 255가지 색상   r,g,b = 0,0,0이면 black / r,g,b = 255,255,255이면 white
        paint.setFont(QFont('NanumGothic', 15))
        paint.drawText(300//2, 300//2, 'HELL WORLD!')
        paint.drawText(event.rect(), Qt.AlignLeft, self.text) # AlignLeft,AlignCenter,AlignRight

    def paintEvent(self, event) -> None: # 재정의(Override) # 부모의 정의를 다시 하는 것 
        paint = QPainter()
        paint.begin(self) # 열면
        self.drawText(event, paint)
        paint.end() # 닫는다
  

loop = QApplication(sys.argv) # 내 소스 위치로 앱을 생성
instance = qtwin_exam() # Qwidget을 상속한 qtwin_exam 객체를 생성
loop.exec_()