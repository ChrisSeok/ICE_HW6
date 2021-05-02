#4번, B835193 석채원
def reverseList3(list):
    big = list[0]
    for i in list:
        if(i>big):
            big = i
    list.remove(big)
    
    list.reverse()
    return list
        
def main():
 lst = [20, 60, 40, 10, 50]
 print(reverseList3(lst))
 print(lst)
main()
