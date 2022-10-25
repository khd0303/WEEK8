import  sys
#1
'''

fname = input('입력한 파일의 이름: ')
try :
    f = open(fname, 'r', encoding='UTF8')
except IOError:
    print('Could not read file:', fname)
    sys.exit()
except :
    print('Unexpected error:', sys.exc_info()[0])
    sys.exit()
n = 0


newname = fname + '_upper.txt'
fnew = open(newname,'wt')
l = f.readline()

while l :
    print('{}'.format(l.upper()), end='')
    fnew.write(l.upper())
    l = f.readline()
    n += 1

fnew.close()
f.close()
'''
#2

fname = input('입력한 파일의 이름: ')
try :
    f = open(fname, 'r', encoding='UTF8')
except IOError:
    print('Could not read file:', fname)
    sys.exit()
except :
    print('Unexpected error:', sys.exc_info()[0])
    sys.exit()

lines = f.readlines()
l = f.readline()
lines.reverse()
for l in lines:
    #l = l.strip()
    print('{}'.format(l),end = '')

f.close()
