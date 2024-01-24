import time
import matplotlib.pyplot as plt

a = []
b = []
c = []

a_initial = 1
b_initial = 0.5
c_initial = 0

k1, k2 = 0.05, 0.05
a.append(a_initial)
b.append(b_initial)
c.append(c_initial)

total_time = 100
total_step = 500
dt = total_time/total_step

print("........................................")
print("|  Time   |  A(t)   |   B(t)  |  C(t)  |")
print("........................................")
print("|  %5.2lf  |  %5.2lf |  %5.2lf  | %5.2lf  |" % (0, a[-1], b[-1], c[-1]))

window_x = total_step+10
plt.figure(figsize=(6, 5))
plt.axis([0, window_x, None, None])
plt.title('Chemical Reactor')
plt.xlabel('Time')
plt.ylabel('Mole')
plt.ion() 
plt.show()

i = 0.0
while i < total_time:
    a.append(a[-1] + (k2*c[-1] - k1*a[-1]*b[-1])*dt)
    b.append(b[-1] + (k2*c[-1] - k1*a[-1]*b[-1])*dt)
    c.append(c[-1] + (2*k1*a[-1]*b[-1] - 2*k2*c[-1])*dt)
    print("|  %5.2lf  |  %5.2lf  |  %5.2lf  | %5.2lf  |" % (i, a[-1], b[-1], c[-1]))
    i += dt

    plt.plot(a, color='blue', label='A')
    plt.plot(b, color='red', label='B')
    plt.plot(c, color='green', label='C')
    if i==dt:
        plt.legend(loc='upper right')
    plt.draw()
    plt.pause(0.05)

print("........................................")
plt.pause(5)