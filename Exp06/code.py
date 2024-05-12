import folium
import pandas as pd

# Load the generated fake data
df = pd.read_csv('crime_data.csv')

# Create a map centered around an average location
m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=5)

# Define marker colors for day and night
colors = {
    'Day': 'blue',
    'Night': 'darkblue'
}

# Add points to the map
for idx, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"<strong>Date and Time:</strong> {row['date_time']}<br><strong>Period:</strong> {row['period']}<br><strong>Description:</strong> {row['description']}",
        tooltip=row['description'],
        icon=folium.Icon(color=colors[row['period']])
    ).add_to(m)

# Save to HTML file
m.save('map.html')
