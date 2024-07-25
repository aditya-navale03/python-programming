#Q.to find 10 terms of sequence of function f(x) = x sqr + x
def f(x):
    return (x**2) + x
for n in range(1, 11):
    term = f(n)
    print(f"Term {n}: {term}")