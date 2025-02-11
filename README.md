Vworld API Data Fetcher
Overview
This repository provides a Python script to fetch geospatial data from the Vworld API, process the retrieved data, and save it as a GeoPackage (GPKG) file. The script efficiently handles multi-page API responses, transforms coordinate reference systems, and logs successful and failed requests.

Features
Automated API Data Retrieval: Fetches spatial data from Vworld API.
Multi-Page Handling: Supports large datasets by iterating through paginated API responses.
GeoDataFrame Processing: Converts API responses into a structured GeoDataFrame.
Coordinate System Transformation: Reprojects data from EPSG:4326 to EPSG:5186.
GeoPackage Export: Saves processed data as a GPKG file for GIS applications.
Error Handling & Logging: Captures failed API requests and logs results.
Installation
To use this repository, clone it and install the required dependencies:

sh
Copy
Edit
# Clone the repository
git clone https://github.com/YOUR_GITHUB/vworld-api-fetcher.git
cd vworld-api-fetcher

# Install dependencies
pip install -r requirements.txt
Usage
Running the Script
To execute the script and fetch geospatial data:

sh
Copy
Edit
python fetch_vworld_data.py
Configuration
The script reads from an Excel file (DBlist.xlsx), which contains:

Dataset codes (code column) for API requests.
Selection column (select) where 1 indicates datasets to fetch.
Example structure of DBlist.xlsx:

code	select
dataset_1	1
dataset_2	0
dataset_3	1
Key Components
fetch_vworld_data.py
Reads dataset list from DBlist.xlsx.
Requests data from Vworld API and processes multi-page responses.
Converts JSON response into a GeoDataFrame using geopandas.
Reprojects coordinates to EPSG:5186 for GIS compatibility.
Saves the final dataset as a GeoPackage (.gpkg).
Example Output
Upon successful execution, results are saved in the downloaded/ directory:

GeoPackages (.gpkg) for each dataset.
failed.txt logs datasets that failed to download.
Contributing
We welcome contributions to improve this repository! Please follow these steps:

Fork the repository.
Create a feature branch (git checkout -b feature-new).
Commit your changes (git commit -m "Added new feature").
Push to your fork (git push origin feature-new).
Submit a pull request.
License
This project is licensed under the GNU General Public License v3.0.

Contact
For inquiries or collaboration, please contact: sanghyun@planit.institute
