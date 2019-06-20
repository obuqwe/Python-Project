
def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

print(f'5!={factorial(5)}, 3!={factorial(3)}, 11!={factorial(11)}')


def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        nums.append(current)

    return nums

print(fibonacci(100))

