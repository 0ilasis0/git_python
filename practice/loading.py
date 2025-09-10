import time

delay = 0.1

print("{:-^14}".format('執行開始'),end = '\r')

start = time.perf_counter()
for i in range(10):
    for j in range(10):
        end = time.perf_counter()
        difftime = end - start
        a = '-' * i
        b = '*' * (10-i-1)
        print('{}{}%[{}>{}]   使用{:.2f}s'.format(i, j, a, b, difftime),end = '\r')
        time.sleep(delay)

print("{:-^14}".format("執行結束"))