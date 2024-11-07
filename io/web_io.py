from flask import request

class WebIO:
    def input(self, prompt):  # Исправлено с заглавной буквы
        return request.form.get(prompt)

    def output(self, title, value):
        print(f"{title}: {value}")  # Вывод через print для отладки или сохранение в шаблон
