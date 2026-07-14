


# x=float(input("Enter a number: "))
# if x%6==0:
#     print("it is divisible by 6")
# else:
#     print("it is NOT divisible by 6")

#
# x=int(input("Enter a number: "))
# if x<0:
#     print("The number is negative")
# else:
#     print("The number is positive")

# x=[1,8,3,0,6,4,5,9,10,25]
# c=[]
# d=[]
# count=0
# while count<len(x):
#
#     if x[count] % 2==0 :
#         c.append(x[count])
#
#     else:
#         d.append(x[count])
#
#
#     count=count+1
# print('even no are =',c)
# print('odd no are =',d)

x=int(input("Enter a number: "))
s=0

while x>0:
    last = x % 10

    s = s + last
    x = x //10

print(s)


