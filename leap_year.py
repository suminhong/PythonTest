year = int(input("년도를 입력하시오 : "))

if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print(year, "년은 윤년입니다")
        else :
            print(year, "년은 평년입니다")
    else :
        print(year, "년은 윤년입니다")
else :
    print(year, "년은 평년입니다")