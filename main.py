# Вызываем модули json для работы с данными в формате json и random для случайного перемешивания списка
import json
import random


def get_statistic(question_list):
    """
    Выводит статистику на основание полученных ответов
    """
    # Задаем счетчики общего количества очков и правильных ответов
    total_points = 0
    right_answers = 0

    total_questions = len(question_list)

    # Получаем статистику из экземпляров класса Question
    for elements in question_list:
        if elements.is_correct():
            total_points += elements.get_points()
            right_answers += 1

    statistic = (f'Вот и всё!\n'
                 f'Отвечено {right_answers} вопроса из {total_questions}\n'
                 f'Набрано баллов: {total_points}')
    return statistic


def get_json_data(filename):
    """
    Получает данные вопросов из файла
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


# Создаем класс Question для работы с вопросами
class Question:
    "Класс Question"
    def __init__(self, question, complexity, right_answer):
        self.question = question
        self.complexity = int(complexity)
        self.right_answer = right_answer
        self.get_question = False
        self.person_answer = None
        self.points = self.complexity * 10

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        self.points = self.complexity * 10
        return self.points

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответом иначе False.
        """
        return self.right_answer == self.person_answer

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        text_answer = (f'{self.question}\n'
                       f'Сложность: {str(self.complexity)}/5')

        return text_answer

    def build_positive_feedback(self):
        """Возвращает:
        Ответ верный, получено __ баллов
        """
        positive_feedback = f'Ответ верный, получено {self.points} баллов'
        return positive_feedback

    def build_negative_feedback(self):
        """Возвращает:
        Ответ неверный, верный ответ __
        """
        negative_feedback = f'Ответ неверный, верный ответ {self.right_answer}'
        return negative_feedback


# Получаем данные о вопросах из файла question.json
json_data = get_json_data('question.json')

# Создаем пустой словарь для хранения экземпляров класса Question
questions_list = []

# Создаем экземпляры класса Question и записываем в словарь
for question_dict in json_data:
    questions_list.append(Question(question_dict['q'], question_dict['d'], question_dict['a']))

# Перемешиваем экземпляры класса Question в случайном порядку
random.shuffle(questions_list)

# Задаем вопросы, записываем результаты и выводим результат ответа
for question_object in questions_list:
    print(question_object.build_question())
    question_object.get_question = True
    question_object.person_answer = input()
    if question_object.is_correct():
        print(question_object.build_positive_feedback())
    else:
        print(question_object.build_negative_feedback())
    print()

# Выводим финальную статистику
print(get_statistic(questions_list))
