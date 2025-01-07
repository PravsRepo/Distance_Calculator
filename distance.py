import sys
import requests
import pandas as pd


class Lat_long:

    def __init__(self, file_name, sheet_name, url_endpoint) -> None:
        """Find the Address, Latitude and Longitude"""
        self.file_name = file_name
        self.sheet_name = sheet_name
        self.endpoint = url_endpoint
        # self.geolocator = Nominatim(user_agent="my_location")
    
    # read the data
    def read_file(self):
       df = pd.read_excel(self.file_name, self.sheet_name)
       return df

    def find_distance(self, df, profile, src_lon_lat):

        dest_lon_lat = df['lon_lat_value'].values[df['lon_lat_value'].values != 0]
        url_endpoints = [self.endpoint+profile+'/'+src_lon_lat+';'+c for c in dest_lon_lat]
      
        params = {'overview': 'false'}
        responses = [requests.get(url, params=params) for url in url_endpoints]

        distance_in_km = [(response.json()['routes'][0]['legs'][0]['distance'] / 1000) for response in responses]
        print(distance_in_km)
        return distance_in_km
       
    def write_data(self, data):
        with pd.ExcelWriter("data/new lon_lat_data.xlsx", mode="a", if_sheet_exists="overlay") as writer:
            pd.DataFrame({"Distance in kms" : data}).to_excel(writer, sheet_name="Zone 20", index=False, startcol=3)


src_lon_lat_rishon = '77.72409549491645,8.696521313421657'
src_lon_lat_mf = '78.09173091925844,9.933363972492069'
src_lon_lat_rp = '80.24293330569519,12.99106520226116'
url_endpoint = 'http://router.project-osrm.org/route/v1/'
loc_obj = Lat_long("data/new lon_lat_data.xlsx", "Zone 20", url_endpoint)

df = loc_obj.read_file()
data = loc_obj.find_distance(df, 'driving', src_lon_lat_rishon)
loc_obj.write_data(data)
