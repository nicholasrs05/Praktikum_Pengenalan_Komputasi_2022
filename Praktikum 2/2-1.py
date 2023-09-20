N = int(input('Masukkan bilangan: '))
fact = 1
count = 0

while (N >= 0):
    if (N == 0):
        fact = fact * 1
    else:
        fact = fact * N
    N = N - 1

end = int(fact % 10)
while (end == 0):
    count = count + 1
    fact = int(fact // 10)
    end = fact % 10

print(f'Banyaknya trailing zeros ada {count} buah.')