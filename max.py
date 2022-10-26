def myMax(x):
    
    numbers2 = list("0123456789")
    x = list(x)
    numbers = []
    i = 0
    j = 0
    while i < (len(x)):
        
        if x[i] != ",":

            if x[i] == "-":
                numbers.append(int("-" + x[i+1]))
                i+=2
                j+=1
            elif x[i] == ".":
                numbers[j-1] = float(str(numbers[j-1]) + str(x[i]) + str(x[i+1]))
                i+=2
            elif i > 1 and x[i-1] in numbers2:
                try:
                    numbers[j-1] = int(str(numbers[j-1]) + str(x[i]))
                    i+=1
                except:
                    numbers[j-1] = float(str(numbers[j-1]) + str(x[i]))
                    i+=1  
            else:
                numbers.append(int(x[i]))
                i+=1
                j+=1
        else:
            i+=1



    i = 1
    position = 0
    maximal = numbers[0]
    while i < len(numbers):
        if numbers[i] > maximal:
            maximal = numbers[i]
            position = i+1
        i+=1

    return (maximal, position, numbers)