import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
n_samples = 100
rd_spend = np.random.normal(70000, 30000, n_samples)
admin_spend = np.random.normal(100000, 20000, n_samples)
marketing_spend = np.random.normal(200000, 50000, n_samples)
states = np.random.choice(['New York', 'California', 'Florida'], n_samples)

# Calculate profit based on linear relationship with some noise
# Profit = 0.8 * R&D + 0.05 * Admin + 0.1 * Marketing + Noise
profit = 0.8 * rd_spend + 0.05 * admin_spend + 0.1 * marketing_spend + np.random.normal(0, 5000, n_samples)

# Create DataFrame
data = {
    'R&D Spend': np.abs(rd_spend),
    'Administration': np.abs(admin_spend),
    'Marketing Spend': np.abs(marketing_spend),
    'State': states,
    'Profit': np.abs(profit)
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('dataset/startup_data.csv', index=False)
print("Synthetic dataset created at dataset/startup_data.csv")
