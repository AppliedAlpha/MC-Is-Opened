# How to import
# import [Name]  // Local
# from . import [Name]  // Production
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MCIsOpenedApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMenu()
        self.initUI()

    def initMenu(self):
        run_action = QAction('실행', self)
        run_action.setShortcut('Alt+R')
        run_action.triggered.connect(self.run)

        exit_action = QAction('종료', self)
        exit_action.setShortcut('Alt+Q')
        exit_action.triggered.connect(qApp.exit)

        menu = self.menuBar()
        menu.setNativeMenuBar(False)

        action_menu = menu.addMenu('&Action')
        action_menu.addAction(run_action)
        action_menu.addAction(exit_action)

    def initUI(self):
        self.setWindowTitle('MC IS OPENED?')
        self.setWindowIcon(QIcon('Sprites/icon.png'))
        self.resize(720, 360)
        self.show()

    def run(self):
        print('executed object:', self)


# 프로그램 실행
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MCIsOpenedApp()
    print("프로그램이 실행되었습니다.")

    sys.exit(app.exec_())
