class Master(object):
    def __init__(self):
        self.kongfu = ['煎饼果子酱料']

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

#学校类
class School(object):
    def __init__(self):
        self.kongfu = ['学员班煎饼果子酱料']
    
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

#徒弟类
class Prentice(School,Master):
    pass

daqiu = Prentice()
daqiu.make_cake()