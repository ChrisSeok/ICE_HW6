#9번 임종욱 C111152

def sortList(lst):
    r_lst = []
    if lst == []:
        return lst
    #가장 작은 원소 추출
    m = lst.pop(lst.index(min(lst)))
    # 작은 원소순으로 정렬
    r_lst = [m] + sortList(lst)
    return r_lst
    
def main():
    lst = [20, 60, 40, 10, 50]
    print(lst)
    print(sortList(lst))

main()
