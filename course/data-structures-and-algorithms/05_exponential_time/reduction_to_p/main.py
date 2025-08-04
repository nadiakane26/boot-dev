def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Polynomial time Fibonacci
    grandparent = 0
    parent = 1
    current = None
    
    for _ in range(n - 1):
        current = grandparent + parent
        grandparent = parent
        parent = current
    
    return current 
  
  # Exponential
    # return fib(n - 1) + fib(n - 2)

