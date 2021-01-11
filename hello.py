# name="ADa lovelace"
# print(name.lower())
# print(name)

# first_name="ada"
# last_name="lovelace"
# full_name=first_name+" "+last_name
# print(full_name)

# print("python")
# print("\tpython")

# name=" python "
# print(name.strip())
# print(name)

# a=23
# print(str(a)+"aaa")

# print(3/2)

# import this

# import antigravity

# a=[1,"sss",3,4]
# print(a)
# a.append(5)
# print(a)
# a.insert(0,5)
# print(a)
# del a[1]
# print(a)
# print(a.pop())
# print(a)
# a.pop(0)
# print(a)
# a.remove('sss')
# print(a)

# a,b=1,2
# print(a)


# a=[4,1,3,2]
# a.sort()
# print(sorted(a,reverse=True))
# print(a)

# a=[1,2,3,4]
# a.reverse()
# print(a)
#

# a=[1,2,3,4]
# print(len(a))

# a=[1,2,3,4]
# for x in a:
#     print(x)
# print(x)
#
# massage="hello"
#     print(massage)


# for value in range(1,5):
#     print(value)

# a=list(range(1,6))
# print(a)

# a=list(range(2,11,2))
# print(a)

# squares=[]
# for value in range(1,11):
#     squares.append(value**2)
# print(squares)

# digits=[1,2,3,4,5,6,7,8,9,0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# chars=['a','b','c']
# print(min(chars))
# print(max(chars))

# squares=[value**2 for value in range(1,11)]
# print(squares)

# a=list(range(1,1000001))
# print(sum(a))

# a=[1,2,3,4,5,6]
# print(a[2:4])
# print(a[:4])
# print(a[2:])
# print(a[-3:])

# a=[1,2,3,4,5,6]
# for value in a[2:4]:
#     print(value)

# a=[1,2,3,4]
# b=a[:]
# print(b)

# a=(1,2,3)
# print(a[1])

# for x in range(1,5):
#               print(x)

# a=[1,2,3,4]
# print(1 not in a)

# a=1
# if a==1: print(1)

# a=2
# if a==1:
#     print(1)
# elif a==2:
#     print(2)

# a=[]
# if a:
#     print('a not empty')
# else:
#     print("a is empty")

# a=b=[1,2,3]
# # c=[1,2,3]
# # if a is c:
# #     print(1)
# # else:
# #     print(2)
# # print(id(a))


# a={'color':'green',2:5}
# print(a[2])

# a = {'color': 'green', 'points': 5, }
# print(a)
# a['x'] = 0
# a['y'] = 1
# print(a)
# a['x'] = 1
# print(a)
# a['x'] = a['x']+1
# print(a)
# del a['x']
# print(a)
#

# a={1:2,2:2,3:4}
# for k,v in a.items():
#     print(str(k)+' '+str(v))
# for k in a.keys():
#     print(k)
# for k in a:
#     print(k)
# for v in a.values():
#     print(v)
# for v in set(a.values()):
#     print(v)

# for x in range(3):
#     print(x)

# a={1:[1,2,3]}
# print(a[1][0])

# message=input("say something:")
# print(message)

# age = float(input("how old are you?"))
# print(age)

# a=1
# while a<=5:
#     print(a)
#     a+=1

# a=[1,2,3,4]
# for x in a:
#     print(x)
#     a.pop(1)

# def greet_user(firstname,lastname='wawa'):
#     print('hello '+firstname+lastname)
#
# greet_user('lala')
# greet_user('pan','guansen')
# greet_user(firstname='pan', lastname='guansen')
# greet_user(lastname='guansen',firstname='pan')

# def add(a,b):
#     return a+b
# print(add(1,2))

# def a(*b):
#     print(b)
# a()
# a(1)
# a(1,2)

# def a(**b):
#     print(b)
#
# a(a='1')
# a(a='1', b='2')
# a(a='f')

# import test
# test.add(2,4)

# from test import add
# add(2,3)

# from test import add as a
# a(2,3)

# import test as t
# t.add(2,3)

# from test import *
# add(2,3)

# class Dog():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.a=1
#
#     def sit(self):
#         print(self.name+" is sitting")
#
#     def roll_over(self):
#         print(self.name+" is rolled over")
#
#     def output(self):
#         print(self.a)
#
#     def update_a(self,a):
#         self.a=a

# dog = Dog('willie', 6)
# print(dog.name)
# dog.sit()
# dog.output()
# dog.a=2
# dog.output()
# dog.update_a(3)
# dog.output()

# class Hotdog(Dog) :
#
#     def __init__(self,name,age):
#         super().__init__(name,age)

# with open('pi_digits.txt') as file_object:
#     contents=file_object.read()
#     print(contents.rstrip())
#
# with open('pi_digits.txt') as file:
#     for line in file:
#         print(line.rstrip())


# with open('pi_digits.txt') as file2:
#     lines=file2.readlines()
# print(lines)
# for line in lines:
#     print(line.rstrip())

# filename='programming.txt'
# with open(filename,'a') as file3:
#     file3.write("I love programming.")

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("lala")

# title="Alice in Wonderland"
# words=title.split()
# print(words)

# print("%d",1)
# print("%d"%1)
# print("%03d"%3)
# print("%.3f"%3)
# print("%03d %.3f"%(3,3))
# name='pan'
# age=18
# print(f"我是{name}，我{age}岁了")
# print("lalala",end='..')
# print("lla")
# a=3
# b=2
# c=a if a>b else b
# print(c)
# s = 'university'
# for i in s:
#     if i == 'a':
#         print('no')
#         break
#     print(i)
"""正常循环结束会执行"""
# else:
#     print("zc")


# import json
# numbers=[2,3,5,7,11,13]
# numbers=(2,3,4)
# numbers={"color": "yellow"}
# filename='numbers.json'
# with open(filename,'w') as file4:
#     json.dump(numbers,file4)
#
# with open(filename) as file5:
#     numbers=json.load(file5)
# print(numbers)

# a = ' "aaaa" '
# b = eval(a)
# print("aaaa")
# print(b)

# def gen(n):
#     for i in range(n):
#         yield i**2

# for i in gen(5):
#     print(i, end=" ")
