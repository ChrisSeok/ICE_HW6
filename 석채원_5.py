#5번, B835193 석채원
import math
def getMean(list):
    sum = 0
    for i in list:
        i = int(i) #문자열인 원소들을 정수로 변환
        sum+=i
    global avg
    avg = sum/len(list)
    return avg
#list1엔 변화 없다
        
def getDeviation(list):
    sum=0
    for i in list:
        i = int(i) #문자열인 원소들을 정수로 변환
        i = i-avg
        sum+=i**2
        
    deviation = math.sqrt(sum/len(list))
    return deviation
        
    
def main():
 inputString = input("정수 리스트 입력: ")
# inputString을 list1으로 변환한다
 list1 = inputString.split() #공백 기준으로 리스트 저장
 print("평균=", getMean(list1))
# print(list1[0]+3)
 print("표준 편차", getDeviation(list1))

 
main()
