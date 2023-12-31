import requests
import json

url = "https://www.lapakgaming.com/api-ms/order/transactions"

# Define the payload
payload = {
    "paymentMethod": "DANA_DI",
    "productCode": "MLBB9_1-S10",
    "forms": {
        "user_id": "688700997",
        "additional_id": "8742"
    },
    "email": "",
    "phoneNumber": "",
    "count": 1,
    "source": "",
    "campaign": "",
    "medium": "",
    "orderDetail": "",
    "additionalInformation": "",
    "promoCode": "",
    "productId": "11418"
}

# Convert payload to JSON
payload_json = json.dumps(payload)

# Set headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Content-Type": "application/json",
    # Add any other headers as needed
}

# Make the POST request
response = requests.post(url, data=payload_json, headers=headers)

if response.status_code == 200:
    print("Request successful!")
    
    # Parse JSON response
    json_response = response.json()
    
    # Extract and print specific information
    print("status code:", json_response["statusCode"])
    print("message:", json_response["message"])
    print("data:", json_response["data"])
    
else:
    print(f"Request failed with status code {response.status_code}")
    print("Response content:")
    print(response.text)
