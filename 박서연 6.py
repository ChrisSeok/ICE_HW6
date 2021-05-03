#6번문제 / C111061 박서연 

count = int(input("주사위를 던지는 횟수를 입력하시오 : "))

import random
eachCount = [0, 0, 0, 0, 0, 0]

for i in range(count):
    dice = random.randint(0, 5)
    eachCount[dice] = eachCount[dice] + 1
    
for i in range(6):
    print("주사위가", i+1, "인 경우는 ", eachCount[i], "번")