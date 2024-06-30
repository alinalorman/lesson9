numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for number in numbers:
    if number == 1:
        # Пропускаем число 1, так как оно не является ни простым, ни составным
        continue

    is_prime = True  # Флаг для проверки простоты числа
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break  # Оптимизация: выходим из цикла, если найден делитель

    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

print("Primes:", primes)
print("Not Primes:", not_primes)