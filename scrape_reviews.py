import pandas as pd
from google_play_scraper import reviews, Sort
import time

# List of apps with their identifiers
apps = {
    'CBE': 'com.cbe.mobile',             # Example package name, replace with actual
    'BOA': 'com.bankofabyssinia',        # Placeholder, replace with real package
    'Dashen': 'com.dashenbank'           # Placeholder, replace with real package
}

# Number of reviews to fetch per app
REVIEWS_PER_APP = 400

# Function to scrape reviews
def scrape_app_reviews(app_name, app_package, count=400):
    all_reviews = []
    # Google Play reviews are paginated; use 'continuation_token' to fetch subsequent pages
    next_token = None
    while len(all_reviews) < count:
        result, continuation_token = reviews(
            app_package,
            lang='en',
            country='ET',  # Ethiopia
            sort=Sort.NEWEST,
            count=min(100, count - len(all_reviews)),
            continuation_token=next_token
        )
        all_reviews.extend(result)
        if not continuation_token:
            break
        next_token = continuation_token
        time.sleep(1)  # To respect rate limits
    return all_reviews

# Collect reviews for all apps
all_data = []

for bank, package_name in apps.items():
    print(f"Scraping reviews for {bank}...")
    reviews = scrape_app_reviews(bank, package_name, REVIEWS_PER_APP)
    for r in reviews:
        data = {
            'review': r['content'],
            'rating': r['score'],
            'date': r['date'],
            'bank': bank,
            'source': 'Google Play'
        }
        all_data.append(data)

# Save raw data to CSV
df = pd.DataFrame(all_data)
df.to_csv('raw_reviews.csv', index=False)
print("Reviews saved to 'raw_reviews.csv'")
