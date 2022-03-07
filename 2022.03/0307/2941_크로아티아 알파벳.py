s = input()

#ddz=z= 3 d dz= z=
#nljj 3 n lj j
#c=c= 2 c= c=
#dz=ak 3 dz= a k

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro:
    s = s.replace(i, '*')
print(len(s))