import xml.etree.ElementTree as ET
from collections import Counter

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
channel = root.find("channel")
items = channel.findall("item")

news_list = []

for item in items:
    news_list = news_list + str(item.find('description').text).split()

news_list2 = []
for word in news_list:
    if len(word) > 6:
        news_list2.append(word)

news_list2.sort()

print(Counter(news_list2).most_common(10))
