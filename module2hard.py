n = int(input("Введите число n (от 3 до 20): " ))
def generate_pairs(n):

    pairs = []

    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i+j) == 0  and i not in [pair for pair in pairs for nambe in pair]:
                pairs.append((i, j))

    return pairs

pairs = generate_pairs(n)

result = "".join([str(pair[0]) + str(pair[1]) for pair in pairs])
print(f"Пароль для числа {n}: {result}")
