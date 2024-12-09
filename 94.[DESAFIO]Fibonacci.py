def Fibonacci(x):
    p1 = 0 
    p2 = 0
    p3 = 0
    for a in range(x-1):
        if p1 == 0 and p2 == 0 and p3 == 0:
            p3 = 1
            print(f"{p3} ", end=">> ")
        p1 = p2
        p2 = p3
        p3 = p1 + p2
        print(f"{p3} ", end=">> ")
    print("Fim!")


Fibonacci(9)