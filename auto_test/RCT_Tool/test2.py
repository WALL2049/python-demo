class Student:
    level = 1
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'{self.name},{self.age}'

    @classmethod
    def set_level(cls, level):
        cls.level = level


s1 = Student('xiaoming', 7)
s2 = Student('xiaoli', 8)
print(s1.get_info())
print(s2.get_info())
print(Student.level)
