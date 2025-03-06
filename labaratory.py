import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from math import sin, cos, exp

# Parametrlarni foydalanuvchi kiritishi
a = float(input("x ning boshlang'ich qiymatini kiriting (a): "))
b = float(input("x ning oxirgi qiymatini kiriting (b): "))
p = float(input("p ni kiriting (y' ning koeffitsienti): "))
q = float(input("q ni kiriting (y ning koeffitsienti): "))
y0 = float(input("y(a) ning boshlang'ich qiymatini kiriting (y0): "))
dy0 = float(input("y'(a) ning boshlang'ich qiymatini kiriting (dy0): "))
f_expr = input("f(x) funksiyasini kiriting (masalan, sin(x), cos(x), exp(x), yoki x**2): ")

# f(x) funksiyasini aniqlash
def f(x):
    return eval(f_expr)

# 2-tartibli ODT ni birinchi tartibli tizimga aylantirish
def ode_system(x, z):
    z1, z2 = z
    dz1dx = z2
    dz2dx = f(x) - p*z2 - q*z1
    return [dz1dx, dz2dx]

# Boshlang'ich shartlar
z0 = [y0, dy0]

# YeChim
x_vals = np.linspace(a, b, 100)
sol = solve_ivp(ode_system, [a, b], z0, t_eval=x_vals)

# Grafik
plt.plot(sol.t, sol.y[0], label='y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()