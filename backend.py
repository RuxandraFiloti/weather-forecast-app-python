import requests

API_KEY = "cc2c3950e72332fb590d21b78b944327"

def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    #filter data 
    filtered_data = data["list"]

    #calculate the values of the weather for 24 days (filter the data by forecast days)
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data 
    

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))