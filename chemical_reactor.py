import time

a = []
b = []
c = []

a_initial = 100
b_initial = 50
c_initial = 0

k1, k2 = 0.002, 0.003
a.append(a_initial)
b.append(b_initial)
c.append(c_initial)

total_time = 5
dt = 0.30

print("........................................")
print("|  Time   |  A(t)   |   B(t)  |  C(t)  |")
print("........................................")
print("|  %5.2lf  |  %5.2lf |  %5.2lf  | %5.2lf  |" % (0, a[-1], b[-1], c[-1]))

i = 0.0
while i < total_time:
    a.append(a[-1] + (k2*c[-1] - k1*a[-1]*b[-1])*dt)
    b.append(b[-1] + (k2*c[-1] - k1*a[-1]*b[-1])*dt)
    c.append(c[-1] + (2*k1*a[-1]*b[-1] - 2*k2*c[-1])*dt)
    print("|  %5.2lf  |  %5.2lf  |  %5.2lf  | %5.2lf  |" % (i, a[-1], b[-1], c[-1]))
    i += dt
    time.sleep(0.5)

print("........................................")