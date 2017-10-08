def funcInterest (x):
    t = 2 * x
    year = 0
    while(x < t):
        year += 1
        x = x * 1.0325
    print year
         
