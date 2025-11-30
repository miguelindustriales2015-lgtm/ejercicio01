import matplotlib.pyplot as plt
import numpy as np
import wooldridge as wd

# --- Carga de datos ---
# Dataset de salarios (informática) del paquete wooldridge
# Este es el mismo dataset que se usa en el Ejercicio 1
print("Cargando dataset 'wage1'...")
data = wd.data('wage1')
salarios = data['wage']
print("Dataset cargado.\\n")

# Simulación: Salarios de pequeñas muestras
np.random.seed(123)
medias_muestrales = []

for i in range(1000):
    muestra = np.random.choice(salarios, size=50, replace=True)  # Muestra n=50
    medias_muestrales.append(muestra.mean())

# Gráfica comparativa
plt.figure(figsize=(12, 5))

# Distribución original
plt.subplot(1, 2, 1)
plt.hist(salarios, bins=20, alpha=0.7, color='lightcoral')
plt.title('Distribución Original\\n(Sesgada a la derecha)')
plt.xlabel('Salario')

# Distribución de medias muestrales
plt.subplot(1, 2, 2)
plt.hist(medias_muestrales, bins=20, alpha=0.7, color='lightgreen')
plt.title('Distribución de Medias Muestrales\\n(Aproximadamente Normal)')
plt.xlabel('Media Muestral')

plt.tight_layout()
plt.show()

print(f"Media poblacional: ${salarios.mean():.2f}")
print(f"Media de medias muestrales: ${np.mean(medias_muestrales):.2f}")

# INTERPRETACIÓN:
# Aunque la distribución original es asimétrica, las medias de muestras siguen distribución normal
# Esto permite hacer inferencias incluso cuando los datos no son normales
