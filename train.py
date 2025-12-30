import pandas as pd
import numpy as np
from pycaret.regression import setup, compare_models, finalize_model, save_model

print("--- Step 1: Generating Data ---")
df = pd.DataFrame(np.random.randn(100, 10), columns=[f"GENE_{i}" for i in range(10)])
df['IC50'] = 5.0 + (2.0 * df['GENE_1']) - (3.0 * df['GENE_5']) + np.random.normal(0, 0.5, 100)

print("--- Step 2: Training Model ---")
s = setup(data=df, target='IC50', session_id=123, verbose=False)
best = compare_models(n_select=1)

print("--- Step 3: Saving Brain ---")
save_model(finalize_model(best), 'cancer_brain')
print("\nSuccess! 'cancer_brain.pkl' created.")