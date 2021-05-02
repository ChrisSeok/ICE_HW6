#7번, B835193 석채원
def getMax(list):
    #제일 큰 수 찾기
    max = list[0]
    for i in list:
        if(max<i):
            max = i
    #제일 큰 수 제거
    list.remove(max)
    
    return max,list
            
def main():
 lst = [20, 60, 40, 10, 50]
 m, rlst = getMax(lst)
 print(m)
 print(rlst)
main()
