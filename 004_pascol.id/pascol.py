import requests, json

url = "https://xc-api.pascol.id/order/prepare/Mobile%20Legend"
params = {
    "userId": "688700997",
    "zoneId": "8742"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    # Add any other headers as needed
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    print("Request successful!")
    json_response = response.json()
    print("status code:", json_response["statusCode"])
    print("message:", json_response["message"])
    print("data:", json_response["data"])
else:
    print(f"Request failed with status code {response.status_code}")
    print("Response content:")
    json_response = response.json()
    print("status code:", json_response["statusCode"])
    print("message:", json_response["message"])
