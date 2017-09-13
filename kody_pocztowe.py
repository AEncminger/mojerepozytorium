def kody(kod1, kod2):

    print("Generowanie kodów pocztowych")
    x = kod1 #input("Podaj pierwszy kod:")
    y = kod2 #input("Podaj drugi kod:")

    x1 = int(x[0:2] + x[3:6])
    y1 = int(y[0:2] + y[3:6])
    r = y1 - x1 + 1
    res = []

    for i in range(r):
        res.append(x1+i)
        st = str(res[i])
        st = st[0:2] + "-" + st[2:5]
        print(st)

kody("12-234", "12-265")
