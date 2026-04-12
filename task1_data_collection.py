import requests
import json
import time
import os
from datetime import datetime
from collections import defaultdict

url='https://hacker-news.firebaseio.com/v0/topstories.json'
headers = {"User-Agent": "TrendPulse/1.0"}

#fetch response
res=requests.get(url,headers=headers)

#convert response into json
story_ids=res.json()

#fetch first 500 ids

# Get first 500 IDs
top_500_ids = story_ids[:500]

from requests.exceptions import RequestException
categories={
    "technology":["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews":["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports":["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science":["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment":["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]

}
story_details=[]
stories_with_catagories=defaultdict(list)

for i in top_500_ids:
  try:
   res=requests.get(f"https://hacker-news.firebaseio.com/v0/item/{i}.json")
   data=res.json()
   print(data)
   story_details.append(data)
 
   for category, keywords in categories.items():
      if any(keyword in data['title'] for keyword in keywords):
        if(len(stories_with_catagories[category])<25):
            required_story={
           "post_id":data['id'],
           "title":data['title'],
           "category":category,
           "score":data['score'],
           "num_comments":data.get('descendants'),
           "author":data['by'],
           "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           }
        stories_with_catagories[category].append(required_story)
        break
        time.sleep(0.2)

  except RequestException as err:
        print(f"Unexpected error: {err}")

filename =f"trends_{datetime.now().strftime("%Y%m%d")}.json"
os.makedirs("data", exist_ok=True)
filepath = os.path.join("data", filename)
with open(filepath, "w", encoding="utf-8") as f:
    json.dump(dict(stories_with_catagories), f, indent=4)

#counting number of collected stories
total_stories = 0
for stories in stories_with_catagories.values():
    total_stories += len(stories)    
print(len(stories_with_catagories))
print(f"Collected {total_stories} Stories.Saved to {filepath}.")