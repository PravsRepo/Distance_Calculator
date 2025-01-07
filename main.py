import pandas as pd
import openpyxl

class Filter:

    def __init__(self, file_name) -> None:
        """Program Initiated..."""
        self.file_name = file_name
    
    def read_data(self):
        df = pd.read_csv(self.file_name)
        return df

    def get_cols(self, all_df):
        for i in all_df.columns:
            all_df = all_df.rename(columns = lambda i:i.replace(' ', '_'))
        return all_df

    def filter_data(self, all_df):
        filter_df = all_df[(all_df.Unique_College > 0)]
        print(filter_df)
        return filter_df

    def save_data(self, filter_df):
        filter_df.to_excel("Filtered_data.xlsx", index = False)


data_obj = Filter("data/Data.csv")
all_df = data_obj.read_data()
all_df = data_obj.get_cols(all_df)
filter_df = data_obj.filter_data(all_df)
data_obj.save_data(filter_df)