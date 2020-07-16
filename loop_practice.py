#1. 구구단을 출력해라
for x in range(1, 10) :
    print(x, "단")
    for y in range(1, 10) :
        print (x, "*", y, "=", x*y)
    print('\n')

#2. 1 ~ 100 합 구하라
sum = 0
for x in range(1, 101) :
    sum += x
print("1부터 100까지 합은", sum)

#3. 1부터 1씩 증가하는 값에 대해 누적합을 구할 때 10000보다 큰
#누적합 값에 대해 마지막에 더해진 값인 얼마인지 구하라
sum = 0
x = 1
while True :
    sum += x
    if sum >= 10000 :
        print("누적합 10000이상에 마지막으로 더해진 값 :", x)
        break
    x += 1

#4. 1부터 100 사이의 소수 출력하고 개수 구하라
count = 0
print("1부터 100까지의 소수는")
for x in range(1, 100) :
    x += 1
    #print("\nx : ", x)
    for i in range(int(x/2), 0, -1) :
        #print(i, end=' ')
        if i < 2 :
            print(x, end=', ')
            count += 1
            break
        if x % i == 0 :
            break

        
print("총 개수는", count, "개")
