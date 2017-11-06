# 数组的生成方式
li = []

# for循环
for i in range(10):
    if (i % 2) == 0:
        li.append(i)
print(li)

# 语法糖1
li = [1] * 10
print(li)

# 语法糖2
li = [i * 2 for i in range(10)]
print(li)
