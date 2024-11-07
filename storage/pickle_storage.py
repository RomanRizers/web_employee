import os
import pickle
from ..models.employee import Employee

class PickleStorage:
    def __init__(self):
        self.filename = os.path.join('storage', 'storage.pkl')
        self.max_id = 0
        self.items = {}
    
    def save(self):
        with open(self.filename, 'wb') as file:
            pickle.dump((self.max_id, self.items), file)
        print("Данные сохранены в файл")

    def load(self):
        if not os.path.exists(self.filename):
            print("Ошибка: Файл не найден")
            return
        with open(self.filename, 'rb') as file:
            (self.max_id, self.items) = pickle.load(file)
        print("Данные успешно загружены")

    def add(self, item):
        try:
            item.id = int(item.id)
        except ValueError:
            item.id = 0 
            
        if item.id <= 0:
            self.max_id += 1
            item.id = self.max_id
    
        self.items[item.id] = item

    def delete(self):
        self.items = {}
        self.max_id = 0
        print("Все сотрудники успешно удалены.")

    def delete_item(self, id):
        if id in self.items:
            del self.items[id]
            print(f"Сотрудник с ID {id} успешно удалён.")

    def get_item(self, id) -> object:
        return self.items.get(id, Employee())

    def get_items(self):
        for _, item in self.items.items():
            yield item

    def edit(self, id, item):
        if id in self.items:
            self.items[id] = item
            print(f"Сотрудник с ID {id} успешно обновлён.")


