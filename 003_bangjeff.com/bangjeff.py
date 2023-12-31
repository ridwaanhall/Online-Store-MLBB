import requests

url = "https://api.bangjeff.com/v3/inquiry/user"
headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,mt;q=0.8",
    "Cache-Control": "no-cache",
    "Content-Length": "231",
    "Content-Type": "application/json",
    "Dnt": "1",
    "Origin": "https://www.bangjeff.com",
    "Pragma": "no-cache",
    "Referer": "https://www.bangjeff.com/",
    "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "X-Bangjeff-Key": "220c50ac20733f2469ad6e83709df8cb",
    "X-Request-Time": "2023-12-31 18:14:33",
    # Add other headers as needed
}

payload = {
    "paymentCode": "BJPAY03-DANA",
    "phoneNumber": "628121212121",
    "variantId": 13630,
    "quantity": 1,
    "inputs": [
        {"name": "id", "value": "688700997"},
        {"name": "server", "value": "8742"}
    ],
    "promo": "",
    "token": "",
    "referer": "https://www.bing.com/",
    "r": ""
}

try:
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)
    print("Response status code:", response.status_code)
    print("Response content:", response.text)  # Print raw response content
except requests.exceptions.RequestException as e:
    print("Request failed with error:", e)
