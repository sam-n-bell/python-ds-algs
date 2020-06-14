sequences = dict()

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if sequences.get(n - 2) is None:
            sequences[n - 2] = fib(n - 2)
        if sequences.get(n - 1) is None:
            sequences[n - 1] = fib(n - 1)
        return sequences.get(n - 2) + sequences.get(n - 1)

n = 100
print(f'The {n}(th) term of fib is {fib(n)}')



