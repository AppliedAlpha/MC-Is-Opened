import sys
# from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QDesktopWidget, QGridLayout, QLabel, QLineEdit
# from PyQt5.QtGui import QIcon
from PyQt5.Qt import *


class MCIsOpenedApp(QWidget):
    def __init__(self):
        super().__init__()

        # 변수 선언 및 초기화
        self.title_label = QLabel('마크 서버 열려 있나요?')
        self.address_label = QLabel('주소/ADDRESS')
        self.port_label = QLabel('포트/PORT')
        self.state_label = QLabel('서버 상태:')
        self.opened_label = QLabel('-')
        self.count_label = QLabel('(-/-)')

        self.address_text = QLineEdit()
        self.port_text = QLineEdit()
        self.motd_text = QLineEdit()  # readOnly

        self.reset_button = QPushButton('초기화')
        self.run_button = QPushButton('실행하기')

        # 호출해서 초기화
        self.initCenter()
        # self.initItems()
        self.initLayout()
        self.initUI()

    def initCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initLayout(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # (세로 idx, 가로 idx, 세로 span, 가로 span)
        grid.addWidget(self.title_label, 0, 0, 1, -1, alignment=Qt.AlignCenter)
        grid.addWidget(self.address_label, 1, 0, 1, 2, alignment=Qt.AlignCenter)
        grid.addWidget(self.port_label, 1, 2, alignment=Qt.AlignCenter)
        grid.addWidget(self.state_label, 3, 1, alignment=Qt.AlignCenter)
        grid.addWidget(self.opened_label, 3, 2)
        grid.addWidget(self.count_label, 3, 3, alignment=Qt.AlignCenter)

        grid.addWidget(self.address_text, 2, 0, 1, 2)
        grid.addWidget(self.port_text, 2, 2)
        grid.addWidget(self.motd_text, 4, 1, 1, -1)

        grid.addWidget(self.reset_button, 1, 3)
        grid.addWidget(self.run_button, 2, 3)

    def initUI(self):
        self.setWindowTitle('MC IS OPENED?')
        self.setWindowIcon(QIcon('Sprites/icon.png'))
        self.resize(720, 360)
        self.show()


# 프로그램 실행
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MCIsOpenedApp()
    print("프로그램이 실행되었습니다.")

    sys.exit(app.exec_())
