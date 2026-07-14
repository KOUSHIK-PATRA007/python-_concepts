'''
 #### ABSTRACTION
'''

#
# from abc import ABC, abstractmethod
#
# class laptop (ABC):
#     @abstractmethod
#     def camera(self):
#         return f'laptop has camera'
#     @abstractmethod
#     def window(self):
#         return f'laptop has windows 11'
#     @abstractmethod
#     def processor(self):
#         return f'laptop has ryzen processor'
# ## we cant create object for the abstract class like [ l1 = laptop()]
# ## Can't instantiate abstract class laptop without an implementation
# ## for abstract methods 'camera', 'processor', 'window'
#
# l1 = laptop()
# print(l1.camera())
# print(l1.window())
# print(l1.processor())
###########################--------------------
# #
# from abc import ABC, abstractmethod
# #
# class Laptop (ABC):
#     @abstractmethod
#     def camera(self):
#         return f'laptop has camera'
#     @abstractmethod
#     def window(self):
#         return f'laptop has windows 11'
#     @abstractmethod
#     def processor(self):
#         return f'laptop has ryzen processor'
#
# class Mac (Laptop):
#
#     def camera(self):
#         return f'mac has camera'
#     def window(self):
#         return f'mac has windows 11'
#     def processor(self):
#         return f'mac has ryzen processor'
# m1 = Mac()
# print(m1.camera())
# print(m1.window())
# print(m1.processor())

#######################################-----------------

from  abc import ABC, abstractmethod

# class Laptop (ABC):
#     @abstractmethod
#     def camera(self):
#         return f'laptop has camera'
#     @abstractmethod
#     def window(self):
#         return f'laptop has windows 11'
#     @abstractmethod
#     def processor(self):
#         return f'laptop has ryzen processor'
#
# class Mac (Laptop):
#     def __init__(self,pixel,virson,cores,card):
#         self.pixel = pixel
#         self.virson = virson
#         self.cores = cores
#         self.card = card
#
#
#     def camera(self):
#         return f'mac has {self.pixel} camera'
#     def window(self):
#         return f'mac has windows {self.virson}'
#     def processor(self):
#         return f'mac has ryzen {self.cores} processor'
# ## we can add extra method in child class but
# ## we cant modify those abstract method in child class
#
#     def graphis(self):
#         return f'laptop has graphis {self.card}'
# m1 = Mac('54mp','11','8','gtx')
# print(m1.camera())
# print(m1.window())
# print(m1.processor())
# print(m1.graphis())
################################--------------------
#

# from  abc import ABC, abstractmethod
#
# class Laptop (ABC):###########------Abstract class
#     @abstractmethod
#     def camera(self):########------Abstract method
#         return f'laptop has camera'
#     @abstractmethod
#     def window(self):
#         return f'laptop has windows 11'
#     @abstractmethod
#     def processor(self):
#         return f'laptop has ryzen processor'
#
# class Mac (Laptop):#####--inheriting the parent class(Abstract class)
#     def __init__(self,pixel,virson,cores,card):
# ###---inicilizing variables using init construtor
#         self.pixel = pixel
#         self.virson = virson
#         self.cores = cores
#         self.card = card
#
#
#     def camera(self):
#         return f'mac has {self.pixel} camera'###--implemantation
#     def window(self):
#         return f'mac has windows {self.virson}'###--implemantation
#     def processor(self):
#         return f'mac has ryzen {self.cores} processor'###--implemantation
# ## we can add extra method in child class but
# ## we cant modify those abstract method in child class
# ## we can add differnt method in subclass
#
#     def graphis(self):####---new method i added into this class
#         return f'laptop has graphis {self.card}'
#
# m1 = Mac('54mp','11','8core','gtx')
# print(m1.camera())
# print(m1.window())
# print(m1.processor())
# print(m1.graphis())
#
# class Hp (Laptop):####----inheriting parent class
#     def __init__(self,pixel,virson,cores,backlight):
#         self.pixel = pixel
#         self.virson = virson
#         self.cores = cores
#         self.backlight = backlight

#
#     def camera(self):
#         return f'Hp has {self.pixel} camera'
#
# ##  if i modify any abstract method name in subclass like 'camer'
# ## it will through an error
# ##TypeError: Can't instantiate abstract class Hp
# ## without an implementation for abstract method 'camera'
#
#     def window(self):
#         return f'Hp has windows {self.virson}'
#     def processor(self):
#         return f'Hp has ryzen {self.cores} processor'
#
# ## we can add extra method in child class but
# ## we cant modify those abstract method in child class
# ## we can add differnt method in subclass
#     def rgb(self):
#         return f'laptop has rgb color {self.backlight}'
#
# m2 = Hp('540mp','10','6','red')
# print(m2.camera())
# print(m2.window())
# print(m2.processor())
# print(m2.rgb())















