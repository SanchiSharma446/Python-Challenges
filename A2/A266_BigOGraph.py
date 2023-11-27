from matplotlib.pyplot import ylabel, plot, show, xlabel, title
import math
x = [2, 4, 6, 8, 10, 12]
c = [100, 100, 100, 100, 100, 100]
e = [2, 4, 8, 16, 32, 64]
f = []
l = []
q = []

for i in range(6):
    f.append(math.factorial(i+1))
    l.append(math.log(i+1))
    q.append((i+1)**2)

# y = [2, 4, 6, 8, 10, 12] # Try this for Linear complexity
plot(x, c, 'b')
plot(x, e, 'c')
plot(x, f, 'r')
plot(x, l, 'g')
plot(x, q, 'y')
xlabel('Inputs')
ylabel('Steps')
title("Different types of graphs")
show()
