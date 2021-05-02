#9번, B835193 석채원
slist = []
def sortList(list):
    global slist
    min = list[0]
    for i in list:
        if(min>i):
            min = i
    slist.append(min)
    list.remove(min)
    
    if(list):
        sortList(list)
        
    return slist

def main():
 lst = [20, 60, 40, 10, 50]
 print(lst)
 print(sortList(lst))
main()
