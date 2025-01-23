import pandas as pd

# Load data from the input folder
enrollment_data = pd.read_csv("data/input/enrollment_2015.csv")
service_area_data = pd.read_csv("data/input/service_area_2015.csv")

# Preview the data
print(enrollment_data.head())
print(service_area_data.head())