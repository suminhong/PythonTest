n = int(input("다이아몬드의 크기를 입력하세요 : "))
m = int(n/2) + 1
for i in range(1, 2*m):
    if(i<=m):
        for j in range(m-i):
            print(" ", end="")
        for j in range(2*i-1):
            print("*", end="")
        print()
    else:
        for j in range(i-m):
            print(" ", end="")
        for j in range((2*m-i)*2-1):
            print("*", end="")
        print()