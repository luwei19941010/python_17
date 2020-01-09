#-*-coding:utf-8-*-
# Author:Lu Wei
def func1(num):
    count=1
    while True:
        yield count
        count+=1
        if count==num:
            return

val=func1(1000)
for i in val:
    print(i)


# def func():
#     yield 2
#
#     return 111
#
#     yield 10
#
# v=func()
# print(v)
# for i in v:
#     print(i)