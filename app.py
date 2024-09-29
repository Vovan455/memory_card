from PyQt6.QtWidgets import QApplication



app = QApplication([])

from main_window import *


def change_box():
    if btn_next.text() == "Відповіть":
        radio_button_box.hide()
        answer_box.show()
        btn_next.setText("натупне питання")
    elif btn_next.text() == "наступне питання":
        radio_button_box.show()
        answer_box.hide()
        btn_next.setText("Вшдповісти")


btn_next.clicked.connect(change_box)










window.show()
app.exec()

