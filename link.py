import requests
import json
import tkinter as tk

def search():
    # Set up the Google Custom Search API endpoint and parameters
    endpoint = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": search_entry.get(),
        "cx": "97841aee915c844ae",
        "key": "AIzaSyB1NODmSr3zAAfaksOEDBxaxAOLPJIeI1o",
        "num": 10,  # Number of results to return
        "fields": "items(title,link,displayLink)"  # Only include title, link, and displayLink fields in the response
    }

    # Make a request to the API and parse the response
    response = requests.get(endpoint, params=params)
    response_json = json.loads(response.text)

    # Clear the result label
    result_label.config(text="")

    # Extract the relevant information from the response and print the results
    for result in response_json["items"]:
        result_label.config(text=result_label.cget("text") + result["title"] + "\n")
        result_label.config(text=result_label.cget("text") + result["link"] + "\n")
        result_label.config(text=result_label.cget("text") + result["displayLink"] + "\n\n")

# Create the GUI
root = tk.Tk()
root.title("Google Custom Search API")

# Create the search label and entry
search_label = tk.Label(root, text="Search:", height=5, width=50)
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()

# Create the search button
search_button = tk.Button(root, text="Search", command=search)
search_button.pack()

# Create the result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the GUI
root.mainloop()
