#4번 C111152 임종욱

def reverseList3(lst):
    lst.remove(max(lst))
    lst.reverse()
    return lst
    
def main():
 lst = [20, 60, 40, 10, 50]
 print(reverseList3(lst))
 print(lst)
 
main()