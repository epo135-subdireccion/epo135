import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def analizar_funcion(expresion_str):
    x = sp.symbols('x')
    # Conversión de cadena a expresión simbólica
    f = sp.sympify(expresion_str)
    
    # Cálculo de derivadas
    f_prime = sp.diff(f, x)
    f_double_prime = sp.diff(f_prime, x)
    
    # Hallar raíces y puntos críticos (numéricamente para mayor robustez)
    raices = sp.solve(f, x)
    puntos_criticos = sp.solve(f_prime, x)
    
    # Función para evaluación numérica
    f_num = sp.lambdify(x, f, 'numpy')
    
    return {
        "funcion": f,
        "derivada": f_prime,
        "segunda_derivada": f_double_prime,
        "raices": raices,
        "puntos_criticos": puntos_criticos,
        "f_num": f_num
    }

# Ejemplo de uso con una función mixta
resultado = analizar_funcion("x**2 * exp(-x) * sin(x)")
