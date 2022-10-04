import json
class Question():

    def __init__(self, text_question, complexity, rigth_answer, get_question=False, person_answer=None):
        self.text_question = text_question
        self.complexity = complexity
        self.rigth_answer = rigth_answer
        self.get_question = get_question
        self.person_answer = person_answer
        self.points = self.complexity * 10

    def get_points(self):
    """Возвращает int, количество баллов.
    Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
    """
    def is_correct():
    """Возвращает True, если ответ пользователя совпадает
    с верным ответов иначе False.
    """
    def build_question():
    """Возвращает вопрос в понятном пользователю виде, например:
    Вопрос: What do people often call American flag?
    Сложность 4/5
    """

    def build_positive_feedback():
    """Возвращает :
    Ответ верный, получено __ баллов
    """
    def build_negative_feedback():
    """Возвращает :
    Ответ неверный, верный ответ __
    """



