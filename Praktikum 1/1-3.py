P = int(input('Masukkan banyak kelompok P: '))
E = int(input('Masukkan banyak kelompok E: '))
N = int(input('Masukkan banyak kelompok N: '))
G = int(input('Masukkan banyak kelompok G: '))

Mobil = P + E + (N / 2)
if (E >= G):
    G = 0
else:
    G = G - E
N = N % 2
if ((G > 0) and (N > G)):
    Mobil = Mobil + G
    G = 0
elif ((G > 0) and (G > N)):
    Mobil = Mobil + N
    G = G - N
Mobil = int(Mobil + (G / 2))

print(f'Banyak mobil yang dibutuhkan adalah {Mobil}')