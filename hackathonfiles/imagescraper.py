import requests
import csv
import time
import re
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from bs4 import BeautifulSoup

# https://towardsdatascience.com/a-tutorial-on-scraping-images-from-the-web-using-beautifulsoup-206a7633e948


html_page = requests.get('http://books.toscrape.com/')
soup = BeautifulSoup(html_page.content, 'html.parser')
warning = soup.find('div', class_="alert alert-warning")
book_container = warning.nextSibling.nextSibling

images = book_container.findAll('img')
example = images[0]
imgurlEXT = example.attrs['src']

url_base = "http://books.toscrape.com/" #Original website
url_ext = example.attrs['src'] #The extension you pulled earlier
full_url = url_base + url_ext #Combining first 2 variables to create a complete URL

r = requests.get(full_url, stream=True) #Get request on full_url
# error handling for reuquest

if r.status_code == 200: #200 status code = OK
    print("good search")
    # if request is okay, open img, decode
    # decode raw content, save onto machine
#    with open("images/book1.jpg", 'wb') as f: 
#       r.raw.decode_content = True
#       shutil.copyfileobj(r.raw, f)



# to preview image
# img = mpimg.imread('images/book1.jpg')
# imgplot = plt.imshow(img)
# plt.show()

# print("\n",example)
# print("\n",imgurlEXT)
print("\n",full_url)