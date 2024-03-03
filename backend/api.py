import requests

def simplify_event_data(event):
    simplified_event = {
        "name": event["name"],
        "url": event["url"],
        "date": event["dates"]["start"]["localDate"],
        "time": event["dates"]["start"]["localTime"],
        "venue": {
            "name": event["_embedded"]["venues"][0]["name"],
            "city": event["_embedded"]["venues"][0]["city"]["name"],
            "state": event["_embedded"]["venues"][0]["state"]["name"],
            "country": event["_embedded"]["venues"][0]["country"]["name"]
        },
        "image_url": event["images"][0]["url"] if event["images"] else None
    }
    return simplified_event

def make_api_call(api_key):
    url = f'https://app.ticketmaster.com/discovery/v2/events.json?countryCode=US&apikey={api_key}&size={10}&pages={1}'
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            simplified_events = [simplify_event_data(event) for event in data["_embedded"]["events"]]
            return simplified_events
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

api_key = 'a7ZZ3PEKgvGkg54s5nr6j6qKg9QdVcvW'
simplified_data = make_api_call(api_key)
if simplified_data:
    for i in range(len(simplified_data)):
        print(f"{i}: {simplified_data[i]}\n")
        
else:
    print("Failed to fetch API data.")
