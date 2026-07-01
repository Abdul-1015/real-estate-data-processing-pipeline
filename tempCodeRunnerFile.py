import pandas as pd;


raw_property_data = pd.read_csv("D:/Data Eningeering/DE_Proj1_RealEstate/data/raw_data/mum_property_data_12182025.csv")

df = pd.DataFrame(raw_property_data)

data_head = raw_property_data.head(5)

helper_col = df.aggregate(['Price', 'City'])