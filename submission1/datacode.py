import pandas as pd
import os

# Load data from the input folder
enrollment_data = pd.read_csv("/Users/ryanscholte/Desktop/GitHub/HW1/data/input/CPSC_Enrollment_2015_01/CPSC_Enrollment_Info_2015_01.csv")
service_area_data = pd.read_csv("/Users/ryanscholte/Desktop/GitHub/HW1/data/input/MA_Cnty_SA_2015_01/MA_Cnty_SA_2015_01.csv")

# Preview the data
print(enrollment_data.head())
print(service_area_data.head())

merged_data = pd.merge(enrollment_data, service_area_data, 
                       left_on="Contract Number", right_on="Contract ID", 
                       how="inner")

#show the merged data
print(merged_data.head())