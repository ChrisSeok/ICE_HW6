#3번문제 / C111061 박서연  

def reverseList2(n):
    lst2 = list(n)
    lst2.remove(max(lst2))
    lst2.reverse()
    return lst2
    

def main():
    lst = [20, 60, 40, 10, 50]
    print(reverseList2(lst))
    print(lst)
    
    
main()