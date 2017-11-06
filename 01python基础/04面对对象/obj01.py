class Foo(object):
    name = 'mary'
    # 变量名加下划线，外界不可访问
    __pwd = 'password'

    # 只对当前类起作用，继承的类不起作用
    __slots__ = ['school','set_school']

    # 构造函数，当对象被创建时，初始化一些事
    def __init__(self):
        self.age = 10

    def bar(self):
        pass

    def hello(self, name):
        print('class self name: %s' % self.name)
        print('i am %s' % name)

    def get_pwd(self):
        return self.__pwd

    def set_pwd(self, pwd):
        self.__pwd = pwd


foo1 = Foo()
foo1.hello('jack')
print(foo1.get_pwd())
