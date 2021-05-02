#8번, B835193 석채원
def getMax(list):
    max = list[0]
    for i in list:
        if(max<i):
            max = i
    list.remove(max)
    return max,list

def mySort(list):
    #새로운 리스트에 max값을 역순으로 저장한다.
    #getMax 함수에서 리턴하는 list값은 불필요하므로 trash에 저장하고 쓰지 않는다.
    rlist = []
    for i in range(len(list)):
        x,trash = getMax(list)
        rlist.insert(0,x)
    return rlist
        
def main():
 lst = [20, 60, 40, 10, 50]
 print(lst)
 print(mySort(lst))
main()