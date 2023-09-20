M = int(input('Masukkan nilai M: '))
cntmax = 0
cntmin = 0

for i in range (1, M+1):
    f = int(input(f'Masukkan nilai fungsi titik ke-{i}: '))
    if (i == 1):
        max = f
        min = f
        prev2 = f
    elif (i == 2):
        cntmax = 1
        cntmin = 1
        prev1 = f
    else:
        if ((f > prev1) and (prev1 < prev2)):
            cntmax = cntmax + 1
        elif ((f < prev1) and (prev1 > prev2)):
            cntmin = cntmin + 1
        prev2 = prev1
        prev1 = f

print(f'Terdapat {cntmax} titik maksimum lokal dan {cntmin} titik minimum lokal.')