'''
##--- MAP() function ----->
##---The map() function executes a already specified function
#--- for each item in an iterable.
##---The item is sent to the function as a parameter.
##--Syntax--->> map(function, iterables)

'''

#
# def square(num):
#     return num**2
# var=map(square,range(10))
# # print(var)##--->> <map object at 0x0000026100940490>
# print(list(var))###--->> type caste into list
#
# ###--------------------->>>>>>>>>>>>>>>>>>
# def square(num):
#     return num**2
# l=[1,2,3,4,5,6,7,8,9]
# var1=map(square,l)
# print(list(var1))
# #----------OR-------->>>
# def square(num):
#     return num**2
# print(list(map(square,l)))
# ###------------------------->>>>>>>>
d=['special','apple','banana']
def item_len(ele):
    return len(ele)
var3=map(item_len,d)
print(list(var3))
# ####----------------------->>>
# def myfunc(a):
#   return len(a)
# x = map(myfunc, ('apple', 'banana', 'cherry'))
# print(list(x))
# #############----------------->>>>>>>>>>>>>>
# def myfunc(ele):
#     d1={}
#     d1[ele]=len(ele)
#     return d1
# res = map(myfunc, ('apple', 'banana', 'cherry'))
# print(list(res))
# ##############------------------->>>>>>>>>>>>
# def myfunc(a, b):
#   return a + b
# x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
# #convert the map into a list, for readability:
# print(list(x))
# ############------------------>>>>>>>>>>>>
# def myfunc(a, b):
#   return a + b
# l1=('apple', 'banana', 'cherry')
# l2=('orange', 'lemon', 'pineapple')
# x = map(myfunc, l1,l2 )
# #convert the map into a list, for readability:
# print(list(x))
# #####################----------------->>>>>>>>>>>>>>>
# def myfunc(a, b):
#   return a + b
# l1=['apple', 'banana', 'cherry']
# l2=['orange', 'lemon', 'pineapple']
# x = map(myfunc, l1,l2 )
# #convert the map into a list, for readability:
# print(list(x))

###############------------>>>>>>>>>>>>>>>>>>>>########################

#>>>>>>>>>>>>>>>------FILTER()-------------------->>>>>>>>>>>
#
# def check_odd(num):
#     if num %2==1:
#         return num
# var5=list(map(check_odd,range(11)))
# '''
# #-->output-->[None, 1, None, 3, None, 5, None, 7, None, 9, None]
# #---->MAP will check the condition for all nums in given range
# #---> It will give unnecessary output for all the nums
# '''
# var6=list(filter(check_odd,range(11)))
# '''
# #-->output-->[1, 3, 5, 7, 9]
# #--> FILTER will check the range and compare with the condition
# #---->It will give output filter only those nums which are satisfied
# #-->with the condition
# '''
# print(var5)
# print(var6)
# ################------------>>>>>>>>>>>>>>>>>>--------->>>>>>>>
#
# def check_odd(num):
#     if num %2==1:
#         return "ODD_NO"##---> it will print ODD_NO instead of all the odd nums
# var5=list(map(check_odd,range(11)))
# var6=list(filter(check_odd,range(11)))
# print(var5)
# print(var6)


# class Cat:
#     def sound(self):
#         print("Meow")
#
# class Dog:
#     def sound(self):
#         print("Bark")
#
# for pet in (Cat(), Dog()):
#     pet.sound()























