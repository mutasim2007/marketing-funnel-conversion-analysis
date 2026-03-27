# =============================
# Marketing Funnel & Conversion Analysis
# =============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Generate Sample Dataset
# -----------------------------
np.random.seed(42)

n = 500

data = pd.DataFrame({
    'User_ID': range(1, n + 1),
    'Lead_Source': np.random.choice(['Organic', 'Paid Ads', 'Referral', 'Social Media'], n),
    'Visits': np.random.randint(1, 10, n),
    'Pages_Viewed': np.random.randint(1, 20, n),
    'Time_Spent_Minutes': np.random.randint(1, 60, n),
    'Converted': np.random.choice([0, 1], n, p=[0.7, 0.3])
})

# Save dataset
data.to_csv('marketing_data.csv', index=False)

print("Dataset created successfully!\n")
print(data.head())

# -----------------------------
# 2. Conversion Rate
# -----------------------------
conversion_rate = data['Converted'].mean() * 100
print(f"\nOverall Conversion Rate: {conversion_rate:.2f}%")

# -----------------------------
# 3. Conversion by Lead Source
# -----------------------------
conversion_by_source = data.groupby('Lead_Source')['Converted'].mean() * 100
print("\nConversion Rate by Lead Source:\n", conversion_by_source)

# -----------------------------
# 4. Funnel Approximation
# -----------------------------
total_users = len(data)
visited = data['Visits'].gt(0).sum()
engaged = data['Pages_Viewed'].gt(5).sum()
converted = data['Converted'].sum()

funnel = pd.Series({
    'Total Users': total_users,
    'Visited': visited,
    'Engaged': engaged,
    'Converted': converted
})

print("\nFunnel Stages:\n", funnel)

# -----------------------------
# 5. Drop-off Calculation
# -----------------------------
drop_off = funnel.pct_change() * -100
print("\nDrop-off Percentages:\n", drop_off)

# -----------------------------
# 6. Visualizations
# -----------------------------

# Conversion by Source
plt.figure()
conversion_by_source.plot(kind='bar', title='Conversion Rate by Lead Source')
plt.xlabel('Lead Source')
plt.ylabel('Conversion Rate (%)')
plt.show()

# Funnel Visualization
plt.figure()
funnel.plot(kind='bar', title='Marketing Funnel')
plt.ylabel('Number of Users')
plt.show()

print("\nAnalysis Completed Successfully!")
