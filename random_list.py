import random
def radomlist (a):
    list = []
    for i in range(a):
        list.append(random.randint(0, 100))
    return list

print(radomlist(10))


