x = int(input('x = '))
if x>1:
    y = 3*x -5
elif(x>=-1 and x<=1):
    y = x + 2
else:
    y = 5*x +3

print('当x等于%d时,y等于%d'%(x,y))