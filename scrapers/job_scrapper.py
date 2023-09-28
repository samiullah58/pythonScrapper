import requests
import json

# This URL should be the internal API endpoint you discover
api_url = "https://www.rolandberger.com/en/Join/All-Jobs/#!?audiences.EN=Consulting%20%E2%80%93%20Internship"

# These headers should mimic the headers your browser sends in the AJAX request
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Host": "www.rolandberger.com",
    "Origin": "https://www.rolandberger.com",
    "Referer": "https://www.rolandberger.com/en/Join/All-Jobs/",
    "Sec-Ch-Ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
    # Add other headers here...
}

response = requests.get(api_url, headers=headers)

print(f"HTTP Status Code: {response.status_code}")
print(f"Server Response: {response.text[:300]}")

if response.status_code == 200:
    try:
        data = json.loads(response.text)
        for job in data["jobs"]:
            print(f"Job Title: {job['title']}")
            print(f"Job URL: {job['url']}")
    except json.JSONDecodeError:
        print("Failed to decode JSON. It's possible that the server did not return JSON data.")
else:
    print("Failed to retrieve data")