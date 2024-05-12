import pandas as pd
from faker import Faker
import random

fake = Faker()

def generate_emails(num=150):
    categories = ['Sent', 'Inbox', 'Spam', 'Waiting', 'Outbox']
    data = []
    for _ in range(num):
        data.append({
            'email': fake.email(),
            'category': random.choice(categories),
            'subject': fake.sentence(nb_words=6),
            'body': fake.text(max_nb_chars=200),
            'date': fake.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S')
        })
    return data

# Generate email data
email_data = generate_emails()

# Convert to DataFrame
df_emails = pd.DataFrame(email_data)

# Save to CSV
df_emails.to_csv('email_categories_dataset.csv', index=False)
