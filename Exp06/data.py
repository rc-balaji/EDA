from faker import Faker
import pandas as pd
import random

fake = Faker()

# Function to generate fake data with day and night categorization
def generate_data(num):
    data = []
    for _ in range(num):
        if random.choice([True, False]):  # Daytime: 6 AM to 6 PM
            time = fake.date_time_between(start_date='-5y', end_date='now').replace(hour=random.randint(6, 18))
            period = 'Day'
        else:  # Nighttime: 7 PM to 5 AM
            if random.choice([True, False]):
                hour = random.randint(19, 23)  # Hours from 7 PM to 11 PM
            else:
                hour = random.randint(0, 5)  # Hours from 12 AM to 5 AM
            time = fake.date_time_between(start_date='-5y', end_date='now').replace(hour=hour)
            period = 'Night'

        data.append({
            "latitude": fake.latitude(),
            "longitude": fake.longitude(),
            "description": fake.sentence(),
            "date_time": time,
            "period": period
        })
    return pd.DataFrame(data)

# Generate 100 fake crime records
df = generate_data(100)
df.to_csv('crime_data.csv', index=False)
print("Data generated and saved successfully.")
