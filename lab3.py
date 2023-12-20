import matplotlib.pyplot as plt
import numpy as np

with open('DS0.txt', 'r') as file:
    data = file.readlines()

points = [list(map(int, point.strip().split())) for point in data]
points_array = np.array(points)

rotation_point = np.array([[480, 480]])
angle = np.radians(90)
rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
transformed_points = np.dot(points_array - rotation_point, rotation_matrix) + rotation_point


plt.figure(figsize=(12, 12), dpi=80)
plt.axis([0, 960, 0, 960])
plt.scatter(transformed_points[:, 0], transformed_points[:, 1], color='blue', label='Transformed Points')
plt.grid(True)

plt.legend()
plt.savefig('rotated.png')
plt.show()
