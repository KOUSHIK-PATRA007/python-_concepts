import time

def outer(func): ##-------- this func will not take the paremeters so for that we have
                       ####------ taken inner function and pass the paremeter into that as arguments
    def inner(*args,**kwargs):
        print("Task to be executed before calling main func")
        func(*args,**kwargs)
        print("Task to be executed after calling main func")
    return inner
@outer
def spam1(a,b):
    print(f"{a+b}")

spam1(2,3)

# def Thank_You(func):
#     def inner(*args,**kwargs):
#         print("User")
#         func(*args,**kwargs)
#         print("Thank You")
#     return inner
#
# @Thank_You
# def spam1():
#     print("Welcome")
#
# @Thank_You
# def spam2():
#     print("Hello")
#
# @Thank_You
# def spam3():
#     print("Python_RMG")
# # spam1()
# # spam2()
# # spam3()
#
# def time_duration(func):
#     def inner(*args,**kwargs):
#         start_time=time.time()
#         func(*args,**kwargs)
#         end_time=time.time()
#         print(f"The total time taken is {end_time-start_time}")
#     return inner
#
#
# def type_check(func):
#     def inner(*args,**kwargs):
#         res=func(*args,**kwargs)
#         if type(res)==str:
#             print("yes")
#         else:
#             print("No")
#     return inner
#
# @type_check
# def some_func():
#     return "Welcome to bangalore"
#
# @type_check
# def some_random_func():
#     return "Welcome to Karnataka"
#
# some_func()
# some_random_func()
