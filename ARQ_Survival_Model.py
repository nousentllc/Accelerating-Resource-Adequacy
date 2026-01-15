import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.special import gamma

# 2026 Empirical Parameters derived from LBNL Data
iso_params = {
    'PJM':   {'k': 0.860, 'eta': 5.61},
    'CAISO': {'k': 0.736, 'eta': 4.71},
    'MISO':  {'k': 0.897, 'eta': 12.00}
}

def survival_func(t, k, eta):
    return np.exp(-(t / eta)**k)

def compute_entropy(k, eta):
    # Survival Entropy (Sr) - measure of outcome concentration
    euler_gamma = 0.5772
    return (1 - 1/k) * euler_gamma + np.log(eta/k) + 1

t_range = np.linspace(0, 15, 100)
plt.figure(figsize=(10, 6))

for iso, p in iso_params.items():
    # Baseline
    s_vals = survival_func(t_range, p['k'], p['eta'])
    plt.plot(t_range, s_vals, label=f"{iso} Baseline (k={p['k']})")
    
    # ARQ Scenario (Simulating k shift toward 1.0 and higher eta)
    s_arq = survival_func(t_range, 1.1, 15.0) 
    
plt.plot(t_range, survival_func(t_range, 1.1, 15.0), 'k--', label="ARQ Target Scenario")
plt.title("2026 Interconnection Queue Survival Model")
plt.xlabel("Years in Queue")
plt.ylabel("Retention Probability S(t)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()