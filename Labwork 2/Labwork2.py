import matplotlib as plt
def f(w1, w0, x, y):
    return 1/2 * (w1*x + w0 - y)**2

def df0(w1, w0, x, y):
    return w1*x + w0 - y

def df1(w1, w0, x, y):
    return x * (w1*x + w0 - y)

def loss(w0, w1, x, y):
    s = 0
    for i in range(len(x)):
        s += f(w1, w0, x[i], y[i])
    return s / len(x)

def gd(w1, w0, r, t, x, y):
    c = 0
    n = len(x)
    
    while abs(loss(w0, w1, x, y)) > t:
        g0 = 0
        g1 = 0
        
        for i in range(n):
            g0 += df0(w1, w0, x[i], y[i])
            g1 += df1(w1, w0, x[i], y[i])
            
        g0 = g0 / n
        g1 = g1 / n
        
        w0 = w0 - r * g0
        w1 = w1 - r * g1
        
        c += 1
        print(f"{c} {w0:.3f} {w1:.3f} {loss(w0, w1, x, y):.3f}")

if __name__ == "__main__":
    w0 = 0
    w1 = 1
    r = 0.0001
    t = 10
    x = []
    y = []

    with open('lr.csv', 'r') as csv:
        lines = [line.rstrip() for line in csv]

    for line in lines:
        row = line.split(',')
        x.append(float(row[0]))
        y.append(float(row[1]))

    gd(w1, w0, r, t, x, y)
