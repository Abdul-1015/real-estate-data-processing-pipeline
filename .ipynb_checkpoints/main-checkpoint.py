import pandas as pd;


raw_property_data = pd.read_csv("D:/Data Eningeering/DE_Proj1_RealEstate/data/raw_data/mum_property_data_12182025.csv")

df = pd.DataFrame(raw_property_data)

data_head = raw_property_data.head(5)

# helper_col = df.aggregate(['Price', 'City'])
# print(helper_col)
Processed_df = df[['ID','Possession Status', 'Availability Starts From', 'Developer', 'Units Available', 'Price', 'Booking Amount', 'Project Name', 'Carpet Area', 'Area Name', 'Parking', 'City', 'Covered Area', 'Location', 'Property', 'Maintenance Charges']]

# print(Processed_df)
# print (raw_property_data.index('Price'))

# print (df.columns)
# processed_data = 
# property_data.groupby