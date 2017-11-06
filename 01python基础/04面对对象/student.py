class Student(object):
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('not int')

        elif (value < 0) or (value > 100):
            raise ValueError('not in 0 ~ 100')

        self._score = value

    # 自定义类的魔术方法
    def __str__(self):
        return print('class Student __str__ ', self._score)


print(Student(12))
