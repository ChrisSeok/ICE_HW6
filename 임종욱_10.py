# 10번 C111152 임종욱

#전화번호부 함수

book = []
name = []
num = []
i = 0             #book의 길이
while True:
    name += input("이름? ")
    if i == len(name) : # 엔터키 입력시 입력모드 종료
        print()
        break
    num += input('전화번호? ')
    i += 1
#리스트 함축으로 [이름,번호]를 저장
book = [[name[x],num[x]]for x in range(i)]

print('전화번호책 :',book,'\n')
    
while True:
    man = input('전화번호 찾고싶은사람의 이름을 입력하세요? ')
    if man == '': #엔터키 입력시 종료
        break
    elif man not in name: #등록되지 않은 사용자의 경우
        print(man,'는 등록되지 않았습니다')
    else:
        for x in range(i): 
            if man == name[x]:
                print(man,'의 전화번호는',num[x])
                break