from .employee import Employee

class Manager(Employee):
    def __init__(self, id=0, name="", age=0, experience="", department=""):
        super().__init__(id, name, age, experience)
        self.department = department 

    def read(self, io):
        super().read(io) 
        self.department = io.input("Отдел")

    def write(self, io):
        super().write(io)
        io.output("Отдел", self.department)
