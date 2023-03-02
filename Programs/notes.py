# try:
#     first = int(input("Enter first Number: "))
#     second = int(input("Enter Second Number: "))
#     result = first/second
#     print("Result iis: ",result)
#     try:
#         store = eval(input("Enter multiple Objects: "))
#         index = int(input("Enter index number: "))
#         print("Index is: ",store[index])
#     except IndexError as e:
#         print(e)
#     else:
#         print("No error in inner try block")
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# else:
#     print("No error in outer try!")

# try:
#     first = int(input("Enter first Number: "))
#     second = int(input("Enter Second Number: "))
#     result = first/second
#     print("Result iis: ",result)
#     try:
#         store = eval(input("Enter multiple Objects: "))
#         index = int(input("Enter index number: "))
#         print("Index is: ",store[index])
#     except IndexError as e:
#         print(e)
#     finally:
#         print("inner block")
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# finally:
#     print("outer block")

# Terminating pvm abnorally

# import os
# try:
#     print("Try")
#     os._exit(0)
# except:
#     print("Except")
# finally:
#     print("Finally")


# class CheckEmployeeSalary:
#         def __init__(self,arg):
#                 self.msg = arg
# class Employee:
#         def __init__(self,eno,ename,esal):
#                 self.eno = eno
#                 self.ename = ename
#                 self.esal = esal
# eno = int(input("Enter Employee Number: "))
# ename = input("Enter Employee name: ")
# esal = int(input("Enter Employe salary: "))
# employee = Employee(eno,ename,esal)
# if employee.esal<0:
#         cem = CheckEmployeeSalary("Salary must be positive !!")
#         raise cem
# else:
#         print("Employee Number is: ",employee.eno)
#         print("Employee name is: ",employee.ename)
#         print("Employee salary is: ",employee.esal)


class Demo:
    def m3(self):
        print("m3()method__")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        num3 = num1 / num2
        print("Result is: ", num3)
    def m2(self):
        print("m2() method__")
        self.m3()
    def m1(self):
        print("m1() metthod__")
        try:
            self.m2()
        except ZeroDivisionError:
            print("Can't deivide by zero")
d = Demo()
d.m1()














