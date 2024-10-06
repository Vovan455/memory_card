from PyQt6.QtWidgets import (QWidget,QLabel,QRadioButton,QPushButton,QGroupBox,QButtonGroup,QVBoxLayout,QHBoxLayout)


card_width, card_height = 600, 500

window = QWidget()
window.resize(card_width, card_height)
window.setWindowTitle("Memori Card. Автор: Бреславський Володимир")


question_ld = QLabel()

rd_answer_1 = QRadioButton()
rd_answer_2 = QRadioButton()
rd_answer_3 = QRadioButton()
rd_answer_4 = QRadioButton()

btn_next = QPushButton("Відповісти")

radio_button_box = QGroupBox("варіанти відповідей")
radio_button_group = QButtonGroup()

radio_button_group.addButton(rd_answer_1)
radio_button_group.addButton(rd_answer_2)
radio_button_group.addButton(rd_answer_3)
radio_button_group.addButton(rd_answer_4)

answer_box = QGroupBox("Результат")
result_ld = QLabel("правельно/неправельно")
correct_answer_ld = QLabel("правильна відповіть")

main_v_line = QVBoxLayout()


radio_button_box_v_line = QVBoxLayout()
radio_button_box_h_line_1 = QHBoxLayout()
radio_button_box_h_line_2 = QHBoxLayout()

radio_button_box_h_line_1.addWidget(rd_answer_1)
radio_button_box_h_line_1.addWidget(rd_answer_2)

radio_button_box_h_line_2.addWidget(rd_answer_3)
radio_button_box_h_line_2.addWidget(rd_answer_4)

radio_button_box_v_line.addLayout(radio_button_box_h_line_1)
radio_button_box_v_line.addLayout(radio_button_box_h_line_2)

radio_button_box.setLayout(radio_button_box_v_line)

main_v_line.addWidget(question_ld)
main_v_line.addWidget(radio_button_box)








answer_box_v_line = QVBoxLayout()
answer_box_v_line.addWidget(result_ld)
answer_box_v_line.addWidget(correct_answer_ld)

answer_box.setLayout(answer_box_v_line)

main_v_line.addWidget(answer_box)

main_v_line.addWidget(btn_next)







answer_box.hide()
window.setLayout(main_v_line)
