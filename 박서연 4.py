#4번문제 / C111061 박서연 

def reverseList3(n):
    lst3 = n
    lst3.remove(max(lst3))
    lst3.reverse()
    return lst3
    

def main():
    lst = [20, 60, 40, 10, 50]
    print(reverseList3(lst))
    print(lst)
    

main()