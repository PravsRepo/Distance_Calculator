
import requests
import pandas as pd


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
data = loc_obj.distance(df)
loc_obj.write_data(data)

