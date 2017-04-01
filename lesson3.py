# !/usr/bin/env python3
# -*- coding: utf-8 -*-\

# #1
# what_he_does = ' plays '
# his_instrument = 'guitar.'
# his_name = 'Robert Johnson'
# artist_intro = his_name + what_he_does + his_instrument
# print (artist_intro)

# #2
# num = 1
# string = '1'
# num2 = int(string)
# print(num + num2)

# #3
# words = 'words'*3
# print(words)

# #4
# words = 'a loooooong word'
# num = 12
# string = 'bang!'
# total = string * (len(words) - num)
# print(total)

# #5
# name = 'My name is Mike'
# print(name[0])
# print(name[-4])
# print(name[11:14])
# print(name[11:15])
# print(name[5:])
# print(name[:5])

# #6
# word = 'friends'
# find_the_evil_in_your_friends = \
#     word[0] + word[2:4] + word[-3:-1]
# print(find_the_evil_in_your_friends)

# #7
# phone_number = '185-0000-6666'
# hiding_number = phone_number.replace(phone_number[:9], '*'*9)
# print(hiding_number)

# #8
# search = '168'
# num_a = '1386-168-0006'
# num_b = '1681-222-0006'
# print(search + ' is at ' + str(num_a.find(search))+ ' to ' + \
#       str(num_a.find(search) + len(search)) + ' of num_a')
# print(search + ' is at ' + str(num_b.find(search))+ ' to ' + \
#       str(num_b.find(search) + len(search)) + ' of num_b')

# #9
# print('{} a word she can get what she {} for.'.format('With','came'))
# print('{preposition} a word she can get what she {verb} for.'\
#       .format(preposition = 'With',verb = 'came'))
# print('{0} a word she can get what she {1} for.'.format('With','came'))
#
# city = input("write down the name of city:")
# url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)
# print(url)

# #10
# def fahrenheit_converter(C):
#     fahrenheit = C * 9/5 + 32
#     return str(fahrenheit) + '˚F'
# T = int(input('请输入摄氏温度(˚C)：'))
# C2F = fahrenheit_converter(T)
# print('转换为华氏温度是：' + C2F)

# #练习题1
# def weight_converter(g):
#     kg = g/1000
#     return str(kg) + 'kg'
# g2kg = weight_converter(150)
# print(g2kg)

# #练习题2
# #求直角三角形斜边长
# import math
# def third_side(a, b):
#     c = math.sqrt(a*a + b*b)
#     return 'The right triangle third side\'s length is ' + str(c)
# a = int(input('Please input the 1st side\'s length:'))
# b = int(input('Please input the 2nd side\'s length:'))
# c = third_side(a, b)
# print(c)

# #11
# print('   *','  * *',' * * *','   |  ',sep='\n')

# #12
# file = open('E:/Python/WebCrawler/TextDic/text.txt','w')
# file.write('Hello, world!')

# #13文本过滤器
# def text_create(name, msg):
#     root_path = 'E:/Python/WebCrawler/TextDic/'
#     full_path = root_path + name + '.txt'
#     file = open(full_path, 'w')
#     file.write(msg)
#     file.close()
#     print('Done')
# # text_create('hello', 'hello ZYU')
#
# def text_filter(word, censored_word = 'lame', changed_word = 'Awesome'):
#     return word.replace(censored_word, changed_word)
# # word = text_filter('Python is lame!')
# # print(word)
#
# def censored_text_create(name, msg):
#     clean_msg = text_filter(msg)
#     text_create(name, clean_msg)
# censored_text_create('Try', 'You\'re lame!lame!lame!')

# #14
# album = ['Black Star', 'David Bowie', 25, True]
# album.append('new song')
# print(album[0], album[-1])

# #15
# def account_login():
#     password = input('Password:')
#     if password == '12345':
#         print('Login success!')
#     else:
#         print('Wrong password or invalid input!')
#         account_login()
# account_login()

# #16
# pwd_list = ['*#*#', '12345']
# def account_login():
#     pwd = input('Password:')
#     pwd_right = pwd == pwd_list[-1]
#     pwd_reset = pwd == pwd_list[0]
#     if pwd_right:
#         print('Login success!')
#     elif pwd_reset:
#         new_pwd = input('Input new password:')
#         pwd_list.append(new_pwd)
#         print('Your password has changed successfully!')
#         account_login()
#     else:
#         print('Wrong password or invalid input!')
#         account_login()
# account_login()

# #17
# for every_letter in 'Hello world':
#     print(every_letter)
# for num in range(1,11):
#     print(str(num) + ' + 1 = '+ str(num + 1))

