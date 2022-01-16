import time

start = time.time()
best_number = 2
best_length = 0
for number in range(2, 1000):
    remainders = []
    remainder = 1
    length = 0
    while remainder > 0:
        if remainder in remainders:
            length = len(remainders) - remainders.index(remainder)
            break
        else:
            remainders.append(remainder)
            remainder = (remainder * 10) % number
    if (length > best_length):
        best_number = number
        best_length = length
end = time.time()

print("Best number is %d and its length is %d." % (best_number, best_length))
print("Executed in %f seconds." % (end - start))

