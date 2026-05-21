import json

with open("users.json") as f:
    data = json.load(f)

print("Total Users:", len(data))

# json to dataframe

import pandas as pd

df = pd.json_normalize(data)

print(df.head())

print(df.duplicated().sum())

print(df.isnull().sum())

#print(df["address.city"].value_counts())

#print(df["company.name"].value_counts())

# Email Validation

import re

for email in df["email"]:
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print(email) 

# Save to CSV 
df.to_csv("users.csv", index=False)

#Save to xml

#Method 1: Using pandas built-in function
df.to_xml("users_1.xml", index=False)

#Method 2: Using dicttoxml library
import xml.etree.ElementTree as ET

root = ET.Element("users")

for user in data:
    user_elem = ET.SubElement(root, "user")

    for key, value in user.items():

        if isinstance(value, dict):
            nested = ET.SubElement(user_elem, key)

            for k, v in value.items():

                if isinstance(v, dict):
                    subnested = ET.SubElement(nested, k)

                    for sk, sv in v.items():
                        child = ET.SubElement(subnested, sk)
                        child.text = str(sv)
                else:
                    child = ET.SubElement(nested, k)
                    child.text = str(v)

        else:
            child = ET.SubElement(user_elem, key)
            child.text = str(value)

tree = ET.ElementTree(root)
tree.write("users_2.xml")

