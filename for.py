"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
student_grades = [{'school_class': '4a', 'scores': [3,5,4,3,2]},
                    {'school_class': '5b', 'scores': [2,4,2,5,3]},
                    {'school_class': '6a', 'scores': [3,4,5,3,4]},
                    {'school_class': '8b', 'scores': [5,4,4,5,2]},]
                
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    scores_sum = 0
    for score in student_grades[0]['scores']:
        scores_sum += score
        print(scores_sum)
    scores_average = scores_sum / len(student_grades[0]['scores'])
    print(f"Средняя оценка {scores_average}")


    
if __name__ == "__main__":
    main()
