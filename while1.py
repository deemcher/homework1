"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    """
    Замените pass на ваш код
    """
    while True:
        user_answer = input('Как дела? ')
        if user_answer == 'Хорошо':
            print('Верно')
            break
        
if __name__ == "__main__":
    ask_user()
