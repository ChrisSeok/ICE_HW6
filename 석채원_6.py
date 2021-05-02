#6번, B835193 석채원
import random
times = int(input("주사위를 던지는 횟수를 입력하시오 :"))
dice = []
for i in range(times):
    x = random.randint(1,6)
    dice.append(x)
    
for i in range(1,7):
    count = 0 #i 바뀔 때마다 초기화
    print("주사위가 %d 인 경우는"%i,end='')
    for j in dice:
        if(i==j):
            count+=1
    print(count,"번")
    
    
    
    


        