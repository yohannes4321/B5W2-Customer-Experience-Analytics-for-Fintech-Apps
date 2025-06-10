import cx_Oracle
import pandas as pd

# Connection details
dsn_tns = cx_Oracle.makedsn('localhost', 1521, service_name='XE')  # Adjust if needed
conn = cx_Oracle.connect(user='bank_reviews_user', password='your_password', dsn=dsn_tns)

cursor = conn.cursor()

# Example: inserting data for Banks
banks_data = [
    ('Bank of America', 'New York, NY', 1910),
    ('Chase Bank', 'New York, NY', 1877),
    ('Wells Fargo', 'San Francisco, CA', 1852),
    # Add more banks as needed
]

# Insert banks
for name, location, year in banks_data:
    cursor.execute(
        """
        INSERT INTO Banks (name, location, established_year)
        VALUES (:name, :location, :year)
        """,
        name=name,
        location=location,
        year=year
    )

conn.commit()

# Fetch bank_ids for inserting reviews
cursor.execute("SELECT bank_id, name FROM Banks")
bank_map = {name: bank_id for bank_id, name in cursor.fetchall()}

# Example: inserting reviews
reviews_data = [
    {
        'bank_name': 'Bank of America',
        'reviewer_name': 'Alice',
        'review_text': 'Great customer service.',
        'review_date': '2023-10-01',
        'rating': 4.5
    },
    {
        'bank_name': 'Chase Bank',
        'reviewer_name': 'Bob',
        'review_text': 'Nice online banking features.',
        'review_date': '2023-09-15',
        'rating': 4.0
    },
    # Add more reviews to reach >1000 entries
]

# Insert reviews
for review in reviews_data:
    bank_id = bank_map.get(review['bank_name'])
    if bank_id:
        cursor.execute(
            """
            INSERT INTO Reviews (bank_id, reviewer_name, review_text, review_date, rating)
            VALUES (:bank_id, :reviewer_name, :review_text, TO_DATE(:review_date, 'YYYY-MM-DD'), :rating)
            """,
            bank_id=bank_id,
            reviewer_name=review['reviewer_name'],
            review_text=review['review_text'],
            review_date=review['review_date'],
            rating=review['rating']
        )

conn.commit()

# Close connection
cursor.close()
conn.close()
