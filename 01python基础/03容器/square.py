import traceback

# 平方表
square_table = []
for i in range(500):
    square_table.append(i * i)
for i in range(10):
    print(square_table[i])

# 生成器
'''
next()
'''
square_generator = (x * x for x in range(500))
for i in range(10):
    print(next(square_generator))


# 斐波那契数列
def fib(limit):
    n, a, b = 0, 0, 1
    while n < limit:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


f = fib(5)
print(type(f))  # 迭代器 <class 'generator'>
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
try:
    print(next(f))
except StopIteration:
    traceback.print_exc()
for i in fib(5):
    print(i)
