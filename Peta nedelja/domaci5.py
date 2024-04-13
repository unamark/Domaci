import datetime
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json
import csv


#   1.
f = pd.read_csv('dailyActivity_merged.csv')
ime = ['Id', 'TotalSteps', 'TotalDistance', 'TrackerDistance', 'LoggedActivitiesDistance', 'VeryActiveDistance', 'ModeratelyActiveDistance',
       'LightActiveDistance', 'SedentaryActiveDistance', 'VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes', 'SedentaryMinutes', 'Calories']

abs_val = f[ime].abs()

max_val = f['TotalSteps'].max()
min_val = f['TotalSteps'].min()
mean_val = f['TotalSteps'].mean()
print(max_val, min_val)
print(abs_val)
print((max_val - mean_val)/mean_val*100)

f['TotalSteps'] = (f['TotalSteps'] - min_val) / (max_val - min_val)
f.to_csv('_normalized.csv', index=False)

d = pd.DataFrame(f[ime])
print("-----------------------------------------------")
cor_mat = d.corr()
max_pos = cor_mat.unstack().sort_values().drop_duplicates().iloc[-3:-1]
max_neg = cor_mat.unstack().sort_values().drop_duplicates().head(2)
print("Maksimalna pozitivna korelacija izmadju:\n", max_pos)
print("Maksimalna negativna korelacija izmadju:\n", max_neg)

std_deviation = d.std()
print(std_deviation)

for column in d.columns:
    plt.figure(figsize=(8, 6))
    plt.hist(d[column], bins=20, color='skyblue', edgecolor='black')
    # plt.legend(handle="Standardna devijacija", loc='upper right')
    std_dev = d[column].std()
    # plt.axhline(std_dev, color="red", label="Standardna devijacija")
    plt.title(f'Raspodela vrednosti u koloni {column}')
    plt.xlabel(f'{column}')
    plt.ylabel('Velicina')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    break

# Ili sve histograme u jednom dijagramu
'''plt.figure(figsize=(10, 8))
for column in d.columns:
    plt.hist(d[column], bins=20, alpha=0.5, label=column)
plt.bar(d)
plt.title('Raspodela vrednosti u svakoj koloni')
plt.xlabel('Vrednost')
plt.ylabel('Brojnost')
plt.legend()
plt.grid(True)
plt.show()'''


#    2.


def scrape_realitica(city_or_category):
    url = f"https://www.realitica.com/?cur_page=1&for={city_or_category}"
    all_properties = []

    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        properties = soup.find_all("div", class_="thumb_div")

        for property in properties:
            details = {}

            details["title"] = property.find("h2").text.strip()
            details["price"] = property.find(
                "div", class_="price").text.strip()

            # Dodajte ostale detalje nekretnine

            all_properties.append(details)

        next_page = soup.find("a", class_="next_page")
        if not next_page:
            break
        url = "https://www.realitica.com/" + next_page["href"]

    return all_properties


def save_to_csv(properties, filename):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["title", "price"]  # Dodajte ostale polja ovdje
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for property in properties:
            writer.writerow(property)


city_or_category = "zagreb"  # Promijenite na željeni grad ili kategoriju
properties = scrape_realitica(city_or_category)
save_to_csv(properties, "realitica_properties.csv")


#   3.


def search_article_by_title(articles, title):
    for article in articles:
        if article['title'] == title:
            return article
    return None


def add_comment_to_article(articles, title, des, author="anoniman"):
    for article in articles:
        if article['title'] == title:
            if 'comments' not in article:
                article['comments'] = []
            article['comments'].append(
                {'title': title, 'author': author, 'description': des})
            return True
    return False


def delete_article_by_comment_title(articles, comment_title):
    for article in articles:
        if 'comments' in article:
            for comment in article['comments']:
                if comment['title'] == comment_title:
                    articles.remove(article)
                    return True
    return False


def get_comment_by_title(article, comment_title):
    if 'comments' in article:
        for comment in article['comments']:
            if comment['title'] == comment_title:
                return comment

        return None


def get_comments_by_author(article, author):
    comments_with_author = []
    if 'comments' in article:
        for comment in article['comments']:
            if 'author' in comment and comment['author'] == author:
                comments_with_author.append(comment)
    return comments_with_author


def get_articles_by_author(articles, author):
    articles_by_author = []
    for article in articles:
        if 'author' in article and article['author'] == author:
            articles_by_author.append(article)
    return articles_by_author


def write_articles_to_csv(articles, author, output_file):
    articles_by_author = get_articles_by_author(articles, author)
    sorted_articles = sorted(
        articles_by_author, key=lambda x: len(x['comments']), reverse=True)

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['title', 'author', 'description',
                      'category', 'views', 'comments']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for article in sorted_articles:
            writer.writerow(article)


def write_articles_to_json(articles, author, output_file):
    articles_by_author = get_articles_by_author(articles, author)
    sorted_articles = sorted(
        articles_by_author, key=lambda x: len(x['views']), reverse=True)

    with open(output_file, mode='w', encoding='utf-8') as file:
        json.dump(sorted_articles, file, indent=4)


with open('articles.json', 'r') as fajl:
    data = json.load(fajl)


author = "Marco Arment"
output_json_file = "articles_by_author.json"
write_articles_to_json(data['data']['articles'], author, output_json_file)

title_to_find = "Apple is Listening"
found_article = search_article_by_title(
    data['data']['articles'], title_to_find)
if found_article:
    print("Found article:")
    print(found_article)
else:
    print(f"Article with title '{title_to_find}' not found.")

title_to_comment = "Apple is Listening"
comment_description = "Great article! Really enjoyed reading it."
author_of_comment = "John Doe"
add_comment_to_article(data['data']['articles'],
                       title_to_comment, comment_description, author_of_comment)
# print(data)

comment_title_to_delete = "hi"
delete_article_by_comment_title(
    data['data']['articles'], comment_title_to_delete)
print(data)

comment_title_to_find = "hi"
found_comment = get_comment_by_title(data, comment_title_to_find)
if found_comment:
    print("Found comment:")
    print(found_comment)
else:
    print(f"Comment with title '{comment_title_to_find}' not found.")

author_to_find = "Marco Arment"
comments_by_author = get_comments_by_author(data, author_to_find)
if comments_by_author:
    print(f"Found comments by author '{author_to_find}':")
    for comment in comments_by_author:
        print(comment)
else:
    print(f"No comments found by author '{author_to_find}'.")

author_to_find = "Marco Arment"
articles_by_author = get_articles_by_author(
    data['data']['articles'], author_to_find)
if articles_by_author:
    print(f"Found articles by author '{author_to_find}':")
    for article in articles_by_author:
        print(article)
else:
    print(f"No articles found by author '{author_to_find}'.")

author_to_write = "Marco Arment"
output_csv_file = "articles_by_author.csv"
write_articles_to_csv(data['data']['articles'],
                      author_to_write, output_csv_file)
print(f"Articles by author '{
      author_to_write}' written to '{output_csv_file}'.")