# #18
# songs_list = ['Holy Diver', 'Thunderstruck', 'Rebel Rebel']
# for song in songs_list:
#     if song == 'Holy Diver':
#         print(song,'- Dio')
#     elif song == 'Rebel Rebel':
#         print(song, '- David Bowie')
#     elif song == 'Thunderstruck':
#         print(song,'- AC/DC')

# #19乘法表
# def multiplication_table(base):
#     for i in range(1,base+1):
#         for j in range(1,i+1):
#             print('{} X {} = {}'.format(j, i, i*j), end="  ")
#             if i == j:
#                 print('')
# multiplication_table(9)

# #20 密码输入错误超过3次就结束
# pwd_list = ['*#*#', '12345']
# def account_login():
#     count = 0
#     while count < 3:
#         pwd = input('Password:')
#         pwd_right = pwd == pwd_list[-1]
#         pwd_reset = pwd == pwd_list[0]
#         if pwd_right:
#             print('Login success!')
#             break
#         elif pwd_reset:
#             new_pwd = input('Enter new password:')
#             pwd_list.append(new_pwd)
#             print('Your password has changed successfully!')
#             count = 0
#         else:
#             print('Wrong password or invalid input!')
#             count = count + 1
#     else:
#         print('Your have entered wrong password 3 times!')
# account_login()

# #P70 练习题1
# def ten_files():
#     #root_path = 'E:/Python/WebCrawler/TextDic/tenfiles/'
#     for i in range(1,11):
#         #full_path = root_path + str(i) + '.txt'
#         full_path = 'E:/Python/WebCrawler/TextDic/tenfiles/{}.txt'.format(str(i))
#         file = open(full_path, 'w')
#         file.write(str(i))
#         file.close()
# ten_files()

# #P70 练习题2
# def invest(amount, time, rate = 0.05):
#     for i in range(1, time+1):
#         print('year',str(i)+': $'+str(amount*(1+rate)**i))
# pri_amount = int(input('principal amount:'))
# pri_time = int(input('how many years:'))
# invest(pri_amount, pri_time)

# #P70 练习题3
# def even_within_100():
#     print('1~100内的偶数是：', end='')
#     for i in range(1, 101):
#         if i%2 == 0:
#             print(str(i), end=' ')
# even_within_100()

# #P72 综合练习，猜大小
# import random
# def small_game():
#     print('<<<< GAME STARTS! >>>>')
#     your_input = input('Big or Small:')
#     print('<<<< ROLE THE DICE! >>>>')
#     point_list = [random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7)]
#     point_sum = sum(point_list)
#     if point_sum >=11 and point_sum <= 18:
#         result = 'Big'
#     if point_sum >=3 and point_sum <= 10:
#         result = 'Small'
#     if your_input == result:
#         rtn = 'Win'
#     else:
#         rtn = 'Lose'
#     print('The points are',str(point_list),'You',rtn+'!')
# small_game()

# #P76 练习1
# import random
# def roll_dice(number = 3):
#     print('<<<<<<<< ROLE THE DICE! >>>>>>>>')
#     points = []
#     while number > 0:
#         points.append(random.randrange(1, 7))
#         number = number - 1
#     return points
#
# def roll_result(total):
#     isBig = 11 <= total <= 18
#     isSmall = 3 <= total <= 10
#     if isBig:
#         return 'Big'
#     if isSmall:
#         return 'Small'
#
# def start_game():
#     your_money = 1000
#     while your_money > 0:
#         print('<<<<<<<< GAME STARTS! >>>>>>>>')
#         choices = ['Big', 'Small']
#         your_choices = input('Big or Small:')
#         if your_choices in choices:
#             try:
#                 your_bet = int(input('How much you wanna bet ? - '))
#             except ValueError:
#                 print('You must enter a number!')
#                 continue
#             if your_bet > your_money:
#                 print('The money you owned is less than that you bet!')
#                 continue
#             points = roll_dice()
#             total = sum(points)
#             youWin = your_choices == roll_result(total)
#             if youWin:
#                 your_money = your_money + your_bet
#                 print('The points are',points,'You win !')
#                 print('You gained {}, you have {} now.'.format(your_bet, your_money) )
#             else:
#                 your_money = your_money - your_bet
#                 print('The points are',points,'You lose !')
#                 print('You lost {}, you have {} now.'.format(your_bet, your_money))
#             if your_money <= 0:
#                 print('GAME OVER!')
#         else:
#             print('Invalid inputs')
# start_game()

