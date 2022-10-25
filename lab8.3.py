#1

a = [1,2,3,4,5]
'''
num = int(input('a의 요소를 하나 선택하시오 : '))
if num == 1:
    print('{}은(는) 첫번째 요소입니다'.format(num))
if num == 2:
    print('{}은(는) 두번째 요소입니다'.format(num))
if num == 3:
    print('{}은(는) 세번째 요소입니다'.format(num))
if num == 4:
    print('{}은(는) 네번째 요소입니다'.format(num))
if num == 5:
    print('{}은(는) 다섯번째 요소입니다'.format(num))
'''

#2

try:
    num = int(input('a의 요소를 하나 선택하시오 : '))

except ValueError:
    print('오류 : 입력값이 정수가 아님')