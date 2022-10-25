import sys

#1
'''
try:
    f = open('greet.txt','wt')

except PermissionError:
    print('Error: PermissionError[errno 13] Permission denied')

f.write('Hi,everyone.\n')
f.write('welcome to Python\n')

f.close()
'''


#2
'''
#(1)
f = open('number1to10.txt','r')
f1 = open('numberby10.txt','w')

l = f.readline()

while(l):
    l1 = int(l)
    l1 = l1 * 10
    l2 = str(l1)
    f1.write(l2 + '\n')
    l = f.readline()


f.close()
f1.close()

'''

#(2)
'''
f = open('merge.txt','w')
f1 = open('number1to10.txt','r')
f2 = open('numberby10.txt','r')
l = f1.readline()
l1 = f2.readline()
while(l):
    l2 = str(int(l)) +':'+ str(int(l1))
    l2 = str(l2) + '\n'
    f.write(l2)
    l = f1.readline()
    l1 = f2.readline()
f.close()
f1.close()
f2.close()
'''
'''
#3
#(1)


f = open('my_hello.txt','w')

f.write('Hello Python\n')
f.close()
# PermissionError : [Errno13] Permission denied 에러 출현
'''
'''
"#(2)
try:
    f1 = open('my_hello.txt','w')


except PermissionError:
    print('Error: PermissionError[errno 13] Permission denied')
except NameError:
    print('Error : NameError name f1 is not defined')

f1.write('Hello Python nonerror')
f1.close()
'''
#1번에서는 생기지 않았던 NameError가 추가로 생겼는데, NameError가 예외처리로 잡히지를 않는다


'''
#4
#(1)
f = open('hello.txt','r')

l = f.readline()

print('hello.txt파일 : ')
while(l):
    print(l,end='')
    l = f.readline()

f.close()

#(2)
f = open('hello.txt','a+')


f.write('Welcome to Python!')
f.close()

f = open('hello.txt','r')

l = f.readline()

print('hello.txt파일 : ')
while(l):
    print(l,end='')
    l = f.readline()

f.close()
'''

'''
#5
import random

f = open('randiant30.txt','w')

for i in range(30):
    l1 = random.randint(1,10)
    l1 = str(l1) + ' '
    f.write(l1)
f.close()

f1 = open('randiant30.txt','r')

#l = (f1.read())
#print(l)



n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
n7=0
n8=0
n9=0
n10=0
while(l):

    print(l)

    if int(l) == 1:
        n1 +=1
    if int(l) == 2:
        n2 += 1
    if int(l) == 3:
        n3 += 1
    if int(l) == 4:
        n4 += 1
    if int(l) == 5:
        n5 += 1
    if int(l) == 6:
        n6 += 1
    if int(l) == 7:
        n7 += 1
    if int(l) == 8:
        n8 += 1
    if int(l) == 9:
        n9 += 1
    if int(l) == 10:
        n10 += 1

f1.close()
print('1 : {}개'.format(n1))
print('2 : {}개'.format(n2))
print('3 : {}개'.format(n3))
print('4 : {}개'.format(n4))
print('5 : {}개'.format(n5))
print('6 : {}개'.format(n6))
print('7 : {}개'.format(n7))
print('8 : {}개'.format(n8))
print('9 : {}개'.format(n9))
print('10 : {}개'.format(n10))
'''
#5txt파일 생성까지는 되겟지만, 문자열을 정수로 변환켜서 갯수를 세려하니 계속 공백부분이 오류가 생긴다