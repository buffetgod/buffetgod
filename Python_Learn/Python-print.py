a='xujianwei'
b=12.123456789
c=9
##  %输出
print('my name is %s and my age is %d'%(a,b)) 
print('%.1f'%b)
print('%o'%c)
##  .format输出
print('{},{}'.format(a,b))
print('{},{}'.format(b,a))
##  f'{}'输出
print(f'{a},{b}')
## 转义字符
print('we\'re friend')
print('we\\er')
print('hellow\tworld')
print('\"hellow world\"')
##运算符
print(10+10)
print(10-5)
print(10*2)
print(10/2)
print(10%2)  #取余数
print(10//3) #整除
print(2**3)  #次方
