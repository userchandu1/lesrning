def mygen(num):
    print('Generating first n number')
    n = 1
    while n <= num:
        yield n
        n = n + 1


print(type(mygen))
m = mygen(10)
print(type(m))
for i in range(10):
    print(next(m))
