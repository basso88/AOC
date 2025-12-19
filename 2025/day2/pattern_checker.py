def check_pattern(n=str):
    nn = ''
    mul = list()
    for m in range(1, len(n)):
        if len(n)%m == 0:
            mul.append(m)
    
    if len(n) > 1:
        for m in sorted(mul, reverse=True):
            for i in range(1, len(n)//m +1):
                if n[:m] == n[m:m*2]:
                    nn +=n[:m]
                    if n == nn:
                        # print(mul, n, nn)
                        return True
        
            
    
    
    

