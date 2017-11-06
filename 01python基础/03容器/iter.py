from collections import Iterable, Iterator

print(isinstance([1, 2, 3], Iterable))

print(isinstance([1, 2, 3], Iterator))

'''
生成器用于惰性计算
'''
