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

    # Clear the result text widget
    result_text.delete("1.0", tk.END)

    # Extract the relevant information from the response and insert the results into the text widget
    for result in response_json["items"]:
        result_text.insert(tk.END, result["title"] + "\n")
        result_text.insert(tk.END, result["link"] + "\n")
        result_text.insert(tk.END, result["displayLink"] + "\n\n")

# Create the GUI
root = tk.Tk()
root.title("Students Search Engine")

# Create the search label and entry
search_label = tk.Label(root, text="Search:", height=5, width=50)
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()

# Create the search button
search_button = tk.Button(root, text="Search", command=search)
search_button.pack()

# Create the scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create the result text widget
result_text = tk.Text(root, yscrollcommand=scrollbar.set)
result_text.pack()

# Attach the scrollbar to the result text widget
scrollbar.config(command=result_text.yview)

# Run the GUI
root.mainloop()
