# Fintech App Reviews Data Collection & Preprocessing

## Overview
This project collects user reviews from the Google Play Store for three Ethiopian bank apps: CBE, BOA, and Dashen Bank. The reviews are scraped using `google-play-scraper`, then cleaned and prepared for analysis.

## Data Collection
- Used `google-play-scraper` to fetch at least 400 reviews per app.
- Targeted reviews in English, from Ethiopia.
- Extracted review content, ratings, and review dates.

## Data Preprocessing
- Removed duplicates and missing data.
- Normalized review dates to YYYY-MM-DD format.
- Saved cleaned data as `clean_reviews.csv`.

## Future Steps
- Sentiment analysis
- Theme extraction
- Storage in Oracle database
- Visualization and reporting
