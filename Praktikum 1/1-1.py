K = int(input('Masukkan kartu Tuan Kil: '))
L = int(input("Masukkan kartu Tuan Leo: "))

if (((K > L) and (K != 1)) or ((K == 1) and (L != 1))):
    print('Pemenangnya adalah Tuan Kil')
elif (((L > K) and (L != 1)) or ((L == 1) and (K != 1))):
    print('Pemenangnya adalah Tuan Leo')
else:
    print('Permainan berakhir seri')