from .storage.pickle_storage import PickleStorage
def menu_exit():
    pass

def main():
    storage = PickleStorage()
    
    menu = [
        ["Добавить сотрудника", storage.add],
        ["Удалить сотрудника", storage.delete_item],
        ["Обновить данные сотрудника", storage.edit],
        ["Показать всех сотрудников", storage.get_items],
        ["Сохранить в файл", storage.save],
        ["Загрузить из файла", storage.load],
        ["Выход",],
    ]

    while True:
        print("\n" + "-" * 40)
        print("Меню:")
        for i, menuItem in enumerate(menu, 1):
            print(f"{i}. {menuItem[0]}")
        print("-" * 40) 

        try:
            print("\n")
            m = int(input("Выберите действие: "))
            if menu[m-1][0] == "Выход":
                return
        except ValueError:
            print("Некорректный ввод, попробуйте снова.")
            continue

        if 1 <= m <= len(menu):
            menu[m-1][1]()
        else:
            print("Некорректный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
