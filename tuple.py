'''
리스트는 [], 튜플은 ()
리스트는 그 값의 생성, 삭제, 수정 가능하지만 튜플은 못바꿈
t1=(1,)처럼 1개의 요소만을 가질 땐 요소 뒤에 , 반드시 붙여줘야됨
t2=1,2,3 처럼 괄호 생략 가능
'''
#기본 사용법
#변수명 = (v1, v2 ...)

tup=(1,2,3,1,2)
print(tup.count(2))
print(tup.index(2))

numbers=(10,20,30,40,50,60,70)
num1 = numbers[2]
num2 = numbers[3]
print(num1, num2)

menu=(('칼국수', 6000), ('비빔밥',5500),('돼지국밥', 7000))
for x in range(3):
    print(menu[x][0], '- {:,}원' .format(menu[x][1]))