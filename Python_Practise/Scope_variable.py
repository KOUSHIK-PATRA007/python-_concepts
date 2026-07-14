# scope is local variable and global variable
# no1=local(func will check lcal level first)
# no2=Enhance level(if func will not find anything in local
# than than it will go to the Enhanced level)
# no3= Global level(if func will not find both the level that time controller will go to the
# global level and search element in there)
# no4= Builtin/ninbuilt level (we can print the inbuilt value
# by calling it) example:-pi=3.14
from html.parser import interesting_normal

#######################----------NO-1
# def inner():
#     x=10
#     return x
# print(inner())
######################-----------NO.2

# def outer():
#  y=50
#  def iner():
#      x='hai'
#      print(x)
#      print(y)
#  iner()
# outer()

####################################------NO.3
# from math import pi
#
# def outer():
#
#  def iner():                    o/p=3.141592653589793/////hai
#
#      x='hai'
#
#      print(pi)
#      return x
#
#  print(iner())
# outer()

##################################-----------NO.4
# from math import pi
#
# def outer():
#  pi=5000
#  def iner():                o/p=5000 ///  hai
#      x='hai'
#      print(pi)
#      return x
#  print(iner())
# outer()
###############################-------------NO.5
from math import pi
# def outer():
#
#  def iner():
#      x='hai'
#      pi = 5000
#      print(pi)
#      print(x)
#
#  return iner
#
# # outer()()
# result=outer()##<-----iner
# result()











































