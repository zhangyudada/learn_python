# !/usr/bin/env python3
# -*- coding: utf-8 -*-\

# 1
#换行输出
# name = input('输入姓名：')
# print(name+'''line1
# line2
# line3
# 大家好''')

# #2
# #格式化输出
# s1 = 72
# s2 = 85
# print('成绩涨了：%0.1f%%' %((s2-s1)/s1*100))

#3
#格式化输出
# s1 = input('请输入你上次的成绩：')
# s2 = input('请输入你这次的成绩：')
# s1 = int(s1)
# s2 = int(s2)
# r = (s2-s1)/s1*100
# print('你的成绩提高了: %5.1f%%' % r)

#4
#列表
# L = [
#     ['apple','google','micrcosft'],
#     ['java','python','ruby','php'],
#     ['adam','bary','lisa']
# ]

# # 打印Apple:
# print(L[0][0])
# # 打印Python:
# print(L[1][1])
# # 打印Lisa:
# print(L[2][2])

#5
#条件语句
# height = float(input('请输入您的身高(m): '))
# weight = float(input('请输入您的体重（kg）: '))

# bmi = weight/height**2
# print('%6.2f' %(bmi))

# if bmi < 18.5:
#     print('过轻')
# elif bmi < 25:
#     print('正常')
# elif bmi < 28:
#     print('过重')
# elif bmi < 32:
#     print('肥胖')
# else:
#     print('严重肥胖')

#6
#进制转换
# n1 = 255
# n2 = 100
# print(hex(n1))
# print(hex(n2))

#7
# 一元二次方程求解函数
# import math

# def quadratic(a,b,c):
#     if not isinstance(a,(int,float)):
#         raise TypeError('a bad operand type')
#     if not isinstance(b,(int,float)):
#         raise TypeError('a bad operand type')
#     if not isinstance(c,(int,float)):
#         raise TypeError('a bad operand type')
#     if a == 0:
#     	raise TypeError('\'a\' can not be zero')
#     delta = b*b-4*a*c
#     if delta >= 0: 
#         x1 = (-b+math.sqrt(delta))/(2*a)
#         x2 = (-b-math.sqrt(delta))/(2*a)
#         return x1,x2    
#     else:
#         return '该函数没有实数解'

# a=float(input('a = '))
# b=float(input('b = '))
# c=float(input('c = '))
# print(quadratic(a,b,c))

#8
#python3.4 爬虫教程
#一个简单的示例爬虫
#林炳文Evankaka(博客：http://blog.csdn.net/evankaka/)
# import urllib.request
# url = 'http://www.douban.com/'
# webPage = urllib.request.urlopen(url)
# data = webPage.read()
# data = data.decode('UTF-8')
# print('这是data')
# print(data)
# print('这是TYPE')
# print(type(webPage))
# print('这是URL')
# print(webPage.geturl())
# print('这是info')
# print(webPage.info())
# print('这是code')
# print(webPage.getcode())

#9
#python3.4 爬虫教程
#一个简单的示例爬虫
#林炳文Evankaka(博客：http://blog.csdn.net/evankaka/)
# import urllib.request
# weburl = 'http://www.douban.com/'
# webheader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'} 
# req = urllib.request.Request(url=weburl, headers=webheader)  
# webPage=urllib.request.urlopen(req)
# data = webPage.read()
# data = data.decode('UTF-8')
# print(data)
# print(type(webPage))
# print(webPage.geturl())
# print(webPage.info())
# print(webPage.getcode())

#10
#python3.4 爬虫教程
#一个简单的示例爬虫
#林炳文Evankaka(博客：http://blog.csdn.net/evankaka/)
# import urllib.request
# weburl = 'http://www.douban.com/'
# webheader1 = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# webheader2 = {
#     'Connection': 'Keep-Alive',
#     'Accept': 'text/html, application/xhtml+xml, */*',
#     'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
#     #'Accept-Encoding': 'gzip, deflate',
#     'Host': 'www.douban.com',
#     'DNT': '1'
#     }
# req = urllib.request.Request(url=weburl, headers=webheader2)  
# webPage=urllib.request.urlopen(req)
# data = webPage.read()
# data = data.decode('UTF-8')
# print(data)
# print(type(webPage))
# print(webPage.geturl())
# print(webPage.info())
# print(webPage.getcode())

#11
# 汉诺塔思想笔记
# 认识汉诺塔的目标：把A柱子上的N个盘子移动到C柱子
# 递归的思想就是把这个目标分解成三个子目标
# 子目标1：将前n-1个盘子从a移动到b上
# 子目标2：将最底下的最后一个盘子从a移动到c上
# 子目标3：将b上的n-1个盘子移动到c上
# 然后每个子目标又是一次独立的汉诺塔游戏，也就可以继续分解目标直到N为1
# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         move(n-1, a, c, b)# 子目标1
#         move(1, a, b, c)# 子目标2
#         move(n-1, b, a, c)# 子目标3
# n = input('enter the number:')
# move(int(n), 'A', 'B', 'C')

#12
#迭代dict（字典）
# d={'a':1,'b':2,'c':3}
# for key,value in d.items():
# 	print(key,value)

#13
#列表生成器
#列出当前目录下的所有文件和目录名
# import os # 导入os模块，模块的概念后面讲到
# L1 = [d for d in os.listdir('.')]# os.listdir可以列出文件和目录
# print(L1)

#14
#列表生成器
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [x.lower() for x in L1 if isinstance(x, str)]
# print(L2)

#15
#生成器：generator
#斐波那契数列
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
    
# g = fib(10)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

#16
#生成器：generator
#杨辉三角
# def triangles():
#     L = [1]
#     yield L
#     while True:
#         L.append(1)
#         yield L
#         L = [L[i-1]+L[i] for i in range(1,len(L))]
#         L.insert(0,1)

# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break

#17
# #filter生成素数
# #先构造一个从3开始的奇数序列，这是一个生成器，并且是一个无限序列
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n

# #定义一个筛选函数
# def _not_divisible(n):
#     return lambda x: x % n > 0

# #定义一个生成器，不断返回下一个素数
# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列


# #由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件
# # 打印1000以内的素数:
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

#18
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909，利用filter()滤掉非回数
# def is_palindrome(n):
# 	return str(n) == str(n)[::-1]

# output = filter(is_palindrome, range(1, 1000))
# print(list(output))

#19
#sorted()函数
#用一组tuple表示学生名字和成绩
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

#按名字排序
def by_name(t):
    return t[0].lower()
L2 = sorted(L, key = by_name)
print(L2)

#按成绩从高到低排序
def by_score(t):
    return t[1]
L3 = sorted(L, key = by_score, reverse = True)
print(L3)

#20
