from random import choice, shuffle
from PyQt6.QtWidgets import QApplication



app = QApplication([])

from main_window import *
from menu_window import*
class Question():
    def __init__(self, question_text, answer_text, wrong:tuple):
        self.question_text = question_text
        self.answer_text = answer_text
        self.wrong_answers = wrong

    def got_right(self):
        ...
    def got_right(self):
        ...

q1 = Question("чим розпочався твір кайдашева сім'я","описом села семи гори",("описом кайдашевої сімїб","привітанням","предісторією"))
q2 = Question("Чим розпочинається твір 'хіба ревуть воли як ясла повні'?","Зустріч з польовою царівною",("зустріч з псом","зустріч з котом","зустріч з королевою"))
q3 = Question("Мідна руда містить 7% міді. скільки руди треба взяти щоб отримати 35 т міді?","500 тонн",("100тон","500грам","500кг"))
q4 = Question("За перший тиждень турист пройшов 32 км, що становить 40% туристського маршруту. Скільки кілометрів становить довжина маршруту?","80 км",("70 км","90 км","60 км"))

question_list = [ q1,q2,q3,q4 ]
radio_button_list = [rd_answer_1,rd_answer_2,rd_answer_3,rd_answer_4,]

def new_question():
    global random_question
    random_question = choice(question_list)

    shuffle(radio_button_list)

    question_ld.setText(random_question.question_text)

    radio_button_list[0].setText(random_question.answer_text)
    radio_button_list[1].setText(random_question.wrong_answers[0])
    radio_button_list[2].setText(random_question.wrong_answers[1])
    radio_button_list[3].setText(random_question.wrong_answers[2])

new_question()

def check_result():
    correct_answer_ld.setText(random_question.answer_text)
    radio_button_group.setExclusive(False)
    for btn in radio_button_list:
        if btn.isChecked():
            btn.setChecked(False)
            if btn.text() == random_question.answer_text:
             result_ld.setText("правельно")
             break
        
    else:
        result_ld.setText("не правельно")
    radio_button_group.setExclusive(True)



def change_box():
    if btn_next.text() == "Відповісти":
        radio_button_box.hide()
        answer_box.show()
        btn_next.setText("наступне питання")
        check_result()
    elif btn_next.text() == "наступне питання":
        radio_button_box.show()
        answer_box.hide()
        btn_next.setText("Відповісти")
        new_question()


btn_next.clicked.connect(change_box)

def open_menu():
    window.hide()
    menu_window.show()

def close_menu():
    ...

menu_btn.clicked.connect(open_menu)








window.show()
app.exec()

