import matplotlib.pyplot as plt
import numpy as np

def discriminantni_hisobla(a, b, c):
    discriminant = b**2 - 4*a*c
    return discriminant

a = float(input("a ni kiriting: "))
b = float(input("b ni kiriting: "))
c = float(input("c ni kiriting: "))

discriminant = discriminantni_hisobla(a, b, c)

x = np.linspace(-10, 10, 400)
y = a*x**2 + b*x + c

print("Diskriminant qiymati:", discriminant)
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f"{a}x^2 + {b}x + {c}")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Diskriminant Grafiki')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()

