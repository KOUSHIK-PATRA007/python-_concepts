

## f=open('sourcefile.txt', 'w')###--write argument must be in string form
## f.write('Hello World \nthank you\n')
##f.writelines('byeeee')### it will overwrite the exsisting content or showing new implementation
## f.close()

# f = open('sourcefile.txt', 'r')###------ read argumnts
# print(f.read())###----it will read all the element present in file
# f.close()

# f = open('sourcefile.txt', 'r')####-----read argument
# print(f.readline()) ##--it will read first ele or first line
# f.close()
#
# f=open('sourcefile.txt', 'w')########----------write in file
# f.write('{Hello World \nthank you\n}')
# f.writelines('{byeeee}')### it will overwrite the exsisting content or showing new implementation
# f.close()

# f = open('sourcefile.txt', 'r')####----- read file
# print(f.readlines()) ##--it will give you output in list format
# f.close()


# f=open('sourcefile.txt', 'w')###--for write (argument must be in string form)
# f.write('Hello World \nthank you\n')
# f.writelines('byeeee !')### it will overwrite the exsisting content or showing new implementation
# f.close()
#
# f=open('sourcefile.txt', 'a')###---append using (a) writing data into existing file
# f.write('now you see me')
# # f.writelines('')### it will overwrite the exsisting content or showing new implementation
# f.close()
#
# f=open('sourcefile.txt', 'r')##---read file
# print(f.read())
# f.close()

########---------ANOTHER WAY OF FILE HANDLING

with open('anotherfile.txt', 'w') as f:####-------no.1 write
    f.write('hello world\n')
    f.writelines('now you see me\n')

with open('anotherfile.txt', 'r') as f:###----read all content
    print(f.read())

with open('anotherfile.txt', 'r') as f:###--- read fst line
    print(f.readline())

with open('anotherfile.txt', 'r') as f:###--read in a list form
    print(f.readlines())

##-- add more ele
with open('anotherfile.txt', 'a') as f:
    f.write('byyeeee')

with open('anotherfile.txt', 'r') as f:
    print(f.read())








































