'''
#1

a = [10,20,30]
(a[3])
#IndexError: list index out of range

n = int('20%')
#ValueError: invalid literal for int() with base 10: '20%'


a = 100 + '200'
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

#2

try:
    a = [10, 20, 30]
    a[3]


except Exception as e:
    print(e)


#list index out of range
