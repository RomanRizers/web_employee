class Employee:
    def __init__(self, id=0, name="", age=0, experience=""):
        self.id = id
        self.name = name
        self.age = age
        self.experience = experience

    def read(self, io):
        self.name = io.input('name')
        self.age = int(io.input('age'))
        self.experience = io.input('experience')
        print(f"Считано: Имя={self.name}, Возраст={self.age}, Стаж={self.experience}")

    def write(self, io):
        io.output('ID', self.id)
        io.output('Имя', self.name)
        io.output('Возраст', self.age)
        io.output('Стаж работы', self.experience)
