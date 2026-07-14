from pyexpat import features
## call and crete object,create class,constructor,inicialize constructor
## self is a veriable use to store the current obj address
## oops is design patern , class is a container consist of object intance
# # class is a blueprint or visualization use to create object.visualization its a plan
# of how to create object in this blueprint we use object in that
# # object real world entity or everything in world is a form of object
# # object has attributs and behaviour
# # init is a constructor every time object is created init will be invocked
# class Mobile:
#     type = 'Android'  ####------ class veriable
#     screen = 'Touchble'  ####------ class veriable
#
#     def __init__(self, name, ram, Camera, memory):
#         self.name = name  ####------ instance veriable
#         self.ram = ram  ####------ instance veriable
#         self.Camera = Camera  ####------ instance veriable
#         self.memory = memory  ####------ instance veriable
#
#
#     @classmethod
#     def feature(cls,new_type):
#         cls.type = new_type
#         return f'mobile feature is {cls.type}'
#
#     @staticmethod
#     def static_method():
#         pass
#
#     # @staticmethod
#     # def static_method(cls):  ###--- if you write cls it
#     #     pass  # ---- will become class method
# print(Mobile.feature('ibm'))
# # print(Mobile.feature('ios'))
# a1 = Mobile("samsung","123","123mp","123gb")

# ##########################--------------------------------------------------------

# class Mobile:
#     type='Android'  ####------ class veriable
#     screen='Touchble'  ####------ class veriable
#     def __init__(self,name,ram,Camera,memory):
#         self.name = name     ####------ instance veriable
#         self.ram = ram         ####------ instance veriable
#         self.Camera = Camera ####------ instance veriable
#         self.memory = memory   ####------ instance veriable
#
#     def  mob_name(self):
#         return f'mobaile name is {self.name}'
#     def mob_ram(self):
#         return f'mobaile  ram is {self.ram}'
#     def mob_camera(self):
#         return f'mobaile camera is {self.Camera}'
#     def mob_memory(self):
#         return f'mobaile memory is {self.memory}'
#
#     @classmethod
#     def feature(cls):
#         return f'mobaile feature is {cls.type}'
#     @staticmethod
#     def static_method():
#         pass
#
#     @staticmethod
#     def static_method(cls):###--- if you write cls it
#         pass                  #---- will not become class method because cls just a veriable name
#
#
#
#
# a1 = Mobile("samsung","123","123mp","123gb")
# ## creating object of mobile class and store into a1 reference/instace var.
# a2= Mobile("Apple","12","123mp","123gb")
# print(a1.mob_name())
# print(a1.mob_ram())
# print(a1.mob_camera())
# print(a1.mob_memory())
# print(a2.mob_name())
# print(a2.mob_ram())
# print(a2.mob_camera())
# print(a2.mob_memory())
# a1.name='Ai'
# a2.Camera='5000mp'
# print(a1.name)
# print(a2.Camera)
# # print(a1.mob_ram())
# print(a1.mob_name())
# print(a1.mob_ram())
# print(a1.mob_camera())
# print(a1.mob_memory())
# print(a2.mob_name())
# print(a2.mob_ram())
# print(a2.mob_camera())
# print(a2.mob_memory())
# print(Mobile.type)
# print(Mobile.screen)
# print(Mobile.feature())
# # print(Mobile.name)
# print(a1.type)
# print(a1.__dict__)
# print(a2.type)

# #
########--------NO.2---------INHERITANCE
# singel level inheritance
# class Car:
#
#     def __init__(self,name,brand,model):
#         self.name = name
#         self.brand = brand
#         self.model = model
# class Cardoor(Car):
#
#     def carfeature(self):
#         print(f'{self.name} car model {self.model} has doors')
#
# c1=Cardoor('Toyota','Math',1)
# c1.carfeature()

# multi level inheritance
#
# class Bank:
#     def __init__(self,name,acno,balance):
#         self.name = name
#         self.acno = acno
#         self.balance = balance
#
# class Cust1(Bank):
#
#     def customer(self):
#         return f'{self.name} customer {self.acno} has {self.balance} credits'
#
# class Cust2(Cust1):
#
#     def customer(self):
#         return f'{self.name} customer {self.acno} has {self.balance} credits'
#
# c1=Cust2('chucha',4558667000,5895415)
# print(c1.customer())
# c2=Cust1('chacha',4558667001,5895405)
# print(c2.customer())
##########################################------------

  # multilevel
#
# class Bank:
#     def __init__(self,name,acno,balance):
#         self.name = name
#         self.acno = acno
#         self.balance = balance
#
# class Cust1(Bank):
#     def __init__(self,iden,name,acno,balance):
#         self.iden= iden
#         super().__init__(name,acno,balance)
#
#
#     def customer(self):
#         return f'{self.iden} customer {self.acno} has {self.balance} credits'
#
# class Cust2(Cust1):
#
#     def customer(self):
#         return f'{self.iden} customer {self.acno} has {self.balance} credits'
#
# c1=Cust2('454','chucha','800','500')
# print(c1.customer())
# c2=Cust1('45400','chacha','800','500')
# print(c2.customer())

#########################################

# multiple level


# class Bank:          #################---parent class
#     def __init__(self,name,acno,balance):
#         self.name = name
#         self.acno = acno
#         self.balance = balance
#
# class Cust1:        ############-----parent class
#     def __init__(self,iden):
#         self.iden= iden
#
#         # super().__init__(name,acno,balance)
#
#
#     def custgeo(self):
#         return f'{self.iden} customer {self.acno} has {self.balance} credits'
#
# class Cust2(Bank,Cust1):###########---------child class
#
#     def custamerica(self):
#         return f'{self.name} customer {self.acno} has {self.balance} credits'
#
# ##### controler first search init constructor depends on the parent class you
# ### pass in subclasses and it will check first parent class has init or not
# ## if yes it will initialize if not than it will search for the next class
## init constructor
# c2=Cust2('ghf','111113','312111')
# print(c2.custamerica())




##############################
#
# class Mammal:
#     def mammal_info(self):
#         print("Mammals can give direct birth.")
#
# class WingedAnimal:
#     def winged_animal_info(self):
#         print("Winged animals can flap.")
#
# class Bat(Mammal, WingedAnimal):
#     pass
#
# # create an object of Bat class
# b1 = Bat()
#
# b1.mammal_info()
# b1.winged_animal_info()
###############################################

### multiple inheritance

# '''
# # ##--Hierchical
# '''
#
#
#
# class CEO:  #################---parent class
#     def __init__(self, name,job,phno):
#         self.name = name
#         self.job = job
#         self.phno = phno
#
# class CTO(CEO):  ############-----parent class
#
#     def geo(self):
#         return f'{self.name}   {self.job} and phno is {self.phno}'
#
#
#
# class MANAGER(CEO):  ###########---------child class
#
#     def america(self):
#         return f'{self.name}  {self.job} and phno is {self.phno}'
#
#
# c1 =CTO ('kumar', 'technicalHead', '9177775555')
# c2=MANAGER('chucha','manager','9755466525')
# print(c1.geo())
# print(c2.america())

##########################################

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         return f'{self.name} says Woof'
#
# class Cat(Animal):
#     def speak(self):
#         return f'{self.name} says Meow'
#
# # Usage
# dog = Dog('Buddy')
# cat = Cat('Whiskers')
# print(dog.speak())
# print(cat.speak())
##########################################


































