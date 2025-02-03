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
        
        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))

        print(f"Iteration {step}, x2 = {x2:.6f}, f(x2) = {f(x2):.6f}")

        
        if abs(f(x2)) < e:  
            condition = False
            print(f"\nRequired root is: {x2:.8f}")

        
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        
        step += 1  

# Example usage
def f(x):
    return x**3 - 3*x + 1  

falsePosition(f, 0, 1, 0.00001)  
