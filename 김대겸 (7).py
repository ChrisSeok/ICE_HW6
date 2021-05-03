# 7번_B735042_김대겸

# main()함수 선언
def main():
    lst = [20, 60, 40, 10, 50]
    m, rlst = getMax(lst)
    print(m)
    print(rlst)

# getMax()함수 선언 (정수 리스트에서 가장 큰 원소와 그 원소를 제외한 리스트를 반환하는 함수)
def getMax(inlist):
    m = max(inlist)
    inlist.remove(m)
    return m, inlist 

# main()함수 호출
main()

    