import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Étape 1 : Définir une fonction symbolique avec SymPy
x = sp.symbols('x')
f_expr = sp.sin(x**2) / x

# Étape 2 : Convertir en fonction utilisable avec NumPy
f_lambdified = sp.lambdify(x, f_expr, modules=['numpy'])

# Étape 3 : Générer les données numériques
x_vals = np.linspace(-10, 10, 1000)
y_vals = f_lambdified(x_vals)

# Étape 4 : Tracer avec Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) = sin(x²)/x', color='royalblue')
plt.title('Graphe de la fonction f(x) = sin(x²)/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()
