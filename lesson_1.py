# ООП
# Классы

def sum1(a,b):
    return a+b

# print(sum1(1,8))
class Human:
    # атребуты уровня класса
    # свойства класса
    head = True
    # магический метод
    # конструктор класса
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # метод
    def tprint(self):
        print(self.name, self.head, self.age)

    def summ(self):
        print(self.name, self.age+15)

    def __str__(self):
        return f'{self.name},{self.age}'

    def __len__(self):
        return len(self.name)

# экземпляр класса, обекты класса
human = Human('beka',20)
human2 = Human('Erbol',180)
human3 = Human('Malik', 16)

human.tprint()
human.summ()
