length = int(input('Masukkan panjang bilangan biner: '))
biner = str(input('Masukkan bilangan biner: '))
ArrBiner = list(biner)

simpan = 0
if ('0' in ArrBiner):
    for i in range (length):
        if (ArrBiner[i] == '0'):
            panjang = 0
            for j in range (length):
                if (i != j):
                    if (ArrBiner[j] == '0'):
                        if (panjang >= simpan):
                            simpan = panjang
                        panjang = 0
                    else:
                        panjang += 1
                if (panjang >= simpan):
                    simpan = panjang
else:
    simpan = length

print(f'Panjang 1 berurutan maksimum adalah {simpan}')