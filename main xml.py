import xml.etree.ElementTree as ET
import showtopnews

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
channel = root.find("channel")
items = channel.findall("item")

news_list = []
for item in items:
    news_list = news_list + str(item.find('description').text).split()

showtopnews.show_top_10_news(news_list)

