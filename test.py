import pandas as pd

# Sample data
data = {
    'arrest_id': [1, 2, 3, 4],
    'charge_degree': ['felony', 'misdemeanor', 'felony', 'misdemeanor'],
    'prediction_felony': [0.8, 0.3, 0.6, 0.4],
    'prediction_nonfelony': [0.2, 0.7, 0.4, 0.6]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('./data/pred_universe.csv', index=False)

data = {
    'charge_degree': ['felony', 'misdemeanor'],
    'count': [120, 80]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('./data/charge_counts.csv', index=False)

data = {
    'offense_category': ['theft', 'assault', 'theft', 'assault'],
    'charge_degree': ['felony', 'felony', 'misdemeanor', 'misdemeanor'],
    'count': [50, 30, 40, 20]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('./data/charge_counts_by_offense.csv', index=False)
