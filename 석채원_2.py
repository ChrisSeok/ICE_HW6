#2번, B835193 석채원
def reverseList(list):
    #역순 리스트를 저장할 리스트 초기화
    reverse = []
    #list원소에 역순으로 접근-slicing이용(list는 바뀌지x)
    for i in list[::-1]:
        reverse.append(i)
    return reverse
    
def main():
 lst = [20, 60, 40, 10, 50]
 print(reverseList(lst))
 print(lst)
 
main()
