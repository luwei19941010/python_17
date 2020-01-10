#-*-coding:utf-8-*-
# Author:Lu Wei
import time
def func():
    cursor=0
    while True:
        f=open('生成器',mode='r',encoding='utf-8')
        l = []
        f.seek(cursor)
        for i in range(10):
            date=f.readline()
            if not date:
                return
            l.append(date.strip())
        cursor = f.tell()
        # print(cursor)
        # time.sleep(1)
        f.close()
        for i in l:
            yield i

val=func()
for i in val:
    print(i)
    