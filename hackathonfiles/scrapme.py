import requests
import csv
import time
import re
from bs4 import BeautifulSoup

# what i need
# <img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" 
# alt="A Light in the Attic" class="thumbnail">
# 



def scrape(source_url, soup):  # Takes the driver and the subdomain for concats as params
    # Find the elements of the article tag
    books = soup.find_all("article", class_="product_pod")
    #sourceurl-

    # Iterate over each book article tag
    for each_book in books:
        info_url = source_url+"/"+each_book.h3.find("a")["href"]
        cover_url = source_url+"/catalogue" + \
            each_book.a.img["src"].replace("..", "")

        title = each_book.h3.find("a")["title"]
        rating = each_book.find("p", class_="star-rating")["class"][1]
        image = each_book.find("a")["img"]
        # can also be written as : each_book.h3.find("a").get("title")
        price = each_book.find("p", class_="price_color").text.strip().encode(
            "ascii", "ignore").decode("ascii")
        availability = each_book.find(
            "p", class_="instock availability").text.strip()
        
        seed ="http://books.toscrape.com/catalogue/page-{}.html".format(str(page_number))

        # Invoke the write_to_csv function
        write_to_csv([info_url, cover_url,image, title, rating, price])


def write_to_csv(list_input):
    # The scraped info will be written to a CSV here.
    try:
        with open("allBooks.csv", "a") as fopen:  # Open the csv file.
            csv_writer = csv.writer(fopen)
            csv_writer.writerow(list_input)
    except:
        return False
