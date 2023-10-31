import requests
from bs4 import BeautifulSoup
import time

# The templates for the data to be scrapped from abyssinialaw.com
# make sure to improve the scrapeprs logix for other links (the flows are generally the same)


def save_to_file(text, file_path="data/scrapped_texts/", file_name="law_blog.txt"):
    try:
        with open(file_path + file_name, "a", encoding='utf-8') as f:
            f.write(text + "\n")
        print("[SUCCESS] SAVED TO FILE: " + file_path + file_name)
    except Exception as e:
        print("Failed to save to file: " + file_path + file_name)
        print("**************** START: ERROR LOG ***************")
        print(e)
        print("**************** END: ERROR LOG ***************")


def scrap(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("SUCCESS")
            soup = BeautifulSoup(response.content, 'html.parser')
            title = "TITLE STOP: " + \
                soup.find('h1', class_="eb-entry-title reset-heading").text
            content = soup.find(
                'div', class_="eb-entry-article clearfix").text
            return title + "\n" + content
    except Exception as e:
        print("Failed to scrap: " + url)
        print("**************** START: ERROR LOG ***************")
        print(e)
        print("**************** END: ERROR LOG ***************")


URL_LIST = 'data/scrapper_logs/scrapped_links.txt'
with open(URL_LIST, 'r', encoding='utf-8') as f:
    urls = f.readlines()
    for url in urls:
        text = scrap(url.rstrip())
        save_to_file(text)
print("DONE SCRAPPING")
