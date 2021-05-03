# 5번_B735042_김대겸

# main()함수 선언.
def main():
    inputString = input("정수 리스트 입력: ")
    # inputString을 list1으로 변환한다
    list1 = list(map(int, inputString.split()))
    print("평균=", getMean(list1))
    print("표준 편차", getDeviation(list1))

# getMean()함수 선언.(평균과 구하고 그 값을 반환하는 함수)
def getMean(lst):
    lst_total = 0
    for i in lst:
        lst_total += i
    lst_average = (lst_total / len(lst))
    return lst_average

# getDeviation()함수 선언.(표준편차를 구하고 그 값을 반환하는 함수)
def getDeviation(lst):    
    ave = getMean(lst)
    cha_total = 0
    for i in lst:
        cha_total += ((i - ave)**2)
    devi = ((cha_total / (len(lst)))**(1/2))
    return devi

# main()함수 호출.
main()
