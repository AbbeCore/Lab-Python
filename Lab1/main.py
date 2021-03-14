x = 4
y = '12'
z = x + int(y)
print(z)  # 16

z1 = y + str(x)
print(z1)  # 124

print(int(3.2))  # 3
print(float('3.2'))  # 3.2
print(int(float('3.2')))  # 3

e = float('3.8e3')  # 3.8 * 10^3
print(e)  # 3800.0

print(float('3.2e4'))  # 32000.0
print(float('3.2e-4'))  # 0.00032


print(1, 'ahmed', 2, 'ali', sep='*', end='\t')
print(3, 'ali')  # 1*ahmed*2*ali	3 ali

print(1, 2, 3, 4, sep='*', end='@')  # 1*2*3*4@

print('\n')
print('I"m')  # I"m
print('I', 'm', sep='"')  # I"m
print('I', 'm', sep='\'')  # I'm

print('\n')
print('\t\tTitle\nThis is python code !')
#		Title
# This is python code !
print('\n')
print('No.\t|\tName')
print('1\t|\tAli')
print('2\t|\tOmar')
# No.	|	Name
# 1	|	Ali
# 2	|	Omar
print('\n')
print('No.\t|\tName\n1\t|\tAli\n2\t|\tOmar')
# No.	|	Name
# 1	|	Ali
# 2	|	Omar
