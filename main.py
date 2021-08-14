import sys

from PySide6.QtWidgets import QVBoxLayout, \
                              QPushButton, \
                              QLabel, \
                              QWidget, \
                              QApplication


def button_click():
    label.setText('アイスといったらパリパリバー')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()

    label = QLabel('ここにボタンを押した結果が表示されます。')
    button = QPushButton('実行')
    button.clicked.connect(button_click)

    vlayout = QVBoxLayout(window)
    vlayout.addWidget(label)
    vlayout.addWidget(button)

    window.show()

    sys.exit(app.exec_())
