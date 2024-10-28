class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # Добавляем название дома в историю
        cls.houses_history.append(args[0])
        # Создаем экземпляр объекта
        return super().__new__(cls)

    def __init__(self, first, second=25, third=3.14):
        self.first = first
        self.second = second
        self.third = third

    def __del__(self):
        print(f"{self.first} снесён, но он останется в истории")


# Пример использования класса
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']
h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2  # ЖК Акация снесён, но он останется в истории
del h3  # ЖК Матрёшки снесён, но он останется в истории

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
del h1  # ЖК Эльбрус снесён, но он останется в истории
