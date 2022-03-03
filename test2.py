def data(a,b,c):
    sum1=int(a+b+c)
    if sum1 < 21:
        return sum1
    
    elif sum1 > 21 and a == 11 or b == 11 or c == 11:
        sum2=sum1-10
        return sum2
    
    else:
        return "BUST"
        
    
    
print(data(5, 6, 7))
print(data(9, 9, 9))
print(data(9, 9, 11))