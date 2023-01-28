# def n():
#     print('hi')
# n()   #hi 
# def a(s):
#     print('hi',s)
# a('pooja')   #hi pooja 
# def d(*names):
#     print('hi',names[3])
# d('pooja','kiran','bhargavi','sravani','chandu')    #hi sravani
# def n(n,a):
#     print('my name is',n,'and age is',a)
# n(n='pooja',a='22')   #my name is pooja and age is 22
# def b(n,a):
#      print('my name is',n,'and age is',a)
# n=input('enter your name:')
# a=input('enter your age:')  
# b(n,a)  #my name is pooja and age is 22 
# def r(x,y):
#     print(x*y)#15
# r(5,3)  
# or  
# def r(x,y):
#     return(x*y)
# print(r(5,3))    #15
# def f(a,b):
#     return a+b,a*b
# a=int(input())  #6   
# b=int(input())#4
# a,b=[int(x)for x in input().split()]#6 4
# print(f(a,b))#(10,24)
'''builtin_functions'''
# x=10
# print(bin(x))
# # y=bin(x)
# print(y)
# print(dir(__builtins__))
# print(sorted([1,9,4,7,5,8,3,6,2]))#[1,2,3,4,5,6,7,8,9]
# a=['h','p','Y','t','D','F']
# print(sorted(a))#['D','F','Y','h','p','t']
# a=[1,6,'p',4]
# print(all(a))
# a=[1,6,'',4]
# print(all(a))#False
# a=[1,6,' ',4]
# print(all(a))#True
# a=[1,6,0,4]
# print(all(a))#false
# a=[None,1,9]
# print(all(a))#FALSE
# a=[False,1,9]
# print(all(a))#false
# a=[False,None,0,]
# print(any(a))#false
# a=[6,None,False,0]
# print(any(a))#true:because value is there in a 
# a=[True,False,None]
# print(any(a))#true
# a=[1]
# print(bool(a))#true
# a=(0)
# print(bool(a))#false
# a=None
# print(bool(a))#false
# print(eval('2+3.4'))#5.4
# print(eval('2+5'))#7
# print('sum =', sum((4,8,2,7,6)))#sum = 27
# print('sum =',sum((2.4,5)))#sum = 7.4
print(chr(97))#a
print(chr(90))#Z
print(ord('h'))#104
print(ord('H'))
