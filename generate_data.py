import pandas as pd
import numpy as np

#to set random seed of 42

np.random.seed(42)

n_items = 100

data_frame = pd.DataFrame({
    "Item_ID" : [f"ITEM_{i:03d}" for i in range(1, n_items+1)],
    "Annual_Demand" : np.random.randint(50,5000,n_items),
    "Unit_Cost" : np.random.uniform(5,1000, n_items).round(2)
})

#print(data_frame.head())

data_frame["Annual_Consumption"] = (data_frame["Annual_Demand"] * data_frame["Unit_Cost"]).round(2)

data_frame.to_csv("inventory_data.csv", index=False)

print("Data has been generated and saved to inventory_data.csv")

print(data_frame.head())




