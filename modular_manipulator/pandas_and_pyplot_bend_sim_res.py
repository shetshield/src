import numpy as np
import pandas as pd
from math import degrees
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

df = pd.read_csv('/Users/shetshield/Desktop/workspace/python_ws/sim_res/bend_response.csv')

x1 = list(df.loc[:, 'x1'].values / 1000)
x2 = list(df.loc[:, 'x2'].values / 1000)
x3 = list(df.loc[:, 'x3'].values / 1000)
x4 = list(df.loc[:, 'x4'].values / 1000)

y1 = list(df.loc[:, 'y1'].values / 1000)
y2 = list(df.loc[:, 'y2'].values / 1000)
y3 = list(df.loc[:, 'y3'].values / 1000)
y4 = list(df.loc[:, 'y4'].values / 1000)

z1 = list(df.loc[:, 'z1'].values / 1000)
z2 = list(df.loc[:, 'z2'].values / 1000)
z3 = list(df.loc[:, 'z3'].values / 1000)
z4 = list(df.loc[:, 'z4'].values / 1000)


def equation_plane(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    a1 = x2 - x1
    b1 = y2 - y1
    c1 = z2 - z1
    a2 = x3 - x1
    b2 = y3 - y1
    c2 = z3 - z1
    a = b1 * c2 - b2 * c1
    b = a2 * c1 - a1 * c2
    c = a1 * b2 - b1 * a2
    d = (- a * x1 - b * y1 - c * z1)
    print("equation of plane is ", a, "x + ", b, "y +", c, "z +", d, "=0.")


# equation_plane(x1[0], y1[0], z1[0], x3[0], y3[0], z3[0], x4[0], y4[0], z4[0])
# equation_plane(x1[3], y1[3], z1[3], x3[3], y3[3], z3[3], x4[3], y4[3], z4[3])

from sympy import Plane, Point3D, Line3D

p = Plane(Point3D(x2[0], y2[0], z2[0]), Point3D(x1[0], y1[0], z1[0]), Point3D(x3[0], y3[0], z3[0]))
# p = Plane(Point3D(x2[5], y2[5], z2[5]), Point3D(x1[5], y1[5], z1[5]), Point3D(x3[5], y3[5], z3[5]))
L = Line3D(Point3D(0, 0, 0), Point3D(0, 0, 1))
angle = list()
for i in range(len(x1)):
    p = Plane(Point3D(x2[i], y2[i], z2[i]), Point3D(x1[i], y1[i], z1[i]), Point3D(x3[i], y3[i], z3[i]))
    _angle  = abs(degrees(p.angle_between(L)))
    d_angle = 90 - _angle
    angle.append(d_angle)
    # print(_angle, d_angle)

X = np.linspace(-21, 0, 22)
print(angle)

fig = plt.figure()
ax  = fig.add_subplot(111)
ax.minorticks_on()
x_tick_list = [0, 5, 10, 15, 20]
x_tick_list = [-20, -15, -10, -5, 0]
y_tick_list = [0, 10, 20, 30, 40, 50]

ax.set_yticks(y_tick_list)
ax.set_xticks(x_tick_list)

plt.setp(ax.get_yticklabels(), fontsize=10)
plt.setp(ax.get_xticklabels(), fontsize=10)

ax.tick_params(which='both', width=1)
ax.tick_params(which='major', length=6)
ax.tick_params(which='minor', length=3, color='black')

ax.set_xlabel('Pressure (kPa)', fontsize=12)
ax.set_ylabel('Bending angle ($^\circ$)', fontsize=12)

ax.xaxis.set_minor_locator(plt.MultipleLocator(5/3))
ax.yaxis.set_minor_locator(plt.MultipleLocator(10/3))

ax.plot(X, list(reversed(angle)), c='black')

plt.show()
