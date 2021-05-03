#8번문제 / C111061 박서연 

def getMax(n):
    big = max(n)
    return big


def mySort(m):
    s = []
    for i in range(len(m)):
        s.append(getMax(m))
        m.remove(getMax(m))
    s.reverse()
    return s
    
    
        
def main():
    lst = [20, 60, 40, 10, 50]
    print(lst)
    print(mySort(lst))
    

main()