def count_digits(n):
    if n <= 9:
        return n
    else:
        num_digits = 9
        power_of_10 = 10
        while power_of_10 <= n:
            num_digits += (min(n, power_of_10*10-1) - power_of_10 + 1) * len(str(power_of_10))
            power_of_10 *= 10
        return num_digits

t = int(input())
for i in range(t):
    n = int(input())
    print(count_digits(n))
