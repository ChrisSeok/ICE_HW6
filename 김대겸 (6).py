# 6번_B735042_김대겸

# random함수 호출
import random
# 사용잘부터 주사위를 던지는 횟수를 입력받는다.
try_num = int(input("주사위를 던지는 횟수를 입력하시오 : "))
# 주사위 값의 빈도를 저장할 리스트 resultList를 선언한다.
resultList = [0, 0, 0, 0, 0, 0]
# 주사위를 던지며 resultList의 요소에 각각의 횟수를 더한다.
for i in range(try_num):
    x = random.randint(1, 6)
    resultList[x-1] = resultList[x-1] + 1
# 결과를 출력한다.
for i in range(6):
    print("주사위가" , i + 1, "인 경우는", resultList[i], "번")
