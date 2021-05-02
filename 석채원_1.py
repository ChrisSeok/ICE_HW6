#1번, B835193 석채원
def Scores():
    scores = [] #init list
    #양의 정수 입력받기, 음수일 경우 break
    while True:
        inputnum = int(input("정수를 입력하세요:"))
        if(inputnum>0):
            scores.append(inputnum)
        else:
            break
        
        #평균 구하기
    sum = 0
    for i in scores: #원소 list[index]로 접근x, in listname 으로 접근가능
        sum+=i
    avg = sum/len(scores)
    print("평균=",avg)
        
    #평균을 넘는 숫자 개수 구하기
    mnum = 0
    for i in scores:
        if(i>avg):
            mnum+=1
    print("평균을 상회하는 숫자의 개수=",mnum)
    
def main():
    Scores()
main()
        
    
