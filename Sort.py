import operator
d={1:2,3:4,4:3,2:1,0:0}
print('orginal dictionary:',d)
sorted_d=sorted(d.items(),key=operator.itemgetter(0))
print('dictionary in ascending order by value:',sorted_d)
sorted_d=sorted(d.items(),key=operator.itemgetter(0),reverse=True)
print('dictionary in  descending order by value:',sorted_d)
