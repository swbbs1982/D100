class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name or '无名氏'

    @property
    def age(self):
        return self.__age


if __name__ == '__main__':
    stu = Student('王大锤', 20)
    print(stu.age())
    stu.name = ''
    print(stu._Student__name)
