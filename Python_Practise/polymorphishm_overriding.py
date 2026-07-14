
######## IN Polymorphishm there shoulld be a inheritance
#   without inheritance polimorphishm is not possible
# for overwriting or overriding inheritance should be present


class CEO:  #################---parent class
    def __init__(self, name,job,phno):
        self.name = name
        self.job = job
        self.phno = phno

class CTO(CEO):  ############-----parent class

    def geo(self):
        return f'{self.name}   {self.job} and phno is {self.phno}'
    def geo(self):################---overwriting/overloding
        return f"this is overloding"


class MANAGER(CTO):  ###########---------child class
    def geo(self):
        return f'this is a overriding'

    def america(self):
        return f'{self.name}  {self.job} and phno is {self.phno}'


c1 =CTO ('kumar', 'technicalHead', '9177775555')
c2=MANAGER('chucha','manager','9755466525')
print(c1.geo())
print(c2.geo())
print(c2.america())
#
# # ############################################
# class CEO:  #################---parent class
#     def __init__(self, name,job,phno):
#         self.name = name
#         self.job = job
#         self.phno = phno
#
# class CTO(CEO):  ############-----parent class
#
#     # def geo(self):
#     #     return f'{self.name}   {self.job} and phno is {self.phno}'
#     def geo(self):################---overwriting/overloding
#         print(f"this is overloding")
#

# class MANAGER(CTO):  ###########---------child class
#     # def geo(self):
#     #     print(f'this is a overriding')
#
#     def america(self):
#         return f'{self.name}  {self.job} and phno is {self.phno}'
#
#
# c1 =CTO ('kumar', 'technicalHead', '9177775555')
# c2=MANAGER('chucha','manager','9755466525')
# print(c1.geo())
# print(c2.geo())
# print(c2.america())
# c2.geo()
  #### it will check the first geo() method search from down to up
     ############# whichever comes first that will print

######################################----------------





























