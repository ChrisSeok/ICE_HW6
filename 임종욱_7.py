#7번  C111152 임종욱

def getMax(lst):
    # 가장 큰 원소의 위치
    i =lst.index((max(lst)))
    #pop메소드로 가장큰 원소를 반환하고 삭제함
    M = lst.pop(i)
    return M,lst
    

def main():
    lst = [20, 60, 40, 10, 50]
    m, rlst = getMax(lst)
    print(m)
    print(rlst)

main()
