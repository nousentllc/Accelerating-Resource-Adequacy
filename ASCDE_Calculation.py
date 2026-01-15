import pandas as pd

# 2026 Tech & Reliability Constants
VOLL = 5000.0
PENETRATION_LEVELS = [0.2, 0.4, 0.6, 0.8]

# Non-linear EUE (MWh) growth without ARQ
eue_status_quo = {0.2: 500, 0.4: 3000, 0.6: 12000, 0.8: 50000}
eue_arq = {0.2: 100, 0.4: 300, 0.6: 800, 0.8: 2500}

def get_ascde(eue, penetration, load=1e6):
    # Simplified cost model: VRE cost vs Gas cost
    gen_cost = (penetration * 38.0 + (1-penetration) * 45.0) * load
    reliability_cost = eue * VOLL
    return (gen_cost + reliability_cost) / (load - eue)

results = []
for p in PENETRATION_LEVELS:
    sq = get_ascde(eue_status_quo[p], p)
    arq = get_ascde(eue_arq[p], p)
    results.append({'VRE %': p*100, 'SQ_ASCDE': sq, 'ARQ_ASCDE': arq})

df_ascde = pd.DataFrame(results)
print(df_ascde)