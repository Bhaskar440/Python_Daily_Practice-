#return the second largest element
if __name__ == '__main__':
    # number of elements and map containing elements is being given only 
    n = int(input())
    arr = map(int, input().split())
    # firstly converted them to sets to remove duplicate
    jrr = set(arr)
    #used sorted function to sort them ascending order 
    prr = sorted(jrr)
    print(prr[-2])