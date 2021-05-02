#2번  C111152 임종욱

def reverseList(lst):
    ls = lst.copy()
    ls.reverse()
    return ls
    
def main():
 lst = [20, 60, 40, 10, 50]
 print(reverseList(lst))
 print(lst)
 
main()