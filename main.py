import random


def read_matrices(filename1, filename2):
    """Reading Matrices"""
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
    string0 = fin2.readline()
    string0 = string0.replace('\n', '')
    lst2 = string0.split(' ')
    string0 = fin2.readline()
    while not string0.startswith('\n'):
        string0 = string0.replace('\n', '')
        lst2.extend(string0.split(' '))
        string0 = fin2.readline()
    return lst1, lst2, n, m


class Pupa:
    def __init__(self, balance=0):
        self._balance = balance

    def take_salary(self, value):
        self._balance += value

    @staticmethod
    def do_work(filename1, filename2):
        lst1, lst2, n, m = read_matrices(filename1, filename2)
        nm = n * m
        res = []
        for i in range(nm):
            res.append(str(int(lst1[i]) + int(lst2[i])))
        return res


class Lupa:
    def __init__(self, balance=0):
        self._balance = balance

    def take_salary(self, value):
        self._balance += value

    @staticmethod
    def do_work(filename1, filename2):
        lst1, lst2, n, m = read_matrices(filename1, filename2)
        nm = n * m
        res = []
        for i in range(nm):
            res.append(str(int(lst1[i]) - int(lst2[i])))
        return res


class Accountant:
    @staticmethod
    def give_salary(worker):
        if type(worker).__name__ == 'Lupa':
            val = random.randint(1, 101)
            worker.take_salary(val)


lupa = Lupa()
print(lupa.do_work('1.txt', '2.txt'))
