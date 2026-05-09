def loadfunc(filestr):
    with open(filestr, 'r') as f:
        results = []
        for line in f:
                words = line.split(',')
                results.append((words[0], words[1].rstrip("\n\r")))
    return results

import matplotlib.pyplot as plt
data = loadfunc('lr.csv')
x =[]
y = []
for i in range(len(data)):
    x.append(float(data[i][0]))
    y.append(float(data[i][1]))

w0 = 45.976
w1 = 1.297

def f(w1, w0, x):
    return w1*x + w0

xpoints = [1, 100]
ypoints = [f(w1, w0, xpoints[0]), f(w1, w0, xpoints[1])]

print(xpoints)
print(ypoints)


plt.plot(xpoints, ypoints)
plt.plot(x, y, 'ro', linewidth=2, markersize=8) # red circles with dashed lines
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Line Plot")
plt.grid(True)
plt.show()
