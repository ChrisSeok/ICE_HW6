#3번  C111152 임종욱

def reverseList2(lst):
    ls = lst.copy()
    ls.remove(max(ls))
    return ls

def main():
 lst = [20, 60, 40, 10, 50]
 print(reverseList2(lst))
 print(lst)
 
main()
