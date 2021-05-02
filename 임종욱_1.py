#1번 C111152 임종욱

i = 0
Sum = 0
Int = []
while True:
    Int.append(int(input("정수를 입력하세요: ")))
    if Int[i] < 0:
        break
    Sum += Int[i]
    i += 1
    
average = Sum / i
count = 0
for j in Int:
    if j >average:
        count += 1
        
print("평균= %d\n평균을 상화하는 숫자의 개수= %d"%(average,count))
