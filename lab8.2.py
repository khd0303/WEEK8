#1

'''
try:
    10*(30/0)


except ZeroDivisionError:
    print('0으로 나누기 시도')
'''

#2
try:
    x = int(input('정수 x를 입력하시오:  '))
except ValueError:
    print('입력값이 정수가 아님')

#3

import sys

try:
    f = open('myfile.txt')
    s = f.readline()

except FileNotFoundError:
    print('myfile.txt란 파일은 없음')
