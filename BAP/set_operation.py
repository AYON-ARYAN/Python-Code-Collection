# myset =set()
# myset.add(1)#for adding elements
# print(myset)
# myset.remove(1)#.remove for removing elements
# print(myset)#it doesnt take duplicate elements
# nlist={1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,11,12,}
# print(set(nlist))

myset=set()
myset.add(1)
myset.add(2)
myset.add(3)
myset.add(4)
myset.add(5)
my2set=set()
my2set.add(4)
my2set.add(5)
my2set.add(6)
my2set.add(7)
my2set.add(8)
setl=set()
setl=myset.union(my2set)
print(setl)#union
setl=myset.intersection(my2set)
print(setl)#intersection
setl=myset.difference(my2set)
print(setl)#seta-setb
setl=myset.symmetric_difference(my2set)
print(setl)
