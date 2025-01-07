
import requests
import pandas as pd
from haversine import haversine, Unit

class Lat_long:
    def __init__(self, file_name, sheet_name) -> None:
        """Find the Address, Latitude and Longitude"""
        self.file_name = file_name
        self.sheet_name = sheet_name
        # self.geolocator = Nominatim(user_agent="my_location")
    
    # read the data
    def read_file(self):
       df = pd.read_excel(self.file_name, self.sheet_name)
       return df
       

    # Get the entire row in a dataframe to find lat and long
    def lat_long(self):
        base_url =  "https://nominatim.openstreetmap.org/search?format=json"
        post_code = "600048"
        # college_name = "PERI Institute of Technology"
        # area = "V3P6+98 Mannivakkam, Tamil Nadu"
        
        response = requests.get(f"{base_url}&street={post_code}")
        # response = requests.get(f"{base_url}&q={query}")
        data = response.json()
        print(data)
        # latitude = data[0].get("lat")
        # longitude = data[0].get("lon")
        # latitude = "12.886182539529619"
        # longitude = "80.06076058125888"
        # location = float(latitude), float(longitude)
        # return location

    def rev_loc(self):
        # base_url =  "https://nominatim.openstreetmap.org/reverse?format=json"
        lat_value = "12.99130015163631"
        lon_value = "80.24296550982474"
        # response = requests.get(f"{base_url}&lat={lat_value}&lon={lon_value}")
        location_2 = float(lat_value), float(lon_value)
        return location_2
       
    def distance(self, df):
        kilo_mtr = []
        lat_value = "8.696715603453427"
        lon_value = "77.72444061931387"
        location = float(lat_value), float(lon_value)
        
        clg_latvalues = df["lat_value"].values
        clg_lonvalues = df["lon_value"].values

        for i,j in zip(clg_latvalues, clg_lonvalues):
            location2 = float(i), float(j)
            distance_ = haversine(location, location2, unit=Unit.KILOMETERS)
            kilo_mtr.append(distance_)
        return kilo_mtr
        
    # Write the address, Latitude and Longitude in an xl file
    def write_data(self, data):
        with pd.ExcelWriter("data/lat_lon_data.xlsx", mode="a", if_sheet_exists='overlay') as writer:
            pd.DataFrame({"Distance in kms" : data}).to_excel(writer, sheet_name="Sheet2", index=False)

loc_obj = Lat_long("data/lat_lon_data.xlsx", "Sheet2")
df = loc_obj.read_file()
# loc1 = loc_obj.lat_long()
# loc2 = loc_obj.rev_loc()

data = loc_obj.distance(df)
loc_obj.write_data(data)




 # distance_in_km = []
        # dest_lon_lat = df['lon_lat_value'].values
        # for coordinates in dest_lon_lat:
        #     url_endpoint = self.endpoint+profile+'/'+src_lon_lat+';'+coordinates
        #     print(url_endpoint)
        #     params = {
        #         'overview' : 'false'
        #     }
        #     response = requests.get(url_endpoint, params=params)
        #     data = response.json()
        #     distance_in_m = data['routes'][0]['legs'][0]['distance']
        #     # print(distance_in_m)
        #     km = distance_in_m/1000 # converting to KM
        #     distance_in_km.append(km)
        # print(distance_in_km)
        # return distance_in_km

# if debug:
#     print()
#     if len(sys.argv) == 3:
#         find_distance(sys.argv[1], sys.argv[2])
#     else:
#         print('Error while specifying arguments!')