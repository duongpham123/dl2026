e = 2.71828182846
def sigmoid(x):
    return 1 / (1 + e**(-x)  )
def log(x):
    n = 1000.0
    return n * ((x ** (1 / n)) - 1)
def f(w0,w1,w2,x1,x2):
    return w1*x1 +w2*x2+w0
def loss_single(w0, w1, w2, x1, x2, y):
    return -y *log(sigmoid(f(w0,w1,w2,x1,x2))) - (1-y)*log(1-sigmoid(f(w0,w1,w2,x1,x2)))
def loss_all(w0, w1, w2, x1, x2, y):
    sum = 0
    for i in range(len(y)):
        sum += loss_single(w0, w1, w2, x1[i], x2[i], y[i])
    return sum/len(y)
def dLw0(w0, w1, w2, x1, x2, y):
    return 1 - y -sigmoid(-f(w0,w1,w2,x1,x2))
def dLw0_all(w0, w1, w2, x1, x2, y):
    sum = 0
    for i in range(len(y)):
        sum += dLw0(w0, w1, w2, x1[i], x2[i], y[i])
    return sum/len(y)
def dLw1(w0, w1, w2, x1, x2, y):
    return -y *x1 + x1*(1 -sigmoid(-f(w0,w1,w2,x1,x2)))
def dLw1_all(w0, w1, w2, x1, x2, y):
    sum = 0
    for i in range(len(y)):
        sum += dLw1(w0, w1, w2, x1[i], x2[i], y[i])
    return sum/len(y)
def dLw2(w0, w1, w2, x1, x2, y):
    return -y *x2 + x2*(1-sigmoid(-f(w0,w1,w2,x1,x2)))
def dLw2_all(w0, w1, w2, x1, x2, y):
    sum = 0
    for i in range(len(y)):
        sum += dLw2(w0, w1, w2, x1[i], x2[i], y[i])
    return sum/len(y)
def grad(x1,x2,y,w0,w1,w2,lr,t):
    cnt = 0
    print(f"Time x f(x)")
    while abs(loss_all(w0, w1, w2, x1, x2, y)) > t:
        w0 = w0 -lr* dLw0(w0, w1, w2, x1, x2, y)
        w1 = w1 -lr* dLw1(w0, w1, w2, x1, x2, y)
        w2 = w2 -lr* dLw2(w0, w1, w2, x1, x2, y)
        cnt += 1
        print(f"{cnt} {w0:.3f} {w1:.3f} {w2:.3f} {loss_all(w0, w1, w2, x1, x2, y):.3f} ")
    return w0, w1, w2

def grad_all(x1,x2,y,w0,w1,w2,lr,t):

    cnt = 0
    while abs(loss_all(w0, w1, w2, x1, x2, y)) > t:
        w0 = w0 -lr* dLw0_all(w0, w1, w2, x1, x2, y)
        w1 = w1 - lr*dLw1_all(w0, w1, w2, x1, x2, y)
        w2 = w2 - lr*dLw2_all(w0, w1, w2, x1, x2, y)
        cnt += 1
        print(f"{cnt} {w0:.3f} {w1:.3f} {w2:.3f} {loss_all(w0, w1, w2, x1, x2, y):.3f} ")

    return w0, w1, w2
def readcsv(filestr):
    with open(filestr, 'r') as f:
        results = []
        for line in f:
            words = line.split(',')
            results.append((words[0], words[1].rstrip("\n\r"), words[2].rstrip("\n\r")))
    return results

if __name__ == "__main__":
    data = readcsv('loan2.csv')
    x1 = []
    x2 = []
    y = []

    print(data)

    col_names = data[0]
    print(col_names)

    for i in range(len(data) - 1):
        x1.append(float(data[i + 1][0]))
        x2.append(float(data[i + 1][1]))
        y.append(float(data[i + 1][2]))

    lr = 0.1
    t = 0.2
    w0 = 0
    w1 = 1
    w2 = 2
    print("Gradient Descent with all data points:")
    optimal_w0, optimal_w1, optimal_w2 = grad_all(x1, x2, y, w0, w1, w2, lr, t)