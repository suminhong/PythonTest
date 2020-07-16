print('=====계정 생성=====')
id = input('ID를 입력하세요 :')
pw = input('비밀번호를 입력하세요 :')
pw2 = input('비밀번호를 한번 더 입력하세요 :')
if pw == pw2 :
    print(id, '님 계정 생성 완료')
else :
    print('계정 생성 실패')