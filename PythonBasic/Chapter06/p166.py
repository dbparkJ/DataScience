class Parent :
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def display(self):
        print('name : {}, job : {}'.format(self.name, self.job))

p = Parent('홍길동','회사원')
p.display()

class Children(Parent):
    gender = None

    def __init__(self, name, job, gender):
        super().__init__(name, job)
        self.gender = gender

    def display2(self):
        print('name : {}\tjob : {}\tgender : {}'.format(self.name, self.job, self.gender))

chil = Children('이순신', '수군', '남자')
chil.display2()
