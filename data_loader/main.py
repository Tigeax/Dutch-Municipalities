import requests
import geopandas


def post_to_api(file_path, api_endpoint):
    """
    Reads a GeoJSON file, extracts relevant data, and sends POST requests 
    to a specified API endpoint for each entry in the dataset.

    Args:
        file_path (str): Path to the GeoJSON file containing geographic data.
        api_endpoint (str): URL of the API endpoint to which data will be posted.
    """
    
    gdf = geopandas.read_file(file_path)

    # Iterate over each entry in the json data.
    for _, row in gdf.iterrows():

        print(row['geometry'].wkt)

        # Parse the geojson data to a format the API understands.
        data = {
            'name': row['name'],
            'geometry': row['geometry'].wkt
        }

        # Send the POST request to the API and handle any errors.
        try:
            response = requests.post(api_endpoint, data=data)
            
            if response.status_code == 201:
                print(f"Successfully posted {row['name']}")
            else:
                print(f"Failed to post {row['name']}. Status code: {response.status_code}")
                print(f"Response: {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"Error sending the request: {e}")


if __name__ == "__main__":
    post_to_api("municipalities_nl.geojson", "http://localhost/api/municipality/")