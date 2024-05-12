import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

try:
    # Load India districts shapefile
    india_districts = gpd.read_file('E:/EDA/Exp07/india_ds.shp')
    
    # Load generated rainfall data
    rainfall_data = pd.read_csv('E:/EDA/Exp07/district_rainfall.csv')
    
    # Ensure the district names match between the shapefile and the rainfall data
    # Assuming 'DISTRICT' is the column in rainfall_data that corresponds to 'DISTRICT' in india_districts
    if 'DISTRICT' not in india_districts.columns or 'District' not in rainfall_data.columns:
        print("Required columns are missing from the datasets")
        exit()

    # Merge the GeoDataFrame with the rainfall data DataFrame on the district name
    map_data = india_districts.set_index('DISTRICT').join(rainfall_data.set_index('District'))

    # Checking for any NaN values in the 'Rainfall' column after the join
    if map_data['Rainfall'].isnull().any():
        print("Warning: Some districts do not have rainfall data and will not be plotted.")
        map_data = map_data.dropna(subset=['Rainfall'])

    # Plotting
    fig, ax = plt.subplots(1, 1, figsize=(12, 12))
    map_data.plot(column='Rainfall', ax=ax, legend=True,
                  legend_kwds={'label': "Rainfall in mm", 'orientation': "horizontal"})
    plt.title('District Wise Rainfall in India')
    plt.show()
except FileNotFoundError as e:
    print(f"File not found: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
