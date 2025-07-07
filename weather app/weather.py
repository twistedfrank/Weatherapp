import ascii
import requests

# Dumb global variable cause im dumb
global program
program = True

# Input your api key here. sign up at weatherapi.com to get a free api key
api = ""
# Base url for the api itself
base_url = "api.weatherapi.com/v1"
# user_location = input("Enter a location: ")




# Function for the weather "getter"
def get_weather():

    global program

    # Ascii name

    print("""
 __        __         _     _                               
 \ \      / /__  __ _| |__ | |_ ___ _ __    __ _ _ __  _ __  
  \ \ /\ / / _ \/ _` | '_ \| __/ _ \ '__|  / _` | '_ \| '_ \ 
   \ V  V /  __/ (_| | | | | ||  __/ |    | (_| | |_) | |_) |
    \_/\_/ \___|\__,_|_| |_|\__\___|_|     \__,_| .__/| .__/ 
                                                |_|   |_|    
        """)


    # User input for location
    user_location = input("Enter a city: ")
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

        again = int(input("Would you like to enter another city? 1 for yes. 2 for no"))
        if again == 1:
            get_weather()
        elif again == 2:
            program = False
            main()


def main():
    # Shitty program loop cause im dumb
    if program == True:
        get_weather()
    elif program == False:
        print("Exiting.")
        exit
main()
