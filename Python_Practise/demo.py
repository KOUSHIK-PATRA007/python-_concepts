l='helo_world'
print(l[-3])
print("------indexing-----------")
a=10
b=20
c=10
# a(same address) b(diff addreess) c(same address)

print(id(a))
print(id(b))
print(id(c))
print("------fetech address-----------")
# know the datatype

print(type(a))
print(type(l))
D=[1,2,5,6]
E=(1,2,3,5)
R={1,25,86,75,7}
print(R)
print(type(R))
print('-------------')
print(type(D))
print(type(E))

l='HELO_WORLD'
print(l[3])
print(len(l))
print(l[-8])
# lo_
print('------slicing-----')
print(l[2:5:1])

# woe   (slicing)
print(l[5:0:-2])

#it will take start index 0 and last index length of array
# if you dont give any start index or end index
print(l[::2])
print(l[::1])
print(l[:])

# multiplecation
print('hi'*6)

# addition of two string

print('hall'+'hello')
# print('hello'-2)  ////// it will throw error

#formating string for print
a1='boss'
print(f"i am the {a1}")
print("i am the",a1)



