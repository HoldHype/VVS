import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Приложение для анализа текста")

central_widget = QWidget()
window.setCentralWidget(central_widget)

layout = QVBoxLayout()
central_widget.setLayout(layout)

text_input = QTextEdit()
text_input.setPlaceholderText("Введите текст")
layout.addWidget(text_input)

process_button = QPushButton("Анализ текста")
layout.addWidget(process_button)

result_output = QTextEdit()
result_output.setReadOnly(True)
result_output.setPlaceholderText("Результат")
layout.addWidget(result_output)

def on_button_click():
    input_text = text_input.toPlainText()
    
    char_count = len(input_text)
    char_no_spaces = len(input_text.replace(" ", "").replace("\n", ""))
    word_count = len(input_text.split())
    line_count = len(input_text.splitlines())
    
    letter_count = sum(c.isalpha() for c in input_text)
    digit_count = sum(c.isdigit() for c in input_text)
    space_count = input_text.count(' ')
    
    words = input_text.split()
    longest_word = max(words, key=len, default="")
    
    
    t1 = f'Общее количество символов: {char_count}\n'
    t2 = f'Количество символов без пробелов{char_no_spaces}\n'
    t3 = f'Количество слов: {word_count}\n'
    t4 = f'Количество строк: {line_count}\n'
    t5 = f'Количество букв: {letter_count}\n'
    t6 = f'Количество цифр: {digit_count}\n'
    t7 = f'Количество пробелов: {space_count}\n'
    t8 = f'Самое длинное слово: {longest_word}\n'

    result_text = t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8
    result_output.setPlainText(result_text)

process_button.clicked.connect(on_button_click)

# Устанавливаем размер окна
window.resize(600, 400)
window.show()

sys.exit(app.exec())