# #P77 练习题2
# def pho_num_check():
#     cn_mobile = \
#         [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 147, 178, 1705]
#     cn_union = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709]
#     cn_telecom = [133, 153, 180, 181, 189, 177, 1700]
#     flag = True
#     while flag:
#         try:
#             your_input = input('Enter your phone number :')
#             your_num = int(your_input)
#         except ValueError:
#             print('You must enter digits!')
#             continue
#         if len(your_input) != 11:
#             print('Invalid length, your number should be in 11 digits!')
#             continue
#         else:
#             first_three = int(your_input[0:3])
#             first_four = int(your_input[0:4])
#             if first_three in cn_mobile or first_four in cn_mobile:
#                 print('Operator :  China Mobile')
#                 print('We\'re sending verification code via text to your phone: {}'.format(your_num))
#                 flag = False
#             elif first_three in cn_union or first_four in cn_union:
#                 print('Operator :  China Union')
#                 print('We\'re sending verification code via text to your phone: {}'.format(your_num))
#                 flag = False
#             elif first_three in cn_telecom or first_four in cn_telecom:
#                 print('Operator :  China Telecom')
#                 print('We\'re sending verification code via text to your phone: {}'.format(your_num))
#                 flag = False
#             else:
#                 print('No such a operator.')
# pho_num_check()

# #21列表list
# #列表的增删改查
# fruit = ['pineapple','pear']
# print(fruit)
# #增
# fruit.insert(1,'grape')
# print(fruit)
# fruit[0:0] = ['orange']
# print(fruit)
# #删
# fruit.remove('grape')
# print(fruit)
# del fruit[1:2]
# print(fruit)
# #改
# fruit[0] = 'Grapefruit'
# print(fruit)
# #查
# periodic_table = ['H','He','Li','Be','B','C','N','O','F','Ne']
# print(periodic_table[0])
# print(periodic_table[-2])
# print(periodic_table[0:3])
# print(periodic_table[-10:-7])
# print(periodic_table[-10:])
# print(periodic_table[:9])

# # 22字典Dict
# NASDAQ_code = {
#     'BIDU':'Baidu',
#     'SINA':'Sina'
# }
# print(NASDAQ_code)
# # 增
# NASDAQ_code['YOKU'] = 'Youku'
# print(NASDAQ_code)
# NASDAQ_code.update({'FB':'Facebook','TSLA':'Tesla'})
# print(NASDAQ_code)
# # 删
# del NASDAQ_code['FB']
# print(NASDAQ_code)
# # 改
# NASDAQ_code['BIDU'] = 'baidu'
# print(NASDAQ_code)
# # 查
# print(NASDAQ_code['BIDU'])

# # 23元组Tuple
# # 只可查询，不能增删改
# # 查
# letters = ('a','b','c','d','e','f','g')
# print(letters[0])

# # 24集合Set
# # 集合不能被切片和索引，能做集合运算，能增删
# # 增
# a_set = {1,2,3,4}
# print(a_set)
# a_set.add(5)
# print(a_set)
# # 删
# a_set.discard(3)
# print(a_set)

# # 25多重循环
# num_list = [6,2,7,4,1,3,5]
# sorted_list_shunxu = sorted(num_list)
# sorted_list_nixu = sorted(num_list,reverse=True)
# print(num_list)
# print(sorted_list_shunxu)
# print(sorted_list_nixu)
# str_list = ['x','y','z','l','m','n','i','j','k']
# for a,b in zip(sorted(num_list),str_list):
#     print(b,'is',a)

# # 26推倒式
# import time
# a = []
# t0 = time.clock()*1000
# for i in range(1,20000):
#     a.append(i)
# print(time.clock()*1000 - t0,'ms process time')
# t0 = time.clock()*1000
# b = [i for i in range(1,11)]
# print(time.clock()*1000 - t0,'ms process time')
# c = [i**2 for i in range(1,10)]
# d = [j**2 for j in range(1,10)]
# e = [n for n in range(1,10) if n%2==0]
# f = [letter.lower() for letter in 'QWERTYUIOP']
# print(c)
# print(d)
# print(e)
# print(f)
# g = {i:i+1 for i in range(1,10)}
# h = {i:j for i,j in zip(range(1,6),'abcde')}
# l = {i:j.upper() for i,j in zip(range(1,6),'abcde')}
# print(g)
# print(h)
# print(l)
# letters = ['a','b','c','d','e','f','g','h','i','j','k']
# for num,letter in enumerate(letters):
#     print(letter,'is',num+1)

# # 27 词频统计
# import string
# import time
# t0 = time.clock()
# path = 'E:/Python/WebCrawler/TextDic/Walden.txt'
# with open(path,'r') as text:
#     words = [raw_words.strip(string.punctuation).lower() for raw_words in text.read().split()]
#     words_index = set(words)
#     counts_dict = {index:words.count(index) for index in words_index}
# for word in sorted(counts_dict,key=lambda x: counts_dict[x],reverse=True):
#     print('{} -- {} times'.format(word,counts_dict[word]))
# print(time.clock() - t0,'seconds process time')
