# инкапцуляция , Абстракция , git clone
# Уровень зашиты
# Публичная зашита = 0, _зашишеная:protectod,

class Bank:
    def __init__(self,fullname,maney,key):
        self.fullname=fullname
        self.maney=maney
        self._password=key
    def mon(self):
        self.maney += 100

beka=Bank('bekbolot', 0, '1457')
beka.mon()
print(beka.maney)
beka.password="1111"
print(beka.password)
