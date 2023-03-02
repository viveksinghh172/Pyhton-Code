# Lambda

# c = lambda num: num*num*num
# print(c(3))

# c = lambda num1,num2: num1+num2
# print(c(2,3))

# res = lambda first,second,choice: first+second if choice == "+" else first-second if choice == "-" else 'Invalid Operator'
# print(res(10,5, "+"))


# Filter
#filter(function,iterable)


# l = [1,2,3,4,5,6,7,8,9,10]
# def check(num):
#     if num%2 == 0:
#         return True
# #even = list(filter(check,l))
# even = list(filter(check,range(1,11)))
# print(even)



# Filter using lambda

# l = [1,2,3,4,5,6,7,8,9,10]
# even = list(filter(lambda num: num%2 == 0, l))
# odd = list(filter(lambda num: num%2 != 0,range(1,11)))
# print(odd)
# print(even)


#Map() function

# l = [1,2,3,4,5,6,7,8,9,10]
# even = list(filter(lambda num: num%2 == 0, l))
# print(even)
# cube = list(map(lambda num: num*num*num, even))
# print(cube(3))




# Decorator

# def change_wish(func):
#     def inner(name):
#         if name == "Rajeev":
#             print("Hello",name,"Sir morning")
#         else:
#             return func(name)
#     return inner
# @change_wish
# def wish(name):
#     print("Hello",name,"Sir Good Morning")
# w = change_wish(wish)
#
# w = ("Vishal")
# w = ("Rajeev")
# w = ("Junaid")

# def change_divide(func):
#     def inner(num1,num2):
#         if num1<num2:
#             num1,num2 = num2,num1
#         return func(num1,num2)
#     return inner
# @change_divide
# def divide(num1,num2):
#     print(num1/num2)
# divide(10,2)
# divide(2,10)


# Program to count frequency in a dictionary

# from collections import Counter
# def test(dictt):
#     result = Counter(dictt.values())
#     return result
# dictt = {'v':10,'vi':20,'vii':30,'viii':10,'ix':20}
# print("\n Original Dictionary is: ")
# print(dictt)
# print("\n Count frequency of that dictionary: ")
# print(test(dictt))

# Threading

# import threading
# t = threading.current_thread()
# print(t.getName())

# from threading import Thread
# def display():
#     print("My first thread example without using a class: ")
# t = Thread(target=display)
# t.start()
# print("Main thread")

# from threading import Thread
# class MyThread(Thread):
#     def run(self):
#         print("My thread class by extending a thread class:")
# t = MyThread()
# t.start()
# print("Main Thread")

# from threading import Thread
# class MyThread:
#     def m1(self):
#         print("Thread example without exteding a thread class: ")
# obj = MyThread()
# t = Thread(target = obj.m1)
# t.start()
# print("Main thread")


# name = None
# try:
#     print("Length is: ",len(name))
# except TypeError:
#     print("Please initiate the variable!")
# print("All is well")

# store = eval(input("Enter the multiple objects: "))
# index = int(input("Enter the index position: "))
# print("Index is: ",store[index])

# store = eval(input("Enter multiple objects: "))
# while True:
#     index = int(input("Enter index position: "))
#     try:
#         print("Object is: ",store[index])
#     except IndexError:
#         print("Check your index position!!")
#     choice = input("Do you want to continue...")
#
#     if choice == "no":
#         break
# print("All is well")


# try:
#     print("Open connection")
#     print("Process data!")
#     age = int(input("Enter age: "))
# except IndexError:
#     print("Check age input!")
# finally:
#     print("Close connection !!")

# a = 2 + 2j
# b = 3j
# print(a+b)

# my_list = (1,2,3)
# if type(my_list) is list:
#     print(1 == 1)


# a, b = 1<2, 2>3
# my_list = [a, b, a==b];print(my_list)


# my_list = [
#     i for i in range(10) if i>5    
# ]
# print(my_list)


# a={1,2,3}
# b={3,4,5}
# print((a|b)==(a+b))


# import pygal
# wordmap = pygal.maps.world.World()
# wordmap.title = 'Countries'
# wordmap.add('Random Data', {
#     'aq' : 10, 'cd' : 30, 'de' : 40, 'eg' : 50,
#     'ga' : 45, 'hk' : 23, 'in' : 70, 'jp' : 54,
#     'nz' : 41, 'kz' : 32, 'us' : 66 })
# wordmap.render_to_file('abc.svg')