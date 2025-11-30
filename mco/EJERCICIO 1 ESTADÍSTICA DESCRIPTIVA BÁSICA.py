import matplotlib.pyplot as plt
import wooldridge as wd

# Dataset de salarios (informática)
data = wd.data('wage1')
salarios = data['wage']

print("=== ANÁLISIS DESCRIPTIVO SALARIOS ===")
print(f"Media: ${salarios.mean():.2f}")
print(f"Mediana: ${salarios.median():.2f}")
print(f"Desviación Estándar: ${salarios.std():.2f}")
print(f"Mínimo: ${salarios.min():.2f}")
print(f"Máximo: ${salarios.max():.2f}")

# Histograma
plt.figure(figsize=(10, 6))
plt.hist(salarios, bins=20, alpha=0.7, color='skyblue', edgecolor='black')
plt.axvline(salarios.mean(), color='red', linestyle='--', label=f'Media (${salarios.mean():.2f})')
plt.axvline(salarios.median(), color='green', linestyle='--', label=f'Mediana (${salarios.median():.2f})')
plt.xlabel('Salario por Hora ($)')
plt.ylabel('Frecuencia')
plt.title('Distribución de Salarios - Sector Tecnología')
plt.legend()
plt.show()

# INTERPRETACIÓN: 
# La distribución muestra que la mayoría gana entre $5-10/hora, con algunos outliers hasta $25
# La media > mediana indica sesgo positivo (pocos salarios muy altos)
