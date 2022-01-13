class Person:
    def __init__(self, name):
        self.name1 = name
        self.name2 = '小白'

    # 利用property装饰器将获取name方法转换为获取对象的属性
    @property
    def name(self):
        return self.name1 + '!'

    # 利用property装饰器将设置name方法转换为获取对象的属性
    @name.setter  # @属性名.setter
    def name3(self, n):
        self.name1 = '小绿' if n == '小灰' else '小宝'

p = Person('小黑')
print(p.name, p.name1, p.name2, p.name3)
p.name3 = '小灰'
print(p.name, p.name1, p.name2, p.name3)
p.name3 = '小2'
print(p.name, p.name1, p.name2, p.name3)
p.name = '123'
