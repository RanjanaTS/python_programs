s={1,2,3,3,4,5,4}
o={6,4,4,5,7,8,9}
print("s union o : ", s.union(o))
print("o union s : ", o.union(s))
print("s intersection o : ", s.intersection(o))
print("0 intersection s: ", o.intersection(s))
print("s-o difference : ", s.difference(o)) 
print("o-s difference : ", o.difference(s)) 
print("s-o symmetric_difference : ", s.symmetric_difference(o))
print("o-s symmetric_difference : ", o.symmetric_difference(s))
