class House:    #создние класса
    def __init__(self, name, number_of_floors): #конструктор класса. тут будут уникальные хар-ки класса
        self.name = name   # это название класса, имя
        self.number_of_floors = number_of_floors  # кол-во этежей

# очень похоже на работу функций. когда мы будем вызывать наш класс, в переменные name и number_of_floors
# запишутся те данные, что мы укажем при вызове.

    def go_to(self, new_floor):   # создаем метод в теле которго пропишем условие задачи.
        for i in range(1, new_floor + 1): #создаем перебор от 1 до new_floor + 1, важно +1 иначе наш последний этаж не войдет
            if new_floor >= 1 and new_floor <= self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует')
                break
# когда мы вызовем метод, то он или выведет этажи в столбик, или если этажность заложенная в вызове
# класса будет больше или меньше чем в вызове метода, то выдаст сообщение

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

# __init__ это наш конструктор, сюда можно вписать еще характеристики.
