import requests

access_token = 'OTFkNmY1ZmEtMzBhNi00YzYxLTkxMjgtYjQwN2E5MGMxNDFjZDBkZmI0NzEtNTEz_P0A1_d753f5ed-fc6f-453b-b80d-9eed175c690b'

# Function to test connection with Webex server
def test_connection():
    url = 'https://webexapis.com/v1/people/me'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Connection with Webex server is successful.")
    else:
        print("Connection with Webex server failed.")
    
    input("Press Enter to return to the menu...")

# Function to get user details
def get_user_details():
    url = 'https://webexapis.com/v1/people/me'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
     
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        print("User Information: ")
        print(f"Display Name: {user_data['displayName']}")
        print(f"Nickname: {user_data['nickName']}")
        print(f"Emails: {', '.join(user_data['emails'])}")
    else:
        print("Failed to fetch user details.")
    
    input("Press Enter to return to the menu...")

# Function to list rooms
def list_rooms():
    url = 'https://webexapis.com/v1/rooms'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        rooms = response.json()
        print("\nList of Rooms:")
        for i, room in enumerate(rooms['items']):
            print(f"Room {i + 1}:")
            print(f"Room ID: {room['id']}")
            print(f"Room Title: {room['title']}")
            print(f"Date Created: {room['created']}")
            print(f"Last Activity: {room['lastActivity']}")
            print()
    else:
        print("Failed to fetch room details.")
    
    input("Press Enter to return to the menu...")

# Function to create a room
def create_room():
    url = 'https://webexapis.com/v1/rooms'
    title = input("Enter the title for the new room: ")
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    data = {
        "title": title
    }
    
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        room_data = response.json()
        print("Room created successfully!")
        print(f"Room ID: {room_data['id']}")
        print(f"Room Title: {room_data['title']}")
    else:
        print("Failed to create the room.")
    
    input("Press Enter to return to the menu...")

# Function to send a message to a room
def send_message():
    url = 'https://webexapis.com/v1/messages'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    
    response = requests.get('https://webexapis.com/v1/rooms', headers=headers)
    if response.status_code == 200:
        rooms = response.json()
        print("\nList of Rooms:")
        for i, room in enumerate(rooms['items']):
            print(f"Room {i + 1}:")
            print(f"Room ID: {room['id']}")
            print(f"Room Title: {room['title']}")
            print()
        
        room_index = int(input("Enter the room number to send a message (1-5): ")) - 1
        if room_index < 0 or room_index >= len(rooms['items']):
            print("Invalid room selection.")
            return
        
        room_id = rooms['items'][room_index]['id']
        message = input("Enter the message to send: ")
        data = {
            "roomId": room_id,
            "text": message
        }
        
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print("Failed to send the message.")
    
    input("Press Enter to return to the menu...")

while True:
    print("\nMain Menu:")
    print("0. Test Connection with Webex Server")
    print("1. Display User Information")
    print("2. List Rooms")
    print("3. Create a Room")
    print("4. Send Message to a Room")
    print("5. Quit")
    
    choice = input("Select an option (0/1/2/3/4/5): ")
    
    if choice == "0":
        test_connection()
    elif choice == "1":
        get_user_details()
    elif choice == "2":
        list_rooms()
    elif choice == "3":
        create_room()
    elif choice == "4":
        send_message()
    elif choice == "5":
        print("Exiting the application.")
        break
    else:
        print("Invalid option. Please select a valid option.")
