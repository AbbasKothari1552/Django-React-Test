import requests

def get_lat_lng(address):
    base_url = "https://geocode.maps.co/search"
    params = {
        "q": address,
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            location = data[0]  # Assuming the first result is the most relevant
            return location['lat'], location['lon']
        else:
            print("Error: No results found")
            return None, None
    else:
        print("Error in the HTTP request:", response.status_code)
        return None, None
