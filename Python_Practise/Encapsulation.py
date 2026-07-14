# class Car:
#     # engine_type="Petrol"
#     # variant="Top"
#     def __init__(self,name,color):
#         self._name=name
#         self.__color=color
#
#
#     def Doors(self):
#         return f"{self._name} has 5 doors"
#
#     def Wheels(self):
#         return f"The car is {self.__color}"
#
# c1=Car('farrari','red')
# print(c1.Doors())
# print(c1.Wheels())

#######################################
#
# class Car:
#     # engine_type="Petrol"
#     # variant="Top"
#     def __init__(self,name,color):
#         self._name=name
#         #######---declear public access specifire var using (_) underscore
#         self.__color=color
#         #####---decler privet access specifire var using (__)double underscore
#
#
#     def Doors(self):
#         return f"{self._name} has 5 doors"
#
#     def Wheels(self):
#         return f"The car is {self.__color}"
#
# class Suv(Car):
#     def gate(self):
#         return f" {self._name} car has gate"
#     def light(self):
#         return f" {self._Car__color} car has light"
#
#
# c1=Car('farrari','red')
# print(c1.Doors())
# print(c1.Wheels())
#
# print(c1.__dict__)
# c2=Suv('lambo','green')
# print(c2.gate())
#
# print(c2.light())
#
# print(c2.__dict__)
# # ####################################################
# class Car:
#     _enginetype="Petrol"
#     __variant="Top"
#     def __init__(self,name,color):
#         self._name=name
#         #######---declear public access specifire var using (_) underscore
#         self.__color=color
#         #####---decler privet access specifire var using (__)double underscore
#
#
#     def Doors(self):
#         return f"{self._name} has 5 doors"
#
#     def Wheels(self):
#         return f"The car is {self.__color}"
#
# class Suv(Car):
#     def gate(self):
#         return f" {self._name} car has gate"
#     def light(self):

#         return f" {self._Car__color} car has light"

################--------we are using class name to fetch the
## privet member/var in the other class

# c1=Car('farrari','red')
# print(c1.Doors())
# print(c1.Wheels())
#
# print(c1.__dict__)
# c2=Suv('lambo','green')
# print(c2.gate())
#
# print(c2.light())
#
# print(c2.__dict__)
# ####***********************
# print(c1._enginetype)
# print(c2._enginetype)


###################################


























