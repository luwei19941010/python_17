###  day17

#### 1.###今日内容

- 迭代器
- 生成器
- 装饰器
- 项目结构
- logging模块

#### 2.内容回顾&作业

##### 2.1内容回顾

2.1.1函数

- 函数基本结构

  ```
  def func(a1,a2):
  	pass
  ```

  - 参数
  - 返回值
  - 执行函数

- 函数小高级

  - 函数做变量
  - 函数做参数

- 函数中高级

  - 函数做返回值
  - 函数的嵌套

- 装饰器&闭包

- 递归（函数自己调用自己）

- 匿名函数

- 内置函数

  - len id type 
  - print input
  - max sum min divmod abs  bin oct int hex
  - list dict bool str int tuple set()

2.1.2模块

- 定义模块

  - 内置模块  json time datetime os sys random hashlib getpass 

  - 第三方

    - 安装

      - pip install
      - 源码安装
        - 下载源码包：压缩文件
        - 解压文件
        - 打开cmd窗口，进入此目录：cd 源码解压文件的目录
        - 执行：python35 setup.py build 
        - 执行：python35 setup.py install

      安装目录

    - 使用

    - 你了解第三方模块

      - xlrd
      - requests

  - 自定义

    - py文件
    - 文件夹中包含 _ _ init _ _ .py

- 调用模块

  - import
    - import 模块								模块.函数
    - import  模块1.模块2.模块3         模块1.模块2.模块3.函数（）
    - 特殊 import 文件夹                     加载_ _ init _ _ .py
  - from xx import xxx
    - from 模块 import 函数                函数（）
    - from 模块 import 函数as f           f ( )
    - from 模块 import *                       函数1（） 函数2（）
    - from 模块.模块 import 函数         函数（）
      - from 模块 import 模块          模块.函数（）
    - 特殊 from 文件夹 import *           可以直接调用_ _ init _ _ .py函数

2.1.3其他

- 两个值数据交换

  a,b=b,a+b

- 推导式

  - 列表（*）
  - 字典
  - 集合

#### 3.今日内容

类和对象

#### 3.1迭代器

任务：请展示列表中所有的数据。

- while+索引+计数器
- 迭代器，帮助你对某种对象(str/list/tuple/dict/set类创建的对象)【序列】中的元素进行逐一获取，表象：具有__ next __()方法，且每次调用都获取可迭代对象中的元素
  -   列表转换成迭代器：
    - v1=iter([11,22,33,44,55])
    - v1=[11,22,33,44,55].__ iter __()
  - 迭代器想要获取每个值：反复调用 val=v1.__ next__()
  - 直到报错：StopIteration报错
  - 如何判别一个对象是否是迭代器：内部是否有__ next__()方法
- for循环

```
v1=[11,22,33,44]
#1.内部会将v1转换成迭代器
#2.内部反复执行 迭代器.__next__()
#3.取完不报错
for item in v1：
	print(item)
```

####  3.2可迭代对象

1.内部具有__ iter __方法且返回一个迭代器。（*）

```
v1=[11,22,33,44]
result=v1.__iter__()
```

2.可以被for循环的 

#### 3.3 生成器(函数变异)

```
#函数
def func():
	return 123
func()
```

```
#生成器函数（内部是否包含yield）
def func():
	print('f1')
	yield=1
	print('f2')
	yield=2
	print('f3')
	yield=200
	
#函数内部代码不会执行，返回一个 生成器对象。
v1=func（）
for i in v1:
	print(i)
```

```
def func():
	count=1
	while True:
	yield count
	count+=1
	
val=func1()
for i in val:
    print(i)
```

总结：函数中如果存在yield，那么函数就是一个生成器函数，调用生成器函数会返回一个生成器。生成器只有被for循环时，生成器函数内部的函数才会执行，每次循环都会获取yield返回的值。 

 