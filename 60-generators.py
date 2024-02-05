

def my_range(start, end):
    i = start
    while i < end:
        yield i
        i = i + 1

def my_reversed(l):
    i = len(l)
    while i > 0:
        i = i-1
        yield l[i]

print (range(1,3)[1])
        
def naturals_from(start):
    i = start
    while True:
        yield i
        i = i+1


# generate all prime numbers
def primes():
    primes_so_far = []
    for candidate in naturals_from(2):
        for n in primes_so_far:
            if candidate % n == 0:
                # candidate is divisible by n
                break
        else:
            primes_so_far.append(candidate)
            yield candidate


# for i in my_range(10,20):
#     print(i)

# print(list(range(10,20)))
# print(my_range(10,20))

# for x in primes():
#     if x > 100:
#         continue
#     print (x)

