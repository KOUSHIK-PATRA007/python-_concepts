from abc import ABC
from logging import exception

##########################----------------------NO.-1
# class Exccept :
#     try: ########-------here we write the excetion
#         print(1/0)
#     except Exception:#####---- here we handel the exception
#         print('exception handeld')
#
#     finally:
# ###---- it will always execute either exception is handled or not
#                 print('we cant devide a number by zero')

# #######################----------------- NO.2
# import sys
# class Exccept :
#     try:
#         print('setoi'/5)
#     except Exception:
#         print('exception handel')
#
#     finally: #####---it will not execute when we use system.exit()
#         sys.exit()
#         print('here we are handeling the exception')
#
# ######################-----------------------NO.3

# import sys
# class Exccept :
#     try:
#         print({1,2,3}+{8,5,9})
#     except Exception:
#         print('handel we cant add two set')
#
#     finally:
#     #####---it will execute print statement then exit from the block
#
#         print('here we are handeling the exception')
#         sys.exit()

#############################--------------------NO.4

#
# class CustomError(Exception):
#     """A simple custom exception."""
#     pass
#
# def divide(a, b):
#     if b == 0:
#         raise CustomError("Cannot devide")
#     return a / b
#
# # Example usage
# try:
#     result = divide(10, 0)
#     print(result)
# except CustomError as e:
#     print(f"An error occurred: {e}")
#
# # try:
# #     result = divide(10, 2)
# #     print(f"Result of division: {result}")
# # except CustomError as e:
# #     print(f"An error occurred: {e}")

#############-----------------------------
####-------------- custom exception-----------#########
class HazamaError(Exception):
    pass
try:
    num=int(input("Enter a number: "))
    if num < 1:
        raise HazamaError
    print('chucha sale')

except Exception as e :
    print(f'valid not{e}')
























