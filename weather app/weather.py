import ascii
import os
import requests

# Dumb global variable cause im dumb

# Input your api key here. sign up at weatherapi.com to get a free api key
api = "915aa4045ba442f095020221250707"
# Base url for the api itself
base_url = "api.weatherapi.com/v1"
# user_location = input("Enter a location: ")





# Function for the weather "getter"
def get_weather(user_location):


    # User input for location
    #user_location = input("Enter a city: ")
    #url f string {} used to fill in the url to access information from base url, w api key and user location
    url = f"http://{base_url}/current.json?key={api}&q={user_location}"
    
    response = requests.get(url)



    if response.status_code == 200: # if connection with API good
        data = response.json()
        print("Status good.")
        print("")
        # f strings with api commands to access weather infomation from the api
        # Review weather api documention for list of api functions/features

        print("Weather information:")
        print("")
        print(f"Location:", data["location"]["name"])
        print(f"Tempature:", data["current"]["temp_f"])
        print(f"Feels like:", data["current"]["feelslike_f"])
        print(f"Current wind speed:", data["current"]["wind_mph"])
        print("--------------")
        print(f"Condition:", data["current"]["condition"]["text"])

# Function for changing locations
def change_location():
    user_location = input("Enter your new city: >> ")
    with open("location.txt", "w") as f:
        f.write(user_location)
    return user_location


# Function for setting the users location
def set_location():
    if os.path.exists("location.txt"):
        with open("location.txt", "r") as f:
            user_location = f.read().strip()
    else:
        user_location = input("Enter a city >> ")
        with open("location.txt", "w") as f:
            f.write(user_location)
    return user_location


def main():

    print("""
 __        __         _     _                               
 \ \      / /__  __ _| |__ | |_ ___ _ __    __ _ _ __  _ __  
  \ \ /\ / / _ \/ _` | '_ \| __/ _ \ '__|  / _` | '_ \| '_ \ 
   \ V  V /  __/ (_| | | | | ||  __/ |    | (_| | |_) | |_) |
    \_/\_/ \___|\__,_|_| |_|\__\___|_|     \__,_| .__/| .__/ 
                                                |_|   |_|    
        """)

    # Checking of location.txt exists, if it does not it will prompt to create one.
    if os.path.exists("location.txt"):
        with open("location.txt", "r") as f:
            user_location = f.read().strip()
    else:
        user_location = set_location()

    while True:

        

        # Simple Mainmenu
        main_menu = int(input("""

        1. Check weather
        2. Change location
        3. Quit
                        >>"""))

        if main_menu == 1:
            get_weather(user_location)
        elif main_menu == 2:
            user_location = change_location()
        elif main_menu == 3:
            break
main()



