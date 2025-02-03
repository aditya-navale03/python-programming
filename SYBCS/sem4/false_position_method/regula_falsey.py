def falsePosition(f, x0, x1, e):
    x0 = float(x0)
    x1 = float(x1)
    e = float(e)

    if f(x0) * f(x1) > 0.0:
        print("Initial guesses do not bracket the root. Try again with different values.")
        return

    step = 1
    condition = True
    while condition:
        # Compute the next approximation for the root
        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))

        # Print the current iteration's result
        print("Iteration %d, x2 = %0.6f, f(x2) = %0.6f" % (step, x2, f(x2)))

        # Check for convergence
        if abs(f(x2)) < e:  
            condition = False
            print("\nThe root is: %0.8f" % x2)

        
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        
        step += 1

# Example usage
def f(x):
    return x**3 - x - 1  

falsePosition(f, 1, 2, 0.0001)  
