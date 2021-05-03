#7번문제 / C111061 박서연

def getMax(n):
    big = max(n)
    except_big = list(n)
    except_big.remove(max(n))
    return big,except_big
    

def main():
    lst = [20, 60, 40, 10, 50]
    m, rlst = getMax(lst)
    print(m)
    print(rlst)
    

main()