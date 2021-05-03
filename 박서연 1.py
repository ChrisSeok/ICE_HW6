#1번문제 / C111061 박서연

numbers = []
numberSum = 0

while True:
    value = int(input("정수를 입력하세요: "))
    
    if value >= 0:
        numbers.append(value)
        numberSum = numberSum + value
    else:
        break
    
numberAverage = numberSum / len(numbers)

highNumber = 0
for i in range(len(numbers)):
    if numbers[i] > numberAverage:
        highNumber = highNumber + 1
        
print("평균=", numberAverage)
print("평균을 상회하는 숫자의 개수=", highNumber)