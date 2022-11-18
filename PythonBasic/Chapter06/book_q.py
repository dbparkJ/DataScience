# Q1.
class Rectangle :
    width = height = 0

    def __init__(self, w, h):
        self.width = w
        self.height = h
    def area_calc(self):
        area = self.width * self.height
        return area
    def circum_calc(self):
        circum = (self.width + self.height) * 2
        return circum

print("사각형의 넓이와 둘레를 계산합니다.")

w = int(input('사각형의 가로 입력 : '))
h = int(input('사각형의 세로 입력 : '))

print('-'*25)
rec = Rectangle(w, h)
area = rec.area_calc()
print(f'사각형의 넓이 : {area}')

circum = rec.circum_calc()
print(f'사각형의 둘레 : {circum}')
print('-'*25)


# Q2.
class Scattering :
    x = [5, 9, 1, 7, 4, 6]
    #def __init__(self):
