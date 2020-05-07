import json
from pprint import pprint
from collections import Counter

with open("newsafr.json", encoding='utf-8') as js:
    json_data = json.load(js)

news_list = []
js_dict = json_data["rss"]["channel"]["items"]
for news in js_dict:
    news_list = news_list + str(news['description']).split()

news_list2 = []
for word in news_list:
    if len(word) > 6:
        news_list2.append(word)

news_list2.sort()

c = Counter(news_list2).most_common(10)
print(c)





#print(news_str)