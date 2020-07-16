#1부터 100 사이의 소수 출력하고 개수 구하라
count = 0
print("1부터 100까지의 소수는")
for x in range(1, 100) :
    x += 1
    for i in range(int(x/2), 0, -1) :
        if i < 2 :
            print(x, end=', ')
            count += 1
            break
        if x % i == 0 :
            break       
print("총 개수는", count, "개")