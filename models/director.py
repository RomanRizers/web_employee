from ..models.employee import Employee

class Director(Employee):
    def __init__(self, id=0, name="", age=0, experience=""):
        super().__init__(id, name, age, experience)

    def read(self, io):
        super().read(io)

    def write(self, io):
        super().write(io)
