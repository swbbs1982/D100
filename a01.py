class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}.')


if __name__ == '__main__':
    stu = Student('王大锤', 20)
    stu.study('Ptyhon程序设计')

