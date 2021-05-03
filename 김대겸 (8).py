# # 8번_B735042_김대겸

# main()함수 선언
def main():
    lst = [20, 60, 40, 10, 50]
    print(lst)
    print(mySort(lst))

# getMax()함수 선언 (정수 리스트에서 가장 큰 원소와 그 원소를 제외한 리스트를 반환하는 함수)
def getMax(inlist):
    m = max(inlist)
    inlist.remove(m)
    return m, inlist 

# mySort()함수 선언 (정수 리스트를 받아서 리스트를 정렬하여 반환하는 함수)
def mySort(inlist):
    sortList = []
    for i in range(len(inlist)):
        a, b = getMax(inlist)
        sortList.append(a)
    return sortList[::-1]

# main()함수 호출
main()
