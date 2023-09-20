One = int(input('Masukkan angka pertama: '))
Two = int(input('Masukkan angka kedua: '))
Three = int(input('Masukkan angka ketiga: '))
K = int(input('Masukkan K: '))

L = [0 for i in range (K)]

for i in range (K-1, -1, -1):
    if (i == K - 1):
        L[i] = One
    elif (i == K - 2):
        L[i] = Two
    elif (i == K - 3):
        L[i] = Three
    else:
        L[i] = L[i+3] * L[i+2] + L[i+1]

for i in range (K):
    if (i == K - 1):
        print(L[i])
    else:
        print(L[i], end=" ")