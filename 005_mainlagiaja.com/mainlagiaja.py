

import requests, json

url = "https://mainlagiaja.com/ajax/games/check/mobile-legend"
params = {
    "user_id": "68870099",
    "zone_id": "8742"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    # Add any other headers as needed
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    print("Request successful!")
    json_response = response.text()
    print(json_response)
else:
    print(f"Request failed with status code {response.status_code}")
    print("Response content:")
    json_response = response.text()
    print(json_response)
