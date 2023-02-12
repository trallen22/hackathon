"""
starter code to get image urls
"""

import requests
from bs4 import BeautifulSoup
import os

# url = 'https://golfwang.com/collections/new/products/logo-puffy-jacket-by-golf-wang?variant=42362847133868'

def imagescrape(url,folder):
    # url = '' + url + ''
    # create directory joining current directory and new folder we made
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    # test if we are sucessfully accesing page
    # print(soup.title.text,"\n")

    images = soup.find_all('img')

    # gives a bunch of elements but not what we want
    # print(images)

    for image in images:
        # gives list of image links
        name = image['alt']
        url_link = image['src']

        #for shopify sites
        full_link = 'http:' + url_link 
        # get rid of trailing // in link
        url_link = url_link.replace('//','')

        # print(name,url_link,'\n')
        # print(full_link,'\n')

    # downloads images to current directory
        with open(name.replace(' ', '-').replace('/','') + '.jpg', 'wb') as f:
            im = requests.get(full_link)
            f.write(im.content)


    # '//cdn.shopify.com/s/files/1/0412/0133/6481/products/FW22LOGOPUFFYJACKET-BROWN_300x300.jpg?v=1675797870'
    # http:////cdn.shopify.com/s/files/1/0412/0133/6481/products/FW22LOGOPUFFYJACKET-BROWN_300x300.jpg?v=1675797870?

    print('Writing: ',name)
imagescrape('https://golfwang.com/collections/new/products/logo-puffy-jacket-by-golf-wang?variant=42362847133868','wang')