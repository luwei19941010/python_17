#-*-coding:utf-8-*-
# Author:Lu Wei

v1=[11,22,33,44,55,66]
# v2=iter(v1)
v2=v1.__iter__()
print(v1.__iter__().__next__())
# print(type(v2))
#
# result1=v2.__next__()
# print(result1)
# result2=v2.__next__()
# print(result2)
# result3=v2.__next__()
# print(result3)
# result4=v2.__next__()
# print(result4)
# result5=v2.__next__()
# print(result5)
#

