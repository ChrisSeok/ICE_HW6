# 10번_B735042_김대겸

# 빈 전화번호책 리스트(phoneBook)
phoneBook = []
i = 0
# 입력모드 시작
while True:
    name = input("이름? ")
    if name == '': # 사용자가 엔터만 누르면 입력모드 종료
        break
    phoneBook.append([])
    phoneBook[i].append(name)
    phoneNum = input("전화번호? ")
    phoneBook[i].append(phoneNum)
    i += 1
print()
# 전화번호책 출력    
print("전화번호책 : ", phoneBook)
print()
# 검색모드
while True:
    wantName = input("전화번호 찾고싶은 사람의 이름을 입력하세요? ")
    if wantName == '': # 사용자가 엔터만 누르면 검색모드 종료.
        break
    finding = 0   # 사용자가 찾고싶은 이름을 구별해줄 변수finding에 0을 저장.
    for i in range(len(phoneBook)):
        if wantName in phoneBook[i]: # 찾고싶은 이름이 전화번호책에 있다면,
            if wantName == phoneBook[i][0]:
                finding += 1 # 찾고싶은 이름을 찾으면 finding에 1을 더하여 저장
                print(wantName, "의 전화번호는 ", phoneBook[i][1], "입니다.")   
        else: # 찾고싶은 이름이 전화번호책에 없다면.
            finding == 0 # 찾고싶은 이름을 찾지못하면 finding은 0
    if finding == 0: # finding == 0이면 등록되지 않은 이름.
        print(wantName, "는 등록되지 않았습니다.")
          
    
