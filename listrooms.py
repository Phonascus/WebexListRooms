import requests
import base64

# Replace 'YOUR_PERSONAL_ACCESS_TOKEN' with your actual personal access token
access_token = 'YOUR_PERSONAL_ACCESS_TOKEN'

# The headers for the HTTP requests
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Function to handle API pagination and return all items
def get_all_items(url):
    items = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            items.extend(data.get('items', []))
            # Check for a 'next' link in the response
            url = data.get('next')
        else:
            print(f"Failed to retrieve items: {response.status_code} - {response.text}")
            break
    return items

# List all rooms the user is a member of
rooms_url = 'https://webexapis.com/v1/rooms?type=group&sortBy=lastactivity&max=1000'
all_my_rooms = get_all_items(rooms_url)

# Open the files to write the output
with open('WebexSpaces.txt', 'w') as txt_file, open('WebexSpaces.csv', 'w') as csv_file:
    # Process and write room details for all rooms the user is a member of
    for room in all_my_rooms:
        room_name = room.get('title')
        room_id_encoded = room.get('id')
        if room_id_encoded:
            # Decode and extract the UUID
            decoded_uri = base64.b64decode(room_id_encoded).decode('utf-8')
            uuid = decoded_uri.split('/')[-1]
            app_deep_link = f"webexteams://im?space={uuid}"
            # Write to the text file
            txt_file.write(f"Space Name: {room_name}\n")
            txt_file.write(f"Space Link: {app_deep_link}\n\n")
            # Write to the csv file
            csv_file.write(f"{room_name}\t{app_deep_link}\n")
        else:
            # Write to the text file
            txt_file.write(f"Space Name: {room_name} (No space ID available)\n\n")
            # Write to the csv file
            csv_file.write(f"room_name\n")

print("The output has been saved to WebexSpaces.txt and WebexSpaces.csv")
