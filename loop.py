'''
range() 함수 응용
range(종료값)
range(시작값, 종료값)
range(시작값, 종료값, 증가값)
'''

print('range(10) : ')
for i in range(10) :
    print(i, end=' ')

print('\n\nrange(5, 10) : ')
for i in range(5, 10) :
    print(i, end=' ')

print('\n\nrange(1, 10, 2) : ')
for i in range(1, 10, 2) :
    print(i, end=' ')

print('\n\nrange(1, 10, 1) : ')
for i in range(1, 10, 1) :
    print(i, end=' ')

print('\n\nrange(10, 1, -1) : ')
for i in range(10, 0, -1) :
    print(i, end=' ')


print('\n\n문자열 반복')
for value in 'String' :
    print(value, end=' ')


print('\n\n중첩 for문')
n = 1
for x in range(5) :
    for y in range(3) :
        print(n, end='\t')
        n += 1
    print('\n')


print('\nwhile 반복문')
x = 1
while x < 10 :
    print(x, end=' ')
    x += 1

print('\n\n무한반복과 break')
x = 1
while True :
    print(x, end=' ')
    x += 1
    if x == 10 :
        break

print('\n\ncontinue')
x = 0
while True :
    x += 1
    if x % 2 == 1 :
        continue
    print(x, end=' ')
    if x == 10 :
        break