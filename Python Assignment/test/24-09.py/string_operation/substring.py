def substring(x):
    ch=""
    for i in range(len(x)):
        ch=x[i]
        print(ch)
        for j in  range(i+1,len(x)):
            ch=ch+x[j]
            print(ch)