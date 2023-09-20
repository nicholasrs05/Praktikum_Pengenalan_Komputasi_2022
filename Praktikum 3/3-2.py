Len = int(input('Masukkan panjang kata: '))
Kata = str(input('Masukkan kata awal: '))
Li = list(Kata)
Cnt = [0 for i in range (Len)]
Proses = int(input('Masukkan banyak proses yang akan dilakukan: '))

for i in range (1, Proses+1):
    X = int(input(f'Masukkan banyak huruf awal yang dipilih kucing Tuan Riz pada proses ke-{i}: '))
    for j in range (X, Len):
        if (Cnt[j] % 2 == 0):
            Li[j] = 'a'
        else:
            Li[j] = 'b'
        Cnt[j] = Cnt[j] + 1

print('Password: ', end="")
for i in range (Len):
    print(Li[i], end="")