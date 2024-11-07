from ..models.employee import Employee

class Cashier(Employee):
    def __init__(self, id=0, name="", age=0, experience="", shift=""):
        super().__init__(id, name, age, experience) 
        self.shift = shift

    def read(self, io):
        super().read(io) 
        self.shift = io.Input("Смена")

    def write(self, io):
        super().write(io)
        io.Output("Смена", self.shift) 
