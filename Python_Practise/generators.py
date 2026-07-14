# ### generator are use to return multiple statement from
# #### a func by using yeild keyword
#  ##---- yeild is nothing but return keyword
###-- return will exit or terminate the func
###---- yield will return multiple statements in a func controler comes
##--to yield it will pause for a few seconds it will generate and execute the statement
##-- go to next yield again pause for few seconds goes on same process
#
# ###-------------------1 NO
# def go():
#     yield "go there "
#     yield "go there fst "
#     yield "go there fst run "
# G=go()
# for ele in G: ###---- first way to print
#     print(ele)
#
# ################-------------2 NO
# def go():
#     yield "go there "
#     yield "go there fst "
#     yield "go there fst run "
# G=go()
# print(list(G)) ###---- 2nd way to print
#
# ##################-------------- 3 NO
# def go():
#     yield "go there "
#     yield "go there fst "
#     yield "go there fst run "
# G=go()
# print(set(G)) ##---- 3rd way  print
#
# ###########################------------ 4 NO
# def go():
#     yield "go there "
#     yield "go there fst "
#     yield "go there fst run "
# G=go()
# # #####----------- 4th way to print
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# ####################-------------------------- 5 NO calculator
# def sumasion(a,b):
#     yield a+b
#     yield a-b
#     yield a*b
#     yield a/b
#
# S=sumasion(3,2)
## print(S) #####------StopIteration error
# for ele in S:
#     print(ele)

# print(list(S))

# print(next(S))
# print(next(S))
# print(next(S))
# print(next(S))
##################-------------- 6 NO





















