######---------NORMAL PROGRAMME using for loop----------#######
##******--- EVEN NO--------
# l=[8,6,9,4]
# even=[]
# for num in l:
#     if(num % 2 ==0):
#         even.append(num)
#
#     else:
#         even.append('ODD')
#
#
# print(even)
'''
###---LIST comprehension
####------Its ONLY applicable for LIST

## ----var=[o/p for var in collection if condition<>]-->>>>SYNTAX
##-----var1[trueSB if condition<> else falseSB for var in collection]
'''


# even=[num if num%2==0 else 'odd' for num in range(1,100)]
# print(even)

#############---- squre of even  from 1 to 10
# squares = []
# for x in range(10):
#     if x % 2 == 0:
#         squares.append(x**2)
# print(squares)
##########--- using list comprehention

# squres=[x**2 for x in range(10) if x%2==0]
# print(squres)

#############----------squre of 1 to 10
# squre1=[]
# for x in range(10):
#     squre1.append(x**2)
##### print(squre1) if I print here inside the loop
# #it will print one value and one value until the loop will
## loop will be going on

# print(squre1)
#############-------list comprehention
# squre2=[x**2 for x in range(10)]
# print(squre2)

##############-------------
### print all element in upper case

words = ["apple", "banana", "cherry", "date", "mango"]
# # capital = []
# # for word in words:
# #     capital.append(word.upper())
# # print(capital)
# ##### list comperehension

capital1=[word.upper() for word in words]
print(capital1)

########--------------
# sentence = "The quick brown fox jumps over the lazy dog"
# chars=[]
# for char in sentence:
#     if char not in 'aeiou'and char.isalpha():
#         chars.append(char.lower())
# print(chars)
#########---------

# sentence = "The quick brown fox jumps over the lazy dog"
# chars1=[char.upper() for char in sentence if char not in 'aeiou' and char.isalpha()]
# print(chars1)

####################-----------------
# c =0  ##--> increment 0,1,2,3,4,5,6,7,8
#
# l =[]  ##---->>> [[0,1,2]]
#
# for i in range (3):##-->0,1,2
#
#     l2=[]  ##----->>[0,1,2]
#     for j in range (3):##-->0,1,2 | 0,1,2| 0,1,2
#
#         l2.append(c)  ##---->>l2 [0,1,2]
#
#         ##/ print (c, end=' ')
#         c+=1  ###--->>increment  0,1,2 |4,5,6 | 7,8,9
#     l.append(l2)###-->> l2 list store into l list
# print(l[0]) ##-->>[0,1,2]
# print(l[1]) ##-->>[3,4,5]
# print(l[2]) ##-->>[6,7,8]
# ###########################--------------->>>>>>>>>>
# '''
# #########-------SET----->> Its Remove duplicate takes heterogeneous kind data
# '''
#
# set_str={"apple", "banana", "cherry", "date", "mango",'apple',}
# print(set_str)
#
# #####----->>> SET comprehention------->>>
# gt_len={ele for ele in set_str if len(ele)>5}
# print(gt_len)

 ########----->>>> Dictionary comprehention SYNTAX---------->>>

###-->var={key:value for variable in collection if <cond>}

##-->print each word as a key and lenth of each word as value
# given of a given string
# str='Hi chucha welcome to india'
# dict1={ele:len(ele) for ele in str.split() }
# print(dict1)
# ## print each element  starts with h or H
# dict2={ele for ele in str.split() if ele[0] in 'hH'}
# print(dict2)































































































































