import json
import showtopnews

with open("newsafr.json", encoding='utf-8') as js:
    json_data = json.load(js)

js_dict = json_data["rss"]["channel"]["items"]

news_list = []
for news in js_dict:
    news_list = news_list + str(news['description']).split()

showtopnews.show_top_10_news(news_list)
