def f(x):
    return x**2
def f_(x):
    return 2*x

def gradient_descent(x, learning_rate, threshold):
    cnt = 0
    while abs(f(x)>threshold):
        x = x - (learning_rate * f_(x))
        cnt += 1
        print(f"{cnt} {x:.3f} {f(x):.3f}")

        
if __name__ == "__main__":
    x = 10
    learning_rate = 0.1
    threshold = 0.01
    gradient_descent(x, learning_rate, threshold)