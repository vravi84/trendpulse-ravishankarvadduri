import matplotlib.pyplot as plt
import pandas as pd
import os

#read csv
df=pd.read_csv("data/trends_analysed.csv")

#top ten stories
top_10_scores=df.sort_values(by='score',ascending=False).head(10)

#create a directory outputs
os.makedirs("outputs", exist_ok=True)

#Top 10 Stories by Score -chart1
plt.barh(y=top_10_scores['title'],width=top_10_scores['score'],align='center')
plt.title("Top Ten Stories By Score")
plt.xlabel('Scores')
plt.savefig("outputs/chart1_top_stories.png")
plt.show()

#stories vs category
story_vs_cat=df.groupby('category').size()
plt.bar(story_vs_cat.index,story_vs_cat.values,color=['red', 'green', 'blue', 'orange','cyan'])
plt.xlabel("Stories")
plt.ylabel("Scores")
plt.title("Story Vs Category")
plt.savefig("outputs/chart2_categories.png")
plt.show()

#Score vs Comments
colors = df['is_popular'].map({True: 'green', False: 'red'})
plt.scatter(x=df['score'],y=df['num_comments'],c=colors)
plt.xlabel("scores")
plt.ylabel("Number of comments")
plt.legend()
plt.savefig("outputs/chart3_scatter.png")
plt.show()

#dashboard
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

axes[0].bar(story_vs_cat.index, story_vs_cat.values)
axes[0].set_title("Stories vs Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Count")

axes[1].barh(top_10_scores['title'], top_10_scores['score'])
axes[1].set_title("Top 10 Stories by Score")
axes[1].set_xlabel("Score")

colors = df['is_popular'].map({True: 'green', False: 'red'})

axes[2].scatter(df['score'], df['num_comments'], c=colors)

axes[2].set_title("Score vs Comments")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Comments")

plt.suptitle("TrendPulse Dashboard", fontsize=16)

plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.show()