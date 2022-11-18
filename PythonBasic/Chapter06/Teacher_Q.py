# 1. 사칙연산이 가능한FourCal 클래스를 구현하시오
class FourCal :
    first = second = 0
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        add = self.first + self.second
        return print(add)
    def mul(self):
        mul = self.first * self.second
        return mul
    def sub(self):
        sub = self.first - self.second
        return sub
    def div(self):
        div = self.first / self.second
        return div

b = FourCal(3, 8)
b.add()
b.mul()
b.sub()
b.div()
b.setdata(4,2)
b.add()

