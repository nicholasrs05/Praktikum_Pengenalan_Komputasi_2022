N = int(input('Masukkan bilangan N: '))
sum = 0
curr = 0
prev = 0

for i in range (1, N+1):
    if (i > 1):
        curr = prev * 10 + (i % 10)
    else:
        curr = 1
    prev = curr
    sum = sum + curr
    
print(f'Bilangan ke-{N} adalah {curr} dengan jumlah {N} suku pertama adalah {sum}')