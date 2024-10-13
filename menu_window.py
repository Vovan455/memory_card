from PyQt6.QtWidgets import (QWidget,QLabel,QRadioButton,QPushButton,QGroupBox,QButtonGroup,QVBoxLayout,QHBoxLayout, QLineEdit)

menu_window = QWidget()


menu_v_line = QVBoxLayout()

menu_h_line_1 = QHBoxLayout()
menu_h_line_2 = QHBoxLayout()
menu_h_line_3 = QHBoxLayout()
menu_h_line_4 = QHBoxLayout()
menu_h_line_5 = QHBoxLayout()
menu_h_line_6 = QHBoxLayout()

menu_question_text_ld = QLabel("ВВудіть текст питання" )
menu_question_text_input = QLineEdit()
menu_h_line_1.addWidget(menu_question_text_ld)
menu_h_line_1.addWidget(menu_question_text_input)
menu_v_line.addLayout(menu_h_line_1)

menu_question_text_ld = QLabel("ВВудіть правельнк відповідь" )
menu_question_text_input = QLineEdit()
menu_h_line_2.addWidget(menu_question_text_ld)
menu_h_line_2.addWidget(menu_question_text_input)
menu_v_line.addLayout(menu_h_line_2)

menu_question_text_ld = QLabel("ВВудіть правельнк відповідь" )
menu_question_text_input = QLineEdit()
menu_h_line_3.addWidget(menu_question_text_ld)
menu_h_line_3.addWidget(menu_question_text_input)
menu_v_line.addLayout(menu_h_line_3)

menu_question_text_ld = QLabel("ВВудіть правельнк відповідь" )
menu_question_text_input = QLineEdit()
menu_h_line_4.addWidget(menu_question_text_ld)
menu_h_line_4.addWidget(menu_question_text_input)
menu_v_line.addLayout(menu_h_line_4)

menu_question_text_ld = QLabel("ВВудіть правельнк відповідь" )
menu_question_text_input = QLineEdit()
menu_h_line_5.addWidget(menu_question_text_ld)
menu_h_line_5.addWidget(menu_question_text_input)
menu_v_line.addLayout(menu_h_line_5)

menu_question_text_ld = QLabel("ВВудіть правельнк відповідь" )
menu_question_text_input = QLineEdit()
menu_h_line_6.addWidget(menu_question_text_ld)
menu_h_line_6.addWidget(menu_question_text_input)
menu_v_line.addLayout(menu_h_line_6)





menu_window.setLayout(menu_v_line)