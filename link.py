import requests
import json

# Set up the Google Custom Search API endpoint and parameters
endpoint = "https://www.googleapis.com/customsearch/v1"
params = {
    "q": "cloud computing",
    "cx": "97841aee915c844ae",
    "key": " AIzaSyB1NODmSr3zAAfaksOEDBxaxAOLPJIeI1o",
    "num": 10,  # Number of results to return
    "fields": "items(title,link,displayLink)"  # Only include title, link, and displayLink fields in the response
}

# Make a request to the API and parse the response
response = requests.get(endpoint, params=params)
response_json = json.loads(response.text)

# Extract the relevant information from the response and print the results
for result in response_json["items"]:
    print(result["title"])
    print(result["link"])
    print(result["displayLink"])
    print()