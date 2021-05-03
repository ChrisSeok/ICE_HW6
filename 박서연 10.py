#10번문제 / C111061 박서연

def collection():
    global allContact
    allContact = []
    while True:
        name = str(input("이름? "))
        if name == "":
            break
        phoneNumber = str(input("전화번호? "))
        contact = [name, phoneNumber]
        allContact.append(contact)
    print()
    return allContact

def search(allContact):
    print()
    while True:
        check = 'a'
        find = str(input("전화번호 찾고싶은사람의 이름을 입력하세요? "))
        if find == "":
            break
        
        for i in range(len(allContact)):
            if find == allContact[i][0]:
                print(find, "의 전화번호는", allContact[i][1], "입니다.")
                check = 'b'
                break
        
            else:
                i = i + 1
                
        if check == 'a':
            print(find, "는 등록되지 않았습니다")
                
        
def main():
    print("전화번호책 : ", collection())
    search(allContact)
    
main()

        

    
