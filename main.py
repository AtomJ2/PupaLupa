def read_matrices(filename1, filename2):
    fin1 = open(filename1)
    fin2 = open(filename2)
    string0 = fin1.readline()
    string0 = string0.replace('\n', '')
    lst1 = string0.split(' ')
    m = len(lst1)
    n = 1
    string0 = fin1.readline()
    while not string0.startswith('\n'):
        string0 = string0.replace('\n', '')
        n += 1
        lst1.extend(string0.split(' '))
        string0 = fin1.readline()
    string0 = fin1.readline()
    string0 = string0.replace('\n', '')
    lst2 = string0.split(' ')
    string0 = fin1.readline()
    while not string0.startswith('\n'):
        string0 = string0.replace('\n', '')
        lst2.extend(string0.split(' '))
        string0 = fin1.readline()
    return lst1, lst2, n, m


def create_matrix(n, m):
    """Creating matrix"""
    return [[0 for _ in range(m)] for _ in range(n)]


class Pupa:
    def __init__(self, balance = 0):
        self._balance = balance
    def take_salary(self, value):
        self._balance += value


class Lupa:
    def __init__(self, balance = 0):
        self._balance = balance
    def take_salary(self, value):
        self._balance += value
    def do_work(self, filename1, filename2):
        lst1, lst2, n, m = read_matrices(filename1, filename2)
        nm = n * m
        res = create_matrix(n, m)
        for i in range(nm):
            res.extend(int(lst1[i]) + int(lst2[i]))

# class Accountant:
    # def give_salary(self, worker):



class Item:
    def __init__(self, count=3, max_count=16):
        self._count = count
        self._max_count = 16

    def update_count(self, val):
        if val <= self._max_count:
            self._count = val
            return True
        else:
            return False

    # Свойство объекта. Не принимает параметров кроме self, вызывается без круглых скобок
    # Определяется с помощью декоратора property
    @property
    def count(self):
        return self._count

    # Ещё один способ изменить атрибут класса
    @count.setter
    def count(self, val):
        self._count = val
        if val <= self._max_count:
            self._count = val
        else:
            pass

    @staticmethod
    def static():
        print('I am function')

    @classmethod
    def my_name(cls):
        return cls.__name__


class Banana(Item):
    def __init__(self, count=1, max_count=14, color='green'):
        super().__init__(count, max_count)
        self._color = color

    @property
    def color(self):
        return self._color


banana = Banana(color='red')
print(banana.count)
print(banana.color)
banana.update_count(15)
print(banana.count)
