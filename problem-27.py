import math
import time


def is_prime(number):
    if number < 2:
        return False
    elif number % 2 == 0:
        return number == 2
    elif number % 3 == 0:
        return number == 3
    else:
        h = 1 + math.sqrt(number)
        i = 5
        while i <= h:
            if number % i == 0:
                return False
            elif number % (i + 2) == 0:
                return False
            else:
                i += 6
        return True


start = time.time()
best = []
best_length = 0
for a in range(-999, 1000):
    for b in range(2, 1000):
        if is_prime(b):
            n = 1
            while is_prime((n**2) + (a * n) + b):
                n += 1
            if n > best_length:
                best = [a, b]
                best_length = n
end = time.time()

print("Best coefficients are (%d,%d) and their product is %d" % (best[0] , best[1],best[0] * best[1]))
print("Executed in %f seconds" % (end - start))


