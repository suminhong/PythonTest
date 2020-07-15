#1. 정수 : 0 과 음수 , 양수 값을 포함하는 숫자 값
#2. 실수 : 소수점을 사용하는 숫자 값
#3. 문자열 : 따옴표로 묶여 있는 값
#4. 리스트 : 정수 , 실수 및 문자열 등 자료들의 집합(값의 집합)
#5. 튜플 : 정수 , 실수 및 문자열 등 자료들의 집합(값의 집합)
#6. 사전 : 정수 , 실수 , 및 문자열 등 자료들의 집합(키와 값의 쌍)
#7. 부울형(boolean) : True, False

var1, var2, var3 = '1', 1, 1.0
#변수 자료형 확인
print('{}' .format(type(var1)))
print('{}' .format(type(var2)))
print('{}' .format(type(var3)))

#변수 자료형 변환
var1, var2, var3 = int(var1), float(var2), str(var3)
print("변수 자료형 변환")
print('{}' .format(type(var1)))
print('{}' .format(type(var2)))
print('{}' .format(type(var3)))