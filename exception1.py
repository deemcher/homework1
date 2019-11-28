"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
dialog = {"Как жизнь?": "Отлично!",
         "Кем работаешь?": "Программистом",
          "На каком языке?": "Python",
           "До свидания": "Прощайте" }

def ask_user_dict():
    """
    Замените pass на ваш код
    """
    while True:
        try:
            user_question = input('Введите ваш вопрос: ')
            print(dialog.get(user_question))
        except KeyboardInterrupt:
            print('Пока!')
            break
    
if __name__ == "__main__":
    ask_user_dict()
