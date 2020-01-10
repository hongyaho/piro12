def minimum(n):
    mn = n-len(str(n))*9
    mn = 1 if mn < 1 else mn
    for i in range(mn, n):
        a = i
        a += sum(map(int, str(i)))
        if a == unum:
            print(i)
            return

unum = int(input('자연수 N (1<= N <= 1,000,000) '))
minimum(unum)