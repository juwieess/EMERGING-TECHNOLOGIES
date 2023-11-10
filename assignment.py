#Import
from webexteamssdk import WebexTeamsAPI

#Input Webex Teams API access token and create an instance of the WebexTeamsAPI class with provided access token
teams_token = input ("Enter your access token: ")
api = WebexTeamsAPI(access_token=teams_token)

#Test connection to Webex Teams
def Test_Connection():
    print ("connecting...")
    webex = api.people.me()
    if webex:
        print("Successful!")

#Display information about authenticated users
def information():
    webex = api.people.me()
    print(f"Name:  {webex.displayName}")
    print(f"Nickname: {webex.nickName}")
    print(f"Email: {','.join(webex.emails)}")

#Display list of rooms
def displayRoom():
    print("List of Rooms: ")
    rooms = api.rooms.list(max=5)
    roomCount = 0

    for room in rooms:
        print(f"Room ID : {room.id}")
        print(f"Room Title : {room.title}")
        print(f"Date Created  : {room.created}")
        print(f"Last Activity : {room.lastActivity}\n")

        roomCount += 1
        if roomCount >= 5:
            break

#Create new room
def createRoom():
    titleRoom = input("Enter the title of the new room: ")
    dataRoom = {"title": titleRoom}
    try:
        new_room = api.rooms.create(titleRoom)
        print(f"Room '{new_room.title}' (Room ID: {new_room.id}) has been created successfully.")
    except api:
        print(f"Failed to create the room.") 

#Send message to selected room
#Import the ApiError class
from webexteamssdk import ApiError
def sendMessage():
  print("\nList of Rooms:")

  room_list = list(api.rooms.list(max=5))

  for i, room in enumerate(room_list):
    print(f"{i+1}. {room.title} ({room.id})")

  while True:
    try:
      room_choice = int(input("\nEnter the number of the room to send the message to: "))
      if room_choice > 0 and room_choice <= len(room_list):
        break
      else:
        print("Invalid room number, please try again")
    except ValueError:
      print("Please enter a valid number")

  selected_room = room_list[room_choice-1]

  while True:
    message = input("Enter your message: ")
    if message:
      break
    else:
      print("Message cannot be empty, please try again")

  try:
    api.messages.create(roomId=selected_room.id, text=message)
  except ApiError as e:
    print("Error sending message:", e)

  print(f"Message sent to room '{selected_room.title}'")

  while True:
    go_back = input("Enter 5 to go back to main menu: ")
    if go_back.lower() == '5':
      break
  
  return

#Loop
while True:
    print("\nOptions:")
    print("0: Test Connection")
    print("1: Display Information")
    print("2: Display Rooms")
    print("3: Create Room")
    print("4: Send Message")
    print("5: Exit")

    option = input("Select an option: ")

    if option == "0":
        Test_Connection()
    elif option == "1":
        information()
    elif option == "2":
        displayRoom()
    elif option == "3":
        createRoom()
    elif option == "4":
        sendMessage()
    elif option == "5":
        print("Exit")
        break
    else:
        print("Invalid option. Please select a valid option.")
        
          

