import pandas as pd
import os

# Load data from the input folder
enrollment_data = pd.read_csv("../data/input/CPSC_Enrollment_2015_01/CPSC_Enrollment_Info_2015_01.csv")
service_area_data = pd.read_csv("../data/input/MA_Cnty_SA_2015_01/MA_Cnty_SA_2015_01.csv")
contract_data = pd.read_csv("../data/input/CPSC_Enrollment_2015_01/CPSC_Contract_Info_2015_01.csv", encoding='latin1')
pd.set_option('display.max_columns', None)

#rename Contract Number to Contract ID , SSA State county code to SSA, and FIPS state county code to FIPS in enrollment data
enrollment_data.rename(columns={'Contract Number': 'Contract ID', 'SSA State County Code': 'SSA', 'FIPS State County Code': 'FIPS'}, inplace=True)

 # merge enrollment data with contract data on 'Contract ID' and 'Plan ID'
merged_data = pd.merge(enrollment_data, contract_data, on=['Contract ID', 'Plan ID'], how='left')

# #show me the merged data head
print(merged_data.head())

# fill in missing FIPS values with known FIPS values matching the county and state found elsewhere in the dataset
merged_data['FIPS'] = merged_data['FIPS'].fillna(merged_data.groupby(['State', 'County'])['FIPS'].transform('first'))
# fill in missing 'Offers Part D', 'SNP Plan', 'EGHP', values with known values matching from the Plan Type found elsewhere in the dataset
merged_data['Offers Part D'] = merged_data['Offers Part D'].fillna(merged_data.groupby(['Plan Type'])['Offers Part D'].transform('first'))
merged_data['SNP Plan'] = merged_data['SNP Plan'].fillna(merged_data.groupby(['Plan Type'])['SNP Plan'].transform('first'))
merged_data['EGHP'] = merged_data['EGHP'].fillna(merged_data.groupby(['Plan Type'])['EGHP'].transform('first'))



merged_data.to_csv("../data/output/merged_data.csv", index=False)