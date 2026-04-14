import numpy as np
import pandas as pd

df=pd.read_csv("data/trends_clean.csv")
print(f"Loaded data:{df.shape}")

print(f"First five rows \n{df.head()}")

avg_score=df['score'].mean()
avg_num_comments=df['num_comments'].mean()
print(f"Avrage score: {avg_score}")
print(f"Avrage comments: {avg_num_comments}")

#Basic Analysis With Numpy
np_score=df['score'].values
mean_score=np.mean(np_score)
median_score=np.median(np_score)
std_score=np.std(np_score)
max_score=np.max(np_score)
min_score=np.min(np_score)
print("--------Numpy stats-------\n")
print(f"Mean score :{mean_score}\n Median score :{median_score}\nStd deviation :{std_score}\nMax score :{max_score}\nMin score :{min_score}")
most_story_cat = df.groupby('category').size().nlargest(1)

category = most_story_cat.index[0]
count = most_story_cat.values[0]

print(f"Most stories in: {category} ({count} stories)")

#filtere dataframe contains title and comments
filtered_df=df.sort_values(by='score',ascending=False).head(1)

selected_df=filtered_df[['title','num_comments']]
title = selected_df.iloc[0]['title']
num_comments = selected_df.iloc[0]['num_comments']

print(f'Most commented story: "{title}" — {num_comments:,} comments')
#Adding new column
df['engagement']=df['num_comments']/(df['score']+1)
df['is_popular']=(df['score']>mean_score)


#save to csv file 
filepath="data/trends_analysed.csv"
df.to_csv(filepath,index=False, encoding="utf-8")
print(f"Saved to {filepath}")