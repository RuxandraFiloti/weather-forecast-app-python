import requests

API_KEY = "cc2c3950e72332fb590d21b78b944327"

def get_data(place, forecast_days, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    #filter data 
    filtered_data = data["list"]

    #calculate the values of the weather for 24 days (filter the data by forecast days)
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    #filter by kind (Temperature or Sky) parameter
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data] # main is the dictionary and temp is a key in dictionary list
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data] #weather is the dictionary and main is key in dictionary list
        #[0] extracts the dictionary because is one single dictionary in this weather list -> weather:[{'': '', '': '', '': ''}]
    return filtered_data 
    

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))