#5번문제 / C111061 박서연 

def getMean(n):
    sum = 0
    for i in range(len(n)):
        sum = sum + int(n[i])
    global mean
    mean = sum / len(n)
    return mean
    

def getDeviation(n):
    sum_deviation = 0
    for i in range(len(n)):
        deviation = int(n[i]) - mean
        sum_deviation = sum_deviation + deviation**2
    dispersion = sum_deviation / len(n)
    standard_deviation = dispersion**0.5
    return standard_deviation
    

def main():
    inputString = input("정수 리스트 입력: ")
    list1 = inputString.split()
    
    print("평균=", getMean(list1))
    print("표준 편차", getDeviation(list1))
    
main()