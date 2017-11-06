a = 'abc'
print(dir(a))
for k in dir(a):
    print(k)
    print(getattr(a, k))
