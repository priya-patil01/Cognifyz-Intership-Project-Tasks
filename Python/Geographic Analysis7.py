import pandas as pd
import folium
from folium.plugins import MarkerCluster
import webbrowser

# Step 1: Load the dataset
file_path = r"C:\Users\priya\Downloads\Dataset .csv"
df = pd.read_csv(file_path)

# Step 2: Drop rows without Latitude or Longitude
df_geo = df.dropna(subset=['Latitude', 'Longitude']).copy()
print("✅ Valid restaurant locations:", len(df_geo))

# Optional: Check if there's data to plot
if df_geo.empty:
    print("⚠️ No valid location data to plot.")
else:
    # Step 3: Create a base map (centered on India or average location)
    map_center = [df_geo['Latitude'].mean(), df_geo['Longitude'].mean()]
    map_obj = folium.Map(location=map_center, zoom_start=5)

    # Step 4: Add a cluster of markers
    marker_cluster = MarkerCluster().add_to(map_obj)

    for _, row in df_geo.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=row['City']
        ).add_to(marker_cluster)

    # Step 5: Save and open map
    output_file = "restaurant_map.html"
    map_obj.save(output_file)
    print(f"✅ Map saved as '{output_file}'. Opening in your browser...")
    webbrowser.open(output_file)
