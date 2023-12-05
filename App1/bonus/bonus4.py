'''
mutability

可以改变，mutable : list, dic, set,bytearray, user-defined classes
不可以通过index access，immutable: integers, floats, strings, tuples,frozensets, bytes
'''

filenames = ["1.Raw Data.txt", "2.Reports.txt","3.Presentations.txt"]

for i in filenames:
    i = i.replace('.','-',1)
    print(i)