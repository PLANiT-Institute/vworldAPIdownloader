import requests
import geopandas as gpd
import pandas as pd
from shapely.geometry import shape
import json

list_df = pd.read_excel("DBlist.xlsx")
list_df = list_df[list_df['select'] == 1]

result_dt = {"success": [], "failed": []}

for id in list(list_df['code']):

    try:
        print(f"Getting data from Vworld API: {id}")

        apiurl = "https://api.vworld.kr/req/data?"
        params = {
            "service": "data",
            "data": id,
            "request": "GetFeature",
            "geomFilter": "BOX(120,30,140,40)",
            "key": "22908348-FB4C-3271-B2DC-B26C7EAB221C",
            "size": "1000",
            "page": "1"  # Start with the first page
        }

        all_features = []

        while True:
            response = requests.get(apiurl, params=params)
            if response.status_code == 200:
                page_data = response.json()['response']
                features = page_data['result']['featureCollection']['features']
                all_features.extend(features)
                print(f"Page {page_data['page']} processed.")

                # Check if there is another page
                if int(page_data['page']['current']) >= int(page_data['page']['total']):
                    break
                else:
                    params['page'] = str(int(params['page']) + 1)
            else:
                print("Error:", response.status_code, response.text)
                break

        if all_features:
            # Convert features to GeoDataFrame
            geometries = [shape(feature['geometry']) for feature in all_features]
            properties = [feature['properties'] for feature in all_features]

            gdf = gpd.GeoDataFrame(properties, geometry=geometries, crs="EPSG:4326")

            # Reproject to EPSG:5186
            gdf_5186 = gdf.to_crs(epsg=5186)

            # Save to GeoPackage

            gdf_5186.to_file('downloaded/' + params['data'] + ".gpkg", driver='GPKG')

            print("GPKG created successfully.")
        else:
            print("No features retrieved.")

        result_dt["success"].append(id)

    except Exception as e:
        print(e)
        result_dt["failed"].append(id)

