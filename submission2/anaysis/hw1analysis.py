import pandas as pd

merged_data = pd.read_csv('../data/output/merged_data.csv')


# Count the number of plans for each plan type and display results largest down to smallest
plan_counts = merged_data['Plan Type'].value_counts().reset_index()

#make merged data 2 set which drops all special needs plans (SNP), employer group plans (eghp), and all “800-series”
# in "SNP Plan" column drop is says yes, in "EGHP" coloumn if says yes drop it, in "Plan ID" column between 800-900 drop it
merged_data2= merged_data[~merged_data['SNP Plan'].str.contains('Yes', na=False) &
                           ~merged_data['EGHP'].str.contains('Yes', na=False) &
                           ~merged_data['Plan ID'].between(800, 900, inclusive="left")]

plan_counts2 = merged_data2['Plan Type'].value_counts().reset_index()

merged_data2['Enrollment'] = pd.to_numeric(merged_data2['Enrollment'], errors='coerce')
# create table for enrollment count and average enrollment for each plan type
enrollment_summary = merged_data2.groupby('Plan Type')['Enrollment'].agg(['count', 'mean']).reset_index()
enrollment_summary.columns = ['Plan Type', 'Enrollment Count', 'Average Enrollment']
enrollment_summary = enrollment_summary.sort_values(by='Enrollment Count', ascending=False)