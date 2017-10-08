def funcSort():
    x = input()
    for i in range(len(x)-1, 0,-1):
        for j in range(0, i):
            if(x[j] > x[j+1]):
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
    print x
