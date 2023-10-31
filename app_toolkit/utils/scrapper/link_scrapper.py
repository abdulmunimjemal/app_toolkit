import requests
from bs4 import BeautifulSoup
import time


def log_link(link):
    with open("data/scrapper_logs/scrapped_links.txt", "a", encoding='utf-8') as f:
        f.write(link + "\n")


def scrape_links(blog_url, root):
    scrapped_links = 0
    try:
        response = requests.get(blog_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a', href=True, class_="text-inherit")
            for link in links:
                if link['href'].startswith("/blog/"):
                    log_link(root + link['href'])
                    scrapped_links += 1
    except Exception as e:
        print("Failed to scrap: " + blog_url)
        print("**************** START: ERROR LOG ***************")
        print(e)
        print("**************** END: ERROR LOG ***************")
    finally:
        return scrapped_links


blog_url = "https://abyssinialaw.com/blog/"
base_url = "https://abyssinialaw.com"
scrapped = 0
for i in range(1, 100, 10):
    url = blog_url + "?start=" + str(i) if i != 1 else blog_url
    print(f"Scrapping: {url}")
    scrapped += scrape_links(url, base_url)
    time.sleep(1)

print(f"Total scrapped links: {scrapped}")
