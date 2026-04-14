#Task 2 Data processing
import pandas as pd
import json

#load json
filepath = "data/trends_20260414.json"

with open(filepath, "r", encoding="utf-8") as f:
    data = json.load(f)

#making uniform length
data_equal_records={}
for category, stories in data.items():
    data_equal_records[category] = stories[:16]
#create a dataframe
rows=[]
for category, stories in data_equal_records.items():
    for story in stories:
      rows.append(story)
df=pd.DataFrame(rows)
print(f"Number of rows loaded",len(rows))
print(df)
#no of rows and coloumns
print(df.shape)
#datatype and non-null values
print(df.info())

#number of duplicate records
print(df.duplicated())
print(df.duplicated().sum())

#null or missing values count
print(df.isnull().sum())

#checking sure score and num_comments are integers
print(df.dtypes)
#remove stories where score is less than 5
print(df.drop(df[df['score']<5].index,inplace=True))

# strip extra spaces from the title column
df['title']=df['title'].str.strip()

#no of rows after cleaning
print("Number of rows after cleaning ",df.shape[0])

#save to csv file 
df.to_csv("data/trends_clean.csv",index=False, encoding="utf-8")

#Quick Summary
group_counts=df.groupby('category').size()
print(group_counts)
for category,count in group_counts.items():
  print(f"Category {category} has {count} rows")