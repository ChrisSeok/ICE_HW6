#9번문제 / C111061 박서연 

def sortList(n):
    if len(n) < 2:
        return n
    
    choice = n[0]
    low = []
    high = []
    result = []
    
    for i in range(1, len(n)):
        if choice > n[i]:
            low.append(n[i])
        else:
            high.append(n[i])
    
    low = sortList(low)
    high = sortList(high)
    
    result = result + low
    result = result + [choice]
    result = result + high
    
    return result

def main():
    lst = [20, 60, 40, 10, 50]
    print(lst)
    print(sortList(lst))
    

main()
          
        