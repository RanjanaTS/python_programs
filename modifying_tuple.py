t=(1,9,3,4,0,7)
print("original tuple:", t)
t=t[:1]+(2,)+t[2:]
t=t[:4]+(5,)+t[5:]
t=t[:5]+(6,)+t[6:]
print("modified tuple:",t)
t=t[:6]+(7,)
print("modified tuple:", t)
t=(0,)+t[0:]
print("modified tuple:", t)

'''
output : 

original tuple: (1, 9, 3, 4, 0, 7)
modified tuple: (1, 2, 3, 4, 5, 6)
modified tuple: (1, 2, 3, 4, 5, 6, 7)
modified tuple: (0, 1, 2, 3, 4, 5, 6, 7)

'''