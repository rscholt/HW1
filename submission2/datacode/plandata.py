import pandas as pd

import os
print(os.getcwd())

# Load data from the input folder
enrollment_data = pd.read_csv("data/input/CPSC_Enrollment_2015_01/CPSC_Enrollment_Info_2015_01.csv")
contract_data = pd.read_csv("data/input/CPSC_Enrollment_2015_01/CPSC_Contract_Info_2015_01.csv", encoding='latin1')
pd.set_option('display.max_columns', None)

#rename Contract Number to Contract ID , SSA State county code to SSA, and FIPS state county code to FIPS in enrollment data
enrollment_data.rename(columns={'Contract Number': 'Contract ID', 'SSA State County Code': 'SSA', 'FIPS State County Code': 'FIPS'}, inplace=True)

 # merge enrollment data with contract data on 'Contract ID' and 'Plan ID'
merged_datax = pd.merge(enrollment_data, contract_data, on=['Contract ID', 'Plan ID'], how='left')

# #show me the merged data head
# print(merged_datax.head())

# fill in missing FIPS values with known FIPS values matching the county and state found elsewhere in the dataset
merged_datax['FIPS'] = merged_datax['FIPS'].fillna(merged_datax.groupby(['State', 'County'])['FIPS'].transform('first'))
# fill in missing 'Offers Part D', 'SNP Plan', 'EGHP', values with known values matching from the Plan Type found elsewhere in the dataset
merged_datax['Offers Part D'] = merged_datax['Offers Part D'].fillna(merged_datax.groupby(['Plan Type'])['Offers Part D'].transform('first'))
merged_datax['SNP Plan'] = merged_datax['SNP Plan'].fillna(merged_datax.groupby(['Plan Type'])['SNP Plan'].transform('first'))
merged_datax['EGHP'] = merged_datax['EGHP'].fillna(merged_datax.groupby(['Plan Type'])['EGHP'].transform('first'))


merged_datax.to_csv("data/output/merged_datax.csv", index=False)