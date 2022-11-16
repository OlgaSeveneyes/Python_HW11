# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# 1. Определить корни
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 4. Построить график
# 5. Вычислить вершину
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0

# 4 Построить график

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')
function_x = sp.sympify('-12*(x**4)*sin(cos(x)) - 18*(x**3)+5*(x**2) + 10*x - 30')
interval = np.arange(-100, 100, 0.01)
x_values = [function_x.subs(x, value) for value in interval]
plt.figure(figsize = (15, 8))
plt.plot(x_values)
plt.show()