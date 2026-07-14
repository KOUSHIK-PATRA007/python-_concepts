import re
# res1=re.findall(r'Welcome',"welcome")
# print(res1)
# res2=re.findall(r'theory','the ttheoryy of relativity')
# print(res2)
# res3=re.findall(r'\d{3}',"My age is 544 755")
# print(res3)
# res4=re.findall(r'\w{3}',"My age is_ 5445")
# print(res4)
# res5=re.findall(r'\s{2}',"My age is_  5445")
# print(res5)
# res6=re.findall(r'\D{2}',"My age is_  5445")
# print(res6)
# res7=re.findall(r'\w{2}',"My age is_  5445")
# print(res7)
# res8=re.findall(r'aeiou','An aeiou Apple a day keeps no one away')
# print(res8)
#
# # Character Set
# res9=re.findall(r'[5-9]{3}',"My age is 566 955")
# print(res9)
# res10=re.findall(r'[aeiou]','An aeiou Apple a day keeps no one away')
# print(res10)
#
# res11=re.findall(r'col[ou]r',"The color of my house is white")
# print(res11)
# res12=re.findall(r'sep[ea]rate','We are going seperate ways')
# print(res12)
# res13=re.findall(r'[Ss]mith',"Smith and smith are enemies")
# print(res13)
# res14=re.findall(r'[Oo]rgani[zs]ation',"organization")
# print(res14)
#
# # Meta Character "+" [Matches 1 or more occurances of the pattern]
# res15=re.findall(r'[Oo]+rgani[zs]ation',"oooooorganization")
# print(res15)
# res16=re.findall(r'an+a',"aa")
# print(res16)

# "?" [matches 0 time means blank or 1 time occurance of the pattern]

# res17=re.findall(r'an?a',"aa")
# print(res17) ##-->output--> ['aa']
#
# res17=re.findall(r'an?a',"ana")
# print(res17) ##-->output--> ['ana']
#
# res17=re.findall(r'an?a',"annnna")
# print(res17) ##-->output--> []

# "*" [Matches 0 time or Infinite time Occurances of the pattern]
#
# res18=re.findall(r'an*a',"aa")
# print(res18)##-->output-->['aa']
#
# res18=re.findall(r'an*a',"annnnnnna")
# print(res18)##-->output-->['annnnnnna']

#################################----------------------->>>>>>>>>>

'''
findall()--> use 'Returning a list containing every occurrence'
'''
import re
# txt='Returning a list containing every occurrence'
# x=re.findall('in',txt)
# ##--findall takes input as string and return always in the form of list
# print(x)##-- return ['in', 'in', 'in'] because in three times occuring
#
# txt='Returning a list containing every occurrence'
# y=re.findall('iik',txt)
# ##--findall takes input as string and return always in the form of list
# print(y)##-- output-> [] because in three times occuring

# txt='Returning a list containing every occurrence'
# z=re.findall('every',txt)
# ##--findall takes input as string and return always in the form of list
# print(z)##-- output-> ['every'] because in three times occuring
'''
# (\d)--> use Returns a match where the
#  string contains digits (numbers from 0-9)
'''
# txt1='my age is 456'
# f=re.findall(r'\d',txt1)
# print(f)##-->output ['4', '5', '6']

# txt1='my age is 456'
# f=re.findall(r'\d{1}',txt1)
# print(f)##--->output ['4', '5', '6']

# txt1='my age is 456'
# f=re.findall(r'\d{2}',txt1)
# print(f)##--->output ['45']
#
# txt1='my age is 456'
# f=re.findall(r'\d{3}',txt1)
# print(f)##--->output ['456']
#
# txt1='my age is 456'
# f=re.findall(r'\d{4}',txt1)
# print(f)##--->output []

