# import requests

# responses = requests.get('http://127.0.0.1:8000/movies/')
# for response in responses.json():
#     print(response)

import requests
import hashlib
import time

# Replace these values with your own public and private keys
public_key = "8de5cd2b5218c35d18b29424c4209e9d"
private_key = "4f0df15f3f5f67e6abdd7f0e03dcada0389b5114"

# Example API endpoint
base_url = "https://gateway.marvel.com/v1/public/characters"
character_id = 1009610  # Spider-Man's character ID
# Generate timestamp
ts = str(int(time.time()))

# Generate hash
hash_str = ts + private_key + public_key
hash_value = hashlib.md5(hash_str.encode()).hexdigest()

# Construct the request URL with authentication parameters
url = f"{base_url}/{character_id}?apikey={public_key}&hash={hash_value}&ts={ts}"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Handle the data as needed
    print(data)
else:
    print("Error:", response.status_code)
