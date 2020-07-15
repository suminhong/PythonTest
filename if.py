x = int(input("숫자를 입력하세요(0~20) : "))
if x >= 10 :
    print('%d는 10 이상입니다' %x)
elif x >= 5 :
    print('%d는 5 이상입니다' %x)
else :
    print('%d는 5보다 작습니다' %x)

if x in (1, 3, 5, 7, 9, 11, 13, 15, 17, 19) :
    print('%d는 홀수입니다' %x)
else :
    print("%d는 짝수입니다" %x)

if type(x) is int :
    print('%d는 정수입니다' %x)

if x > 10 and x != 15 :
    print('%d는 10보다 크지만 15는 아닙니다')


arr = [1, 2, 3, 4, 5]
n = int(input("\n찾을 숫자 입력 :"))
if n in arr :
    print('arr :', arr, '찾는 숫자가 존재합니다 :', n)
else :
    print('arr :', arr, '찾는 숫자가 존재하지 않습니다 :', n)


#중첩 if문
num = int(input("\n숫자 입력 : "))
if num % 3 == 0 :
    if num % 2 == 0 :
        print(num, "은 3의 배수이면서 짝수입니다")
    else :
        print(num, "은 3의 배수입니다")
else :
    print(num, "은 3의 배수도 짝수도 아닙니다")