import time
x = 0
while True:
    print(x)
    x += 1
    if x > 3:
        x = 0
    time.sleep(1)