# txt = "my age is 456"
# #Check if "aga" is in the string:
# x = re.findall("aga", txt)
# print(x)
# if (x):
#   print("Yes, there is at least one match!")
# else:
#   print("No match")
#######################################----------
'''(\w)--small w--> use for Returns a match where the string contains 
 any word characters (characters from a to Z, digits from 0-9, 
and the underscore _ character)
'''
# f=re.findall('\w','my age is 456')
# print(f)##--> SyntaxWarning: invalid escape sequence cause (r'\w','my age is

# f=re.findall(r'\w','my age is 456')
# print(f)##-->--->output ['m', 'y', 'a', 'g', 'e', 'i', 's', '4', '5', '6']
#
# f=re.findall(r'\w{1}','my age is 456')
# print(f)##-->--->output ['m', 'y', 'a', 'g', 'e', 'i', 's', '4', '5', '6']

# f=re.findall(r'\w{2}','my age is 456')
# print(f)##-->--->output ['my', 'ag', 'is', '45']

# f=re.findall(r'\w{3}','my age is 456')
# print(f)##-->--->output ['age', '456']
#
# txt3='Retu_rns a matc_h where the stri_ng conta_ins 5699'
# f=re.findall(r'\w{5}',txt3)
# print(f)##-->--->output ['Retu_', 'matc_', 'where', 'stri_', 'conta']
#
'''
(\W)--caps W--> use to Return a match at every NON word character
 special character 
(characters NOT between a and Z. Like "!", "?" white-space etc.)
'''

# txt4='Retu_rns a matc_h whe*re the$ stri_ng conta_ins 5699'
# x = re.findall("\W", txt4)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")
# ##-->--->output [' ', ' ', ' ', '*', ' ', '$', ' ', ' ', ' ']
# ##------------>Yes, there is at least one match!

'''
(\D)--use to 
#Return a match at every no-digit character:
'''
#
# txt5='my age is 456 phn 975588444'
# x = re.findall(r"\D", txt5)
# print(x)
# ##-->output-->only charecters
# #['m', 'y', ' ', 'a', 'g', 'e', ' ', 'i', 's', ' ', ' ', 'p', 'h', 'n', ' ']
#
# txt5='my age is 456 phn 975588444'
# x = re.findall(r"\D{2}", txt5)
# print(x)
# ##-->output-->only charecters
# ##-->['my', ' a', 'ge', ' i', 's ', ' p', 'hn']

# txt5='my age is 456 phn 975588444'
# x = re.findall(r"\D{3}", txt5)
# print(x)
# ##--> three charecters including special charecter
# ##-->output-->only charecters-->>['my ', 'age', ' is', ' ph']

'''
(\s)-->#Return every white-space character:
'''
#
# txt6='my age is 456 phn 97 558 844 4'
# x = re.findall(r"\s", txt6)
# print(x)
# ##-->output-->[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
#
# txt7='  my  age  is'
# x = re.findall(r"\s{2}", txt7)
# print(x)
# ##-->output--> ['  ', '  ', '  ']

########################--------------->>>>>>>>>>>>>>>>>
# '''
# Find all lower case characters alphabetically between "a" and "m":
# using -->[]
# '''
# t1 = "The rain in Spain"
# x = re.findall(r"[a-m]", t1)
# print(x)
#
# '''
# #Search for a sequence that starts with "he"
#  followed by two (any) characters, and an "o":
# '''
#
# t2 = "hello planet"
# x = re.findall(r"he..o", t2)
# print(x)
#
# '''
# #Check if the string starts with 'hello':
# '''
# t3 = "hello planet"
# x = re.findall(r"^hello", t3)
# print(x)
#
# '''
# #Check if the string starts with 'hello' using search:
# '''
# t4 = "hello planet"
# x = re.search(r"^hello", t4)
# print(x)## output--> <re.Match object; span=(0, 5), match='hello'>
#
# '''
#Check if the string starts with 'hello' end with planet:
# '''
#
# t3 = "hello planet"
# x = re.findall(r"^hello planet$", t3)
# print(x)


























