# 装饰器

def hello(fun):
    def wrapper():
        print("hello, %s" % fun.__name__)
        fun()
        print("bye, %s" % fun.__name__)

    return wrapper


@hello
def greet():
    print("nice to meet you~")


greet()
