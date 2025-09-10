import matplotlib.pyplot as plt
import numpy as np

# 定義 Antoine 方程常數（對應水）
A = 8.07131
B = 1730.63
C = 233.426

# 定義溫度範圍
T = np.linspace(-10, 120, 500)  # 攝氏度

# 計算蒸氣壓
P_liquid_vapor = 10 ** (A - (B / (C + T)))  # mmHg
P_liquid_vapor = P_liquid_vapor * 133.322  # 轉換為 Pa

# 定義熔化潛熱和升華潛熱 (假設值)
delta_H_f = 333.55e3  # J/kg
delta_H_v = 2260e3  # J/kg
delta_H_s = delta_H_f + delta_H_v  # J/kg

# 定義體積變化（假設值）
delta_V_f = 1e-6  # m^3/kg
delta_V_v = 1e-3  # m^3/kg
delta_V_s = delta_V_f + delta_V_v  # m^3/kg

# 定義壓力範圍
P = np.linspace(611.657, 101325, 500)  # Pa

# 計算固-液平衡
T_fusion = 273.15 - (delta_H_f / (delta_V_f * P))  # K

# 計算固-氣平衡
T_sublimation = 273.15 - (delta_H_s / (delta_V_s * P))  # K

# 轉換為攝氏度
T_fusion_C = T_fusion - 273.15
T_sublimation_C = T_sublimation - 273.15

# 繪圖
plt.figure(figsize=(10, 6))
plt.plot(T, P_liquid_vapor, label='液-氣平衡', color='blue')
plt.plot(T_fusion_C, P, label='固-液平衡', color='green')
plt.plot(T_sublimation_C, P, label='固-氣平衡', color='red')

plt.yscale('log')
plt.xlabel('溫度 (°C)')
plt.ylabel('壓力 (Pa)')
plt.title('水的相態圖')
plt.legend()
plt.grid(True)
plt.show()
