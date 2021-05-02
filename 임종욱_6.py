#6번 C111152 임종욱
from random import randint

# cnt_Max 주사위를 던지는 횟수
cnt_Max = int(input("주사위를 던지는 횟수를 입력하시오 : "))
dice = [0,0,0,0,0,0]

while  cnt_Max > 0 :
    i = randint(1,6)
    dice[i-1] += 1
    cnt_Max -= 1
    
for j in range(6):
    print('주사위가',j + 1,'인 경우는',dice[j])