#10번, B835193 석채원
phonebook = []
def Write():
    while 1:
        name = input("이름?")
        if (name==''):
            break
        else:
            phoneNum = input("전화번호?")
        phonebook.append([name,phoneNum])
    return
def Search():
    while 1:
        searchName = input("전화번호 찾고싶은사람의 이름을 입력하세요?")
        if(searchName==''):
            break;
        else:
            phnum=''
            for name in phonebook:
                if(name[0]==searchName):
                    phnum = name[1]
                    break
            
            if(phnum==''):
                print("해당 사람의 전화번호가 없습니다.")
            else:
                print(searchName,"의 전화번호는",phnum)
        
    return
        
def main():
    Write()
    print("전화번호책:",phonebook)
    Search()
main()   