for number in range(1,1001,1):
    s=0
    for i in range(1,number,1):
        if number%i==0:
            s+=i
    if s==number:print(f"{number} la so hoan thien")