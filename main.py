# import requests

# response = requests.get("https://books.toscrape.com/")

# print(f"voici le status code: {response.status_code}")
# with open("books.html","w") as file :
#      file.write(response.text)

# name = "Jean"

# file_name = "name.txt"

# with open(file_name,"w") as file :
#     file.write(name)

# from bs4 import BeautifulSoup

# with open("books.html","r") as file:
#     html_content = file.read()

# soup = BeautifulSoup(content, "html.parser")

# price = soup.find("p", class_="price_color").get_text()
# print(float(price[2:]))

import requests
from bs4 import BeautifulSoup


def get_all_page_links(total_pages: int) -> list:
    urls = []
    for page in range(1, total_pages + 1):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        urls.append(url)
    return urls


def get_book_links_from(page_link: str) -> list:
    domain = "https://books.toscrape.com/catalogue/"
    response = requests.get(page_link)
    links = []
    if response.status_code != 200:
        print(f"ERROR - Status code: {response.status_code}")
    else:
        content_html = response.text
        soup = BeautifulSoup(content_html, "html.parser")
        all_tag_div = soup.find_all("div", class_="image_container")
        for tag_div in all_tag_div:
            link = domain + tag_div.find("a").get("href")
            links.append(link)
    return links

def main():
    page_links = get_all_page_links(1)
    book_links = []
    for page_link in page_links:
        print(f"Getting links for page {page_link}")
        book_links += get_book_links_from(page_link)
    print(len(book_links))


main()
