#3번, B835193 석채원
import copy
def reverseList2(list):
    rlist = copy.deepcopy(list)
    big = rlist[0]
    for i in rlist:
        if(i>big):
            big = i
    rlist.remove(big)
    
    rlist.reverse()
    return rlist 
        
def main():
 lst = [20, 60, 40, 10, 50]
 print(reverseList2(lst))
 print(lst)
main()