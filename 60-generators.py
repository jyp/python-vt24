

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

def naturals_from(start):
    i = start
    while True:
        yield i
        i = i+1

def is_prime(smaller_primes, candidate):
    for n in smaller_primes:
        if candidate % n == 0:
            # candidate is divisible by n
            return False
    return True

# generate all prime numbers
def primes():
    primes_so_far = []
    for candidate in naturals_from(2):
        if is_prime(primes_so_far,candidate):
            primes_so_far.append(candidate)
            yield candidate


# for i in my_range(10,20):
#     print(i)

# print(list(range(10,20)))
# print(my_range(10,20))

def main():
     for x in primes():
         if x > 100:
             return
         print (x)

main()
