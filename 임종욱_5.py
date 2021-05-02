#5번 C111152 임종욱
#평균을 구하는 함수
def getMean(list1):
    Sum = 0
    for i in list1:
        Sum += i
    global average
    average = Sum /len(list1)
    return average
# 표본표준편차를 구하는 함수
def getDeviation(list1):
# dSum은  편차의 제곱의 합
    dSum = 0
    for i in list1:
        dSum += (i - average)**2
    #표본표준편차 v
    v = (dSum / (len(list1) - 1))**(1/2)     
    return v

def main():
    inputString = input("정수 리스트 입력: ")
# inputString을 list1으로 변환한다
    ls = (inputString).split() #문자열 리스트 변환
    list1 = []
#   리스트안의 숫자 문자열을 정수로 바꾼다
    for i in ls:
        list1 += [int(i)]
#평균을 모든 함수에서 사용할 수 있도록 선언한다. 
    average = 0
    print("평균=", getMean(list1))
    print("표준 편차", getDeviation(list1))

main()
