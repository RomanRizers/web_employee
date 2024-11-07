from .employee import Employee

class Picker(Employee):
    def __init__(self, id=0, name="", age=0, experience="", zone=""):
        super().__init__(id, name, age, experience)
        self.zone = zone

    def read(self, io):
        super().read(io)
        self.zone = io.input("Зона сборки")

    def write(self, io):
        super().write(io)
        io.output("Зона сборки", self.zone)
