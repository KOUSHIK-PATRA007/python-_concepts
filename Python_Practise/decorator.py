# Decorator it is use to modify  the


#####################################------------NO.1
# def coustom_decorator(func):
#     def inner(*args, **kwargs):
#         print('before hii')
#         func()
#         print('after hiiii')
#     return inner
#
#  # its will return the inner to the custom_decorator
#
#
#  # @coustom_decorator  first=coustom_decorator(first)
# @coustom_decorator
# def first():
#     print('first go to coustom_decorator')
#
#
# @coustom_decorator
# def second():
#     print('second go to coustom_decorator')
#
# first()
# second()


#############################################-------NO.2
#
# def coustom_decorator_1(func):
#     def inner(*args, **kwargs):
#         print('before hii')
#         func()
#         print('after hiiii')
#     return inner
# # its will return the inner to the custom_decorator
#
# def coustom_decorator_2(func):
#     def inner(*args, **kwargs):
#         print('before in coustom_decorator_2')
#         func()
#         print('after in coustom_decorator_2')
#     return inner
#
#
# # its will return the inner to the custom_decorator
#
#
# # @coustom_decorator  first=coustom_decorator(first)
# @coustom_decorator_1
# def first():
#     print('goooooo first go to coustom_decorator1')
#
#
# @coustom_decorator_2
# def second():
#     print('welcome    second go to coustom_decorator2')
#
#
# first()
# second()

#######################################-----NO.3
#
# import time
# def outer(func):
#     def inner(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print('execution time is ', execution_time)
#
#         return result
#     return inner
# @outer
# def devide(a,b):
#     print(a/b)
# @outer
# def multiplication(a,b):
#     time.sleep(5)
#     print(a*b)
#
# devide(4,5)
# multiplication(2,6)

#####################################-------NO.4

# def outer1(func):
#     def inner(*args, **kwargs):
#         print('hiiiii')
#         func()
#         print('this word is change into upper')
#
#     return inner
# @outer1
# def st():
#     t='hello'
#     print(t.upper())
# st()
########################################---------NO.5

def outer1(func):
    def inner(*args, **kwargs):
        print('calling outer1')
        print(func())
        print('this word is change into upper')

    return inner
def outer2(func):
    def inner(*args, **kwargs):
        print('outer 2')
        print(func())
        print('this word is change into lower')
    return inner
@outer1
def st():
    t='hello'
    return t.upper()
@outer2
def st1():
    t2='HOW ARE YOU'
    return t2.lower()
st()
st1()
######################################--------NO.6

































