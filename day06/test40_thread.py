# date : 2024-02-05
# file : test40_thread.py
# desc : Qt에서 스레드로 동작
# 스레드는 프로세스 하나당 여러 스레드로 나눠서(동시에) 실행하는 것
# 백그라운드 워커 -> UI스레드가 한번에 일을 처리 못해 병렬로 나눠주는 것
import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class BackWorker(QThread): # PyQt에서 스레드 클래스 상속
    initSignal = pyqtSignal(int) # 시그널을 UI스레드로 전달하기 위한 변수 객체
    setSignal = pyqtSignal(int)
    setLog = pyqtSignal(str)

    def __init__(self, parent) -> None:
        super().__init__(parent) # 부모 스레드에 있는 초기화 사용
        self.parent = parent # BackWorker에서 사용할 멤버변수

    def run(self) -> None: # 스레드 실행 -> run
        # 스레드로 동작할 내용
        maxval = 1000001
        self.initSignal.emit(maxval)
        ### self.parent.pgbTask.setValue(0) # QThread에선 UI 관련된 처리를 할 수 없음
        ### self.parent.pgbTask.setRange(0, maxval-1)
        for i in range(maxval):
            print_str = f'쓰레드 출력 >> {i}'
            print(print_str)
            self.setSignal.emit(i)
            self.setLog.emit(print_str)
            ### self.parent.txbLog.append(print_str)
            ### self.parent.pgbTask.setValue(i)
    
class qtwin_exam(QWidget):  
    def __init__(self) -> None: 
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui', self)
        self.btnStart.clicked.connect(self.btnStartClicked) 

    def btnStartClicked(self):
        th = BackWorker(self)
        th.start() # BackWorker 내의 self.run() 실행
        # connect 부분이 중요!!
        th.initSignal.connect(self.initPgbTask) # 스레드에서 초기화 시그널이 오면 initPgbTask 슬롯함수가 대신 처리
        th.setSignal.connect(self.setPgbTask)
        th.setLog.connect(self.setTxbLog) # TextBrowser 위젯에 진행사항 출력

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료확인', '종료할꺼야?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: 
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore() 

    # 스레드에서 시그널이 넘어오면 UI처리를 대신 해주는 슬롯함수
    @pyqtSlot(int) # BackWorker 스레드에서 self.initSignal.emit() 동작해서 실행
    def initPgbTask(self, maxval):
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0, maxval-1)

    @pyqtSlot(str) # BackWorker 스레드에서 self.setLog.emit() 동작해서 실행
    def setTxbLog(self, msg):
        self.txbLog.append(msg)

    @pyqtSlot(int) # BackWorker 스레드에서 self.setSignal.emit() 동작해서 실행
    def setPgbTask(self, val):
        self.pgbTask.setValue(val)

if __name__ == '__main__':
    loop = QApplication(sys.argv) 
    instance = qtwin_exam()
    instance.show()
    loop.exec_()

    