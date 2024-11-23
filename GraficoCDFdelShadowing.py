import numpy as np
import matplotlib.pyplot as plt

# Datos del laboratorio 3
dist_lab3 = [
    1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3,
    3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0,
    19.0, 20.0, 21.0, 22.0, 23.0, 24.0
]
pathloss_lab3 = [
    65.2, 66.4, 74.3, 71.0, 74.0, 70.2, 67.3, 70.3, 71.7, 69.1, 71.0, 71.2, 74.6, 74.1, 77.3, 79.0, 76.2, 78.4, 75.2, 72.7,
    73.6, 78.5, 82.5, 77.2, 76.3, 80.2, 79.3, 80.4, 75.8, 78.4, 76.8, 79.5, 79.3, 80.5, 77.0, 79.8, 79.1, 75.3, 76.4, 76.2,
    83.7, 80.0, 78.1, 81.3, 81.7, 78.9, 78.3, 82.7, 82.5, 78.7, 80.5, 80.4
]

# Datos del laboratorio 4
dist_lab4 = [
    1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3,
    3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.4, 4.8, 5.2, 5.6, 6.0, 6.4, 6.8, 7.2, 7.6, 8.0, 8.4, 8.8, 9.2, 9.6, 10.0, 10.4,
    10.8, 11.2, 11.6, 12.0
]
pathloss_lab4 = [
    55.0, 60.2, 66.5, 57.9, 56.1, 60.8, 66.2, 63.8, 65.6, 63.4, 70.2, 61.6, 66.0, 65.9, 71.4, 62.8, 61.6, 60.8, 62.2, 65.6,
    63.5, 64.0, 71.7, 60.4, 61.5, 61.3, 61.4, 70.6, 72.4, 63.1, 64.4, 63.7, 67.2, 65.4, 74.6, 72.5, 66.7, 69.7, 69.4, 69.3,
    72.2, 74.3, 74.2, 73.8, 71.2, 71.4, 71.1, 74.6, 71.0, 68.8, 66.5
]

# Convertir distancias a escala logarítmica
dist_lab3_log = np.log10(dist_lab3)
dist_lab4_log = np.log10(dist_lab4)

# Ajuste de curva con método de mínimos cuadrados
coeffs_lab3 = np.polyfit(dist_lab3_log, pathloss_lab3, 1)
coeffs_lab4 = np.polyfit(dist_lab4_log, pathloss_lab4, 1)

fit_lab3 = np.poly1d(coeffs_lab3)
fit_lab4 = np.poly1d(coeffs_lab4)

# Cálculo del shadowing (residuales)
shadowing_lab3 = pathloss_lab3 - fit_lab3(dist_lab3_log)
shadowing_lab4 = pathloss_lab4 - fit_lab4(dist_lab4_log)

# Estadísticas
mean_shadowing_lab3 = np.mean(shadowing_lab3)
std_shadowing_lab3 = np.std(shadowing_lab3)

mean_shadowing_lab4 = np.mean(shadowing_lab4)
std_shadowing_lab4 = np.std(shadowing_lab4)

# Calcular CDF
shadowing_lab3_sorted = np.sort(shadowing_lab3)
shadowing_lab4_sorted = np.sort(shadowing_lab4)

cdf_lab3 = np.arange(1, len(shadowing_lab3_sorted) + 1) / len(shadowing_lab3_sorted)
cdf_lab4 = np.arange(1, len(shadowing_lab4_sorted) + 1) / len(shadowing_lab4_sorted)

# Gráfico CDF para laboratorio 3 y 4
plt.figure(figsize=(10, 6))
plt.plot(shadowing_lab3_sorted, cdf_lab3, label=f'Lab 3 (Media={mean_shadowing_lab3:.2f}, Desv={std_shadowing_lab3:.2f})', color='b')
plt.plot(shadowing_lab4_sorted, cdf_lab4, label=f'Lab 4 (Media={mean_shadowing_lab4:.2f}, Desv={std_shadowing_lab4:.2f})', color='r')
plt.xlabel('Shadowing (dB)')
plt.ylabel('CDF')
plt.title('CDF del Shadowing para Laboratorios 3 y 4')
plt.legend()
plt.grid(True)
plt.show()
