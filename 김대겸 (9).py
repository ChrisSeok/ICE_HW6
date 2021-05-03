# 9번_B735042_김대겸

# main()함수 선언
def main():
    lst = [20, 60, 40, 10, 50]
    print(lst)
    print(sortList(lst))

# sortList()함수 선언 (정수 리스트를 받아서 리스트를 정렬하여 반환하는 재귀함수
def sortList(inlist):
    if len(inlist) <= 1:
        return inlist
    else:
        return sortList(([x for x in inlist[1:] if x <= inlist[0]])) +\
               ([inlist[0]]) +\
               (sortList([x for x in inlist[1:] if x > inlist[0]]))

# main()함수 호출
main()

