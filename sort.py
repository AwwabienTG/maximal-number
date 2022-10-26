import max as m

def mySort(x):
    j = 0

    while j < len(x):
        i = 0
        while i < (len(x) - 1):
            if x[i] < x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]

            i+=1
        j+=1
    
    return x