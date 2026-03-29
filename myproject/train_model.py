import pandas as pd
import numpy as np
from lifelines import CoxPHFitter
import pickle

# --- Create synthetic dataset ---
np.random.seed(42)

n = 50

df = pd.DataFrame({
    'time': np.random.randint(5, 50, n),
    'event': np.random.choice([0, 1], n),
    'age': np.random.randint(40, 80, n),
    'stage': np.random.choice([1, 2, 3, 4], n),
    'grade': np.random.choice([1, 2, 3], n),
    'glycan1': np.random.normal(1.5, 0.5, n),
    'glycan2': np.random.normal(2.0, 0.6, n)
})

# --- Train Cox model ---
cph = CoxPHFitter()
cph.fit(df, duration_col='time', event_col='event')

# --- Save model (IMPORTANT: wb mode) ---
with open("cox_model.pkl", "wb") as f:
    pickle.dump(cph, f)

print("✅ Model trained and saved as cox_model.pkl")