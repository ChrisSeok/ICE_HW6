#1번_B735042_김대겸

# 빈 리스트와 입력받을 변수들의 합을 저장할 변수를 선언.
user_values = []
user_sum = 0
# 사용자로부터 정수를 입력받고 그 값들이 0보다 크다면 user_values에 저장하고, user_sum에
# 더하는 반복문 진행.
while True:
    value = int(input("정수를 입력하세요: "))
    if value < 0:
        break
    user_values.append(value)
    user_sum += value
# 평균을 구하고 출력.
user_ave = (user_sum / len(user_values))
print("평균= ", user_ave)
# 평균을 상회하는 숫자의 개수를 구하고 출력.
highValues = 0
for i in user_values:
    if i > user_ave:
        highValues += 1
print("평균을 상회하는 숫자의 개수= ", highValues)
