sequences = dict()

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if sequences.get(n - 2) is None:
            new_seq = fib(n - 2)
            sequences[n - 2] = new_seq
        if sequences.get(n - 1) is None:
            new_seq = fib(n - 1)
            sequences[n - 1] = new_seq
        return sequences.get(n - 2) + sequences.get(n - 1)

n = 100
print(f'The {n}(th) term of fib is {fib(n)}')



