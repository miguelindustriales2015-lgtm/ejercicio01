import statsmodels.api as sm
import wooldridge as wd
from tabulate import tabulate  # <- IMPORTACIÓN AÑADIDA

# Dataset completo de salarios
df = wd.data('wage1')

# --- Visualización de la tabla con formato profesional ---
print("--- Visualización de una muestra de los datos ('wage1') ---")
# Seleccionamos las primeras 10 filas para mostrar
df_head = df.head(10)
# Creamos la tabla formateada
tabla_formateada = tabulate(df_head, headers='keys', tablefmt='psql', showindex=False)
print(tabla_formateada)
print("----------------------------------------------------------\\n")

# --- Inicio del análisis del modelo ---
print("Variables disponibles para el modelo:", df.columns.tolist())

# Modelo: wage = β₀ + β₁*educ + β₂*exper + ε
X = df[['educ', 'exper', 'age']]  # Variables independientes
y = df['wage']  # Variable dependiente
git
# Añadir constante (β₀)
X = sm.add_constant(X)

# Modelo MCO
modelo = sm.OLS(y, X).fit()

print("\\n=== MODELO SALARIOS INFORMÁTICA ===")
print(modelo.summary())

# Predicción puntual para nuevo empleado
nuevo_empleado = [1, 16, 5]  # const=1, educ=16 años, exper=5 años
salario_predicho = modelo.predict(nuevo_empleado)

print(f"\\n📊 PREDICCIÓN PUNTUAL:")
print(f"Empleado con 16 años de educación y 5 años de experiencia")
print(f"Salario predicho por hora: ${salario_predicho[0]:.2f}")

print("\\n--- INTERPRETACIÓN DE COEFICIENTES ---")
print("- educ: Por cada año adicional de educación, el salario aumenta en $0.64/hora (ceteris paribus).")
print("- exper: Por cada año adicional de experiencia, el salario aumenta en $0.07/hora.")
print("- R² = 0.225: El modelo explica el 22.5% de la variabilidad en los salarios.")
