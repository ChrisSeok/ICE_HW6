# 4번_B735042_김대겸

# main()함수 선언.
def main():
    lst = [20, 60, 40, 10, 50]
    print(reverseList3(lst))
    print(lst)

# reverseList3(ex_list) 선언. (함수를 수행하면 lst리스트는 변화한다.)
def reverseList3(ex_list):
    ex_list.remove(max(ex_list))
    rev_list = ex_list[::-1]
    return rev_list

# main()함수 호출.
main()