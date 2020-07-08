from itertools import cycle, count, islice

for i in count(3):
    if i > 10:
        break
    print(i)

i = 0
for el in cycle("python"):
    if i > 11:
        break
    i += 1
    print(el)
