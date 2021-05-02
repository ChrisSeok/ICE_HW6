#8번 C111152 임종욱

# 리스트의 가장큰원소를 구하고 그것을 제외한 리스트를 만드는 함수
def getMax(lst):
    # 가장 큰 원소의 위치
    i =lst.index((max(lst)))
    #pop메소드로 가장큰 원소를 반환하고 삭제함
    M = lst.pop(i)
    return M,lst

#리스트를 크기순으로 나열하는 함수, getMax이용
def mySort(lst):
    M_lst =[]
    
    while lst != []:
        m,lst = getMax(lst)
        M_lst = [m] +M_lst
    return M_lst

def main():
    lst = [20, 60, 40, 10, 50]
    print(lst)
    print(mySort(lst))

main()
