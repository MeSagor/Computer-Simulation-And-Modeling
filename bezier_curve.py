import matplotlib.pyplot as plt
import numpy as np

def cubic_bezier(p0, p1, p2, p3, t):
    return (1 - t)**3 * p0 + 3 * (1 - t)**2 * t * p1 + 3 * (1 - t) * t**2 * p2 + t**3 * p3

# control points
p0 = np.array([0, 0])
p1 = np.array([2, 1])
p2 = np.array([3, 5])
p3 = np.array([1, 4])

# Generate 100 points along the curve
t = np.linspace(0, 1, 100)
points = [cubic_bezier(p0, p1, p2, p3, t_val) for t_val in t]
x = [item[0] for item in points]
y = [item[1] for item in points]

plt.plot(x, y)
plt.plot([p0[0], p1[0], p2[0], p3[0]], [p0[1], p1[1], p2[1], p3[1]], 'o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cubic Bezier Curve')
plt.show()
