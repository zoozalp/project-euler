import time

start = time.time()
sum, size, index = 1, 1, 1
while size < 1001:
    size += 2
    for i in range(4):
        index += size - 1
        sum += index
end = time.time()

print("Sum of diagonals is %d" % (sum))
print("Executed in %f seconds" % (end - start))

