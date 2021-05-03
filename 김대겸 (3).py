#3번_B735042_김대겸

# main()함수 선언.
def main():
    lst = [20, 60, 40, 10, 50]
    print(reverseList2(lst))
    print(lst)

# reverseList2(ex_list) 선언. (함수를 수행해도 lst리스트는 변화하지 않는다.)
def reverseList2(ex_list):
    # temp에 ex_list를 깊게 복사하여 사용.
    temp = ex_list[:]
    temp.remove(max(temp))
    rev_list = temp[::-1]
    return rev_list

# main()함수 호출.
main()