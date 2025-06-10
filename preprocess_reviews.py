import pandas as pd

# Load raw data
df = pd.read_csv('raw_reviews.csv')

# Remove duplicates
df.drop_duplicates(subset=['review'], inplace=True)

# Handle missing data
df.dropna(subset=['review', 'rating', 'date'], inplace=True)

# Normalize date format to YYYY-MM-DD
# Assuming date is in a string format, convert accordingly
def normalize_date(date_str):
    try:
        return pd.to_datetime(date_str).strftime('%Y-%m-%d')
    except:
        return None

df['date'] = df['date'].apply(normalize_date)

# Remove rows with invalid dates
df.dropna(subset=['date'], inplace=True)

# Save cleaned data
df.to_csv('clean_reviews.csv', index=False)
print("Cleaned reviews saved to 'clean_reviews.csv'")
