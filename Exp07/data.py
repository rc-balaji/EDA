import pandas as pd
import random

# List of some districts in India (can be expanded with actual district names)
districts = ["Mumbai", "Pune", "Nagpur", "Bhopal", "Indore", "Jaipur", "Udaipur", "Lucknow", "Kanpur", "Patna", "Ranchi", "Kolkata", "Guwahati", "Bhubaneswar", "Chennai", "Bengaluru", "Hyderabad", "Kochi"]

# Generate random rainfall data for these districts
data = {
    "District": districts,
    "Rainfall": [random.uniform(100, 900) for _ in districts]  # Rainfall in mm
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("district_rainfall.csv", index=False)
print("Data generated and saved to 'district_rainfall.csv'")
