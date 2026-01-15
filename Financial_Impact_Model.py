import numpy as np

def run_npv_sim(delay_years, simulations=1000):
    # 100MW Project Constants
    capex = 118_000_000  # $118M
    annual_revenue = 15_000_000
    wacc_base = 0.08
    
    # Monte Carlo on WACC and Revenue
    npvs = []
    for _ in range(simulations):
        # Apply 50-150bps risk premium for long delays
        risk_premium = 0.01 if delay_years > 3 else 0.0
        r = np.random.normal(wacc_base + risk_premium, 0.005)
        
        # Simple NPV: Revenue starts after delay
        cash_flows = [-capex] + [0]*int(delay_years) + [annual_revenue]*25
        npv = sum([cf / (1+r)**t for t, cf in enumerate(cash_flows)])
        npvs.append(npv)
    return np.array(npvs)

# Compare 4.75y (CAISO) vs 2.0y (ARQ)
baseline_npv = run_npv_sim(4.75)
arq_npv = run_npv_sim(2.0)

print(f"Baseline Median NPV: ${np.median(baseline_npv)/1e6:.2f}M")
print(f"ARQ Median NPV: ${np.median(arq_npv)/1e6:.2f}M")
print(f"Value Preserved: ${(np.median(arq_npv) - np.median(baseline_npv))/1e6:.2f}M")