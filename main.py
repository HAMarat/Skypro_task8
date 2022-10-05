import json

#
# class Question:
#
#     def __init__(self, question, complexity, right_answer, get_question=False, person_answer=None):
#         self.question = question
#         self.complexity = complexity
#         self.right_answer = right_answer
#         self.get_question = get_question
#         self.person_answer = person_answer
#         self.points = None
#
#     def get_points(self):
#         """Возвращает int, количество баллов.
#         Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
#         """
#         self.points = self.complexity * 10
#         return self.points
#
#     def is_correct(self):
#         """Возвращает True, если ответ пользователя совпадает
#         с верным ответов иначе False.
#         """
#         return self.right_answer == self.person_answer
#
#     def build_question(self):
#         """Возвращает вопрос в понятном пользователю виде, например:
#         Вопрос: What do people often call American flag?
#         Сложность 4/5
#         """
#
#     def build_positive_feedback(self):
#         """Возвращает :
#         Ответ верный, получено __ баллов
#         """
#
#     def build_negative_feedback(self):
#         """Возвращает :
#         Ответ неверный, верный ответ __
#         """


with open('question.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

for question_dict in json_data:

