'''
기본 사용법
변수명 = []
변수명 = [v1, v2, v3 ...]

list 클래스의 생성자 이용
list1 = list()              -> []
list2 = list("Hello")       -> ['H', 'e', 'l', 'l', 'o']
list3 = list(range(0,5))    -> [0, 1, 2, 3, 4]
'''
list1 = list()
list2 = list("Hello")
list3 = list(range(0,5))

print(list1, list2, list3, sep=' ')

#list 연산자
a=[1,2,3]
b=[4,5]
c=['hello']

print(len(a))       #3
print(a+b)          #[1,2,3,4,5]
print(a*3)          #[1,2,3,1,2,3,1,2,3]
print(c*3)          #['hello','hello','hello']
print(3 in a)       #True
print(3 not in a)   #False
print(a[1])         #2(인덱스->0부터 시작)
print(min(a))       #1(최솟값)
print(max(a))       #3(최댓값)
for x in a:print(x, end=' ')    #for문으로 반복

print('\n')
lst=[1,2,3,4,5,6,7,8,9,10]
print("lst\t\t->\t", lst)
print("lst[0]\t\t->\t", lst[0])
print("lst[1]\t\t->\t", lst[1])
print("lst[-1]\t\t->\t", lst[-1])
print("lst[-3]\t\t->\t", lst[-3])
print("lst[0:2]\t->\t", lst[0:2])
print("lst[-3:-1]\t->\t", lst[-3:-1])
print("lst[-2:]\t->\t", lst[-2:])

print('\n')
#리스트 함수
l = [1,2,3]
print(l)
l.append('a')           #뒤에 'a' 추가
print(l)
l.append([4, 'b'])      #뒤에 [4, 'b'] 추가
print(l)
l.extend([4, 'b'])      #뒤에 4, 'b' 추가
print(l)
l.insert(1, 'insert1')  #index 1번자리에 insert1 추가
print(l)
l.pop()                 #맨 마지막 삭제
print(l)
l.pop(0)                #index 0번 삭제
print(l)
l.remove(2)             #value가 2인 값 삭제
print(l)
print(l.count(3))       #value가 3인게 몇개 있느냐
print(l.index(3))       #value가 3인놈의 index가 몇번이냐
l.reverse()             #리스트 뒤집기
print(l)
l.clear()               #리스트 전부 삭제
print(l)

#리스트 정렬 : 숫자 문자 혼합은 사용 못함
print('\n')
l2 = [1,3,2]
print(l2)
l2.sort()               #리스트 정렬
print(l2)
l2.sort(reverse=True)   #리스트 역순 정렬
print(l2)


#copy 비교
#shallow copy
#두 리스트가 같은 걸 가리키기 때문에 하나만 수정해도 나머지에 변경사항 적용
print('\nshallow copy')
lst1 = [1,3,2]
lst2 = lst1
print("lst1 =", lst1, "lst2 =", lst2)
lst2.append(5)
print("lst1 =", lst1, "lst2 =", lst2)

#deep copy
#두개가 별도의 기억 공간을 가짐
print("deep copy")
lst1 = [1,3,2]
lst2 = list(lst1)
print("lst1 =", lst1, "lst2 =", lst2)
lst2.append(5)
print("lst1 =", lst1, "lst2 =", lst2)

print('\n')
#연습문제
#1. numbers=[10,20,30,40,50,60,70]
#위 리스트의 모든 값을 더한 결과 출력
numbers=[10,20,30,40,50,60,70]
sum = 0
for x in numbers:
    sum += x
print('1번 문제 :', sum)

#2. lst_sec=[['홍길동','남',36],['김수양','여',32],['박담소','남',28]]
#위의 2차 리스트 자료를 다음과 같은 형식으로 출력하시오
#   이름 : 홍길동
#   성별 : 남
#   나이 : 36
print('\n2번 문제')
lst_sec=[['홍길동','남',36],['김수양','여',32],['박담소','남',28]]
for x in range(3):
    print('이름 :', lst_sec[x][0])
    print('성별 :', lst_sec[x][1])
    print('나이 :', lst_sec[x][2])
    print('\n')

#추가 문제
#친구 이름 관리하는 코드 만들기
print('\n\n친구 관리 프로그램')
friend=[]
while(1):
    print('-'*20)
    print('1. 친구 리스트 출력')
    print('2. 친구 추가')
    print('3. 친구 삭제')
    print('4. 이름 변경')
    print('0. 종료')
    x = int(input('메뉴를 선택하시오 :'))
    if x == 0:
        print('-'*20)
        break
    elif x ==1:
        if len(friend) == 0 :
            print('친구가 없습니다')
            continue
        else:
            for i in friend:
                print(i, end=' ')
            print('\n')
    elif x==2:
        f=input('친구 이름을 입력하세요:')
        friend.append(f)
    elif x==3:
        f=input('친구 이름을 입력하세요:')
        friend.remove(f)
    elif x==4:
        f=input('친구 이름을 입력하세요:')
        idx=friend.index(f)
        c=input("바뀔 이름을 입력하세요:")
        friend.pop(idx)
        friend.insert(idx, c)