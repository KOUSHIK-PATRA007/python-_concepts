'''
###--- lamda is a keyword it can not be declear as def
##--- but it will act as function so we will call it as anonymous function

###-- A lambda function is a small anonymous function.

##-- A lambda function can take any number of arguments,
#--- but can only have one expression.
##-- The expression is executed and the result is returned:
##----------Syntax:--> lambda arguments : expression
'''

##-- normal func
def add(a,b):
    return a+b
print(add(1,2))
## var=lambda args :expression
## print(var(args))

##-- using lamda func
var=lambda a,b:a+b
print(var(4,5))
##----
var1=lambda a,b,c:a+b+c
print(var1(4,5,6))
##----
var2=lambda num:num**3
print(var2(4))
###-----















































































