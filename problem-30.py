import time

start = time.time()
result = 0
for i in range(2,200000):
    number = i
    sum = 0
    while number > 0:
        digit = number % 10
        number //= 10
        sum += digit**5
    if sum == i:
        result += i
end = time.time()

print("Sum of all numbers that can be written as the sum of fifth powers of their digits is %d" % (result))
print("Executed in %f seconds" % (end - start))

