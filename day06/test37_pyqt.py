# date : 2024-02-05
# file : test37_pyqt.py
# desc : PyQt5 이벤트(Signal)

import sys
from PyQt5.QtCore import Qt # 사용한 것은 밝은 색, 안한 것은 어두운 색
from PyQt5.QtGui import QCloseEvent, QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class qtwin_exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        btn01 = QPushButton('클릭', self)
        btn01.setGeometry(50, 100, 100, 40) # 버튼의  Geometry
        btn01.clicked.connect(self.btn01_clicked) # 버튼을 클릭하면(시그널) btn_clicked 함수를 실행시키겠다

        self.setGeometry(300, 200, 400, 200)
        self.setWindowTitle('버튼 시그널')
        # self.show() # 37번 라인

    def btn01_clicked(self):
        QMessageBox.about(self, '버튼클릭', '버튼을 클릭했습니다!') # about(self, '박스제목', '내용')

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료확인', '종료할꺼야?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore() # 무시

if __name__ == '__main__': # Main Entry 확인조건 추가
    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    instance.show() # self.show 대신
    loop.exec_()


