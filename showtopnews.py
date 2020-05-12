from collections import Counter


def show_top_10_news(news_list):
    news_list2 = []
    for word in news_list:
        if len(word) > 6:
            word = word.title()
            news_list2.append(word)

    news_list2.sort()

    print(Counter(news_list2).most_common(10))
