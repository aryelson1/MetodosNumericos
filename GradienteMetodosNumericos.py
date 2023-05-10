import numpy as np

def gradient_descent(f, df, x0, alpha, eps=1e-6, interacoes=1000):

    
    for i in range(interacoes):
        grad = df(x0)
        x_new = x0 - alpha * grad
        if abs(x_new - x0) < eps:
            break
        x0 = x_new
        
    return x0, f(x0)



f = lambda x : x**2 + 2*x + 1
df = lambda x : 2*x + 2

print(gradient_descent(f, df, x0 = 1, alpha = 0.1))

