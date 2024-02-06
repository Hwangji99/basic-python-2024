# date : 2024-02-05
# file : test38_pyqt.py
# desc : Qt디자이너로 만든 ui와 연동

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qtwin_exam(QWidget): 
    def __init__(self) -> None: 
        super().__init__()
        uic.loadUi('./day06/TestApp.ui', self)  # QtDesigner에서 만든 ui를 불러옴
        # 버튼에 대한 시그널 처리
        self.btnstart.clicked.connect(self.btnStartClicked) # ui 파일 내에 있는 위젯접근은 VSCode상에서 색상으로 표시되지 않음
        self.btnstop.clicked.connect(self.btnStopClicked)

    def btnStartClicked(self):
        print('시작버튼 클릭')
        self.lblstatus.setText('상태 : 동작시작')
        QMessageBox.about(self, '동작', '시스템 가동~ 준비완료~')
    
    def btnStopClicked(self):
        print('종료버튼 클릭')
        self.lblstatus.setText('상태 : 동작중지')

    # QWidget에 있는 closeEvent를 그대로쓰면 그냥 닫힘
    # 닫을지 말지를 한번 더 물어보는 형태로 다시 구현하고 싶음(재정의 : Override)
    def closeEvent(self, QCloseEvent) -> None: # X버튼 종료확인(재정의)
        re = QMessageBox.question(self, '종료확인', '종료할꺼야?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore() # 무시

if __name__ == '__main__':
    loop = QApplication(sys.argv) 
    instance = qtwin_exam()
    instance.show()
    loop.exec_()

