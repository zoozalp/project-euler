import time

start = time.time()
numbers = []
for a in range(2,101):
    for b in range(a, 101):
        if a**b not in numbers:
            numbers.append(a**b)
        if b**a not in numbers:
            numbers.append(b**a)
end = time.time()

print("Count of distinct values is %d" % (len(numbers)))
print("Executed in %f seconds" % (end - start))

