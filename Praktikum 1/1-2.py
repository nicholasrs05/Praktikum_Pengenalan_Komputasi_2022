Roda = int(input('Masukkan banyak roda kendaraan: '))
Time = int(input('Masukkan lama kendaraan terparkir (jam): '))

if (Roda == 2):
    if (Time <= 3):
        Biaya = 2000
    elif ((Time > 3) and (Time < 24)):
        Biaya = 2000 + 1000 * (Time - 3)
    else:
        Biaya = 30000
else:
    if (Time <= 3):
        Biaya = 5000
    elif ((Time > 3) and (Time < 24)):
        Biaya = 5000 + 2000 * (Time - 3)
    else:
        Biaya = 70000

print(f'Biaya parkir sebesar Rp {Biaya}')