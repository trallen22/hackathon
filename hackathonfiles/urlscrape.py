"""
starter code to get image urls
"""

import requests
from bs4 import BeautifulSoup
import os
import cookiehead

# cookies = {
#     'dwsid': 'NQZIMEqd-PzynjvxyP2K_byBJcHVF9OMf5e37EaVkIMcSnkb_fn02i9-b6MPfV8OO-Lhn2M9oWM0KFHz32kVxA==',
#     'ua-target-session-id': '2fd0470b-0a70-48e2-9cfb-5abfc8adfc08',
#     'ua-experience-pdp': 'salesforce',
#     'dwac_b69c08bd482c4e7baa999dc69c': '6P-Q0M5JnJ7DkXYdtmRrKmF4_SFRw7fuTpg%3D|dw-only|||USD|false|US%2FEastern|true',
#     'cqcid': 'abnysdNnyIsTu8i8nzDM5x7TFU',
#     'cquid': '||',
#     'sid': '6P-Q0M5JnJ7DkXYdtmRrKmF4_SFRw7fuTpg',
#     'dwanonymous_7254072e2668c23dc3bf6cca213a6657': 'abnysdNnyIsTu8i8nzDM5x7TFU',
#     '_pxhd': 'Sw7Si9dyRI1lRJ54r9krdPdV8oxqwBbhCnbbU7czHMaH2ZCD2Ikc9lKCnkyWpbfmlpUQ0kXO8qBv5jBrO6duIg==:WZBPcijC5RWYlVPnuPRXEOJt09N5NxxEigwUW-CrMUjBDWLfib7UuVg/b0TgQJmtKbel7VJ0wAWsBVGlzFO3ud0g8u2dTsRsH/F9bso/G-E=',
#     '__anact': '%5B%7B%22activityType%22%3A%22viewSearch%22%2C%22parameters%22%3A%7B%22cookieId%22%3A%22%22%2C%22userId%22%3A%22%22%2C%22searchText%22%3A%221295739%22%2C%22suggestedSearchText%22%3A%22__UNDEFINED__%22%2C%22products%22%3A%5B%5D%2C%22showProducts%22%3Afalse%2C%22personalized%22%3Atrue%2C%22refinements%22%3A%22%5B%5D%22%2C%22searchID%22%3A%22099339d6-c424-474a-9071-ba1e42aadb0f%22%2C%22locale%22%3A%22en_US%22%2C%22queryLocale%22%3A%22en_US%22%2C%22realm%22%3A%22BCVK%22%2C%22siteId%22%3A%22US%22%2C%22instanceType%22%3A%22prd%22%7D%7D%5D',
#     '__cq_dnt': '0',
#     'dw_dnt': '0',
#     '__cqact': '%5B%7B%22activityType%22%3A%22viewSearch%22%2C%22parameters%22%3A%7B%22cookieId%22%3A%22%22%2C%22userId%22%3A%22%22%2C%22searchText%22%3A%221295739%22%2C%22suggestedSearchText%22%3A%22__UNDEFINED__%22%2C%22products%22%3A%5B%5D%2C%22showProducts%22%3Afalse%2C%22personalized%22%3Atrue%2C%22refinements%22%3A%22%5B%5D%22%2C%22searchID%22%3A%22099339d6-c424-474a-9071-ba1e42aadb0f%22%2C%22locale%22%3A%22en_US%22%2C%22queryLocale%22%3A%22en_US%22%2C%22realm%22%3A%22BCVK%22%2C%22siteId%22%3A%22US%22%2C%22instanceType%22%3A%22prd%22%7D%7D%5D',
#     'notice_behavior': 'implied,eu',
#     'emailSubscribeCookie': 'second',
#     'consentCookie': 'first',
#     'utag_main': 'v_id:018642fba1d2007535f436a5767805054004200f00942$_sn:1$_se:3$_ss:0$_st:1676162848388$ses_id:1676161032658%3Bexp-session$_pn:3%3Bexp-session',
#     'bfx.apiKey': '41a1f990-a119-11ea-9767-f9dfebd38fce',
#     'bfx.env': 'PROD',
#     'bfx.logLevel': 'ERROR',
#     '_px_f394gi7Fvmc43dfg_user_id': 'OTkwZTRkMjEtYWE2YS0xMWVkLWI0NWItZDU0YWFjZGY3MDdi',
#     'bfx.country': 'US',
#     'bfx.currency': 'USD',
#     'bfx.language': 'es',
#     'bfx.isInternational': 'false',
#     'bfx.sessionId': '7be7e8c4-7afb-4c8c-ad69-bff6172ad449',
#     'ua-experience-plp': 'salesforce',
#     'UAVisitorType': 'guest',
#     'BVBRANDID': 'b991a91d-75e0-41d9-8f0b-b93b2ce12822',
#     'BVBRANDSID': 'ad6de37d-842f-4cf2-b4a7-eb27f5c821b3',
#     's_fid': '45E76AE22B025A1E-30B7567530E7FCB8',
#     's_sq': 'underarmourtealiumdev%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fwww.underarmour.com%25252Fen-us%25252Fc%25252Fshoes%25252F%2526link%253DUnisex%252520UA%252520SlipSpeed%2525E2%252584%2525A2%252520Training%252520Shoes%2526region%253D3027057%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fwww.underarmour.com%25252Fen-us%25252Fc%25252Fshoes%25252F%2526oid%253Dhttps%25253A%25252F%25252Fwww.underarmour.com%25252Fen-us%25252Fp%25252Ftraining%25252Funisex_ua_slipspeed_training_shoes%25252F3027057.html%25253Fdwvar_3%2526ot%253DA',
#     'ak_bmsc': 'A48C9CA45534F7476B908B7036C2C9E5~000000000000000000000000000000~YAAQPdcwF0zCKjCGAQAAEOD7QhILfNJPQEUx/mG9cEzI+h8Gd0foK2iYuLP5TcnPHBiu6hWG9mMFledgCkpbkzLVKRGHTB/7yHLURf2vkINez+QgR1lxXAjki7kONQQHWe9MJLGlXlSccgYvEoMtij+Ukp8JIkds6uF4RRCzRW810I7d/mtuHAEcDiy3cnVvdWUdzJ7Y7qyG/9hbvVYHzT2iBP+XAgsMhjb4dn76yHj6eulQXoEFl98GZD5YkieyTfErITD5WnvDJGo7Ner8A+84M6TY7IVdjEMFXOj8iG1uxd4Hz0J/LVyTInD4231yQ1Sg4Apm+iKmXRCefhKztb2IzTzqEHZWWFCGTSYUMjwA//4r+A/ZAOi2tYPozolDo9xqsVP6yBysQz6eDLGu',
#     'BVImplmain_site': '2471',
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'Accept-Language': 'en-US,en;q=0.5',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Referer': 'https://www.underarmour.com/en-us/c/shoes/',
#     'DNT': '1',
#     'Connection': 'keep-alive',
#     # 'Cookie': 'dwsid=NQZIMEqd-PzynjvxyP2K_byBJcHVF9OMf5e37EaVkIMcSnkb_fn02i9-b6MPfV8OO-Lhn2M9oWM0KFHz32kVxA==; ua-target-session-id=2fd0470b-0a70-48e2-9cfb-5abfc8adfc08; ua-experience-pdp=salesforce; dwac_b69c08bd482c4e7baa999dc69c=6P-Q0M5JnJ7DkXYdtmRrKmF4_SFRw7fuTpg%3D|dw-only|||USD|false|US%2FEastern|true; cqcid=abnysdNnyIsTu8i8nzDM5x7TFU; cquid=||; sid=6P-Q0M5JnJ7DkXYdtmRrKmF4_SFRw7fuTpg; dwanonymous_7254072e2668c23dc3bf6cca213a6657=abnysdNnyIsTu8i8nzDM5x7TFU; _pxhd=Sw7Si9dyRI1lRJ54r9krdPdV8oxqwBbhCnbbU7czHMaH2ZCD2Ikc9lKCnkyWpbfmlpUQ0kXO8qBv5jBrO6duIg==:WZBPcijC5RWYlVPnuPRXEOJt09N5NxxEigwUW-CrMUjBDWLfib7UuVg/b0TgQJmtKbel7VJ0wAWsBVGlzFO3ud0g8u2dTsRsH/F9bso/G-E=; __anact=%5B%7B%22activityType%22%3A%22viewSearch%22%2C%22parameters%22%3A%7B%22cookieId%22%3A%22%22%2C%22userId%22%3A%22%22%2C%22searchText%22%3A%221295739%22%2C%22suggestedSearchText%22%3A%22__UNDEFINED__%22%2C%22products%22%3A%5B%5D%2C%22showProducts%22%3Afalse%2C%22personalized%22%3Atrue%2C%22refinements%22%3A%22%5B%5D%22%2C%22searchID%22%3A%22099339d6-c424-474a-9071-ba1e42aadb0f%22%2C%22locale%22%3A%22en_US%22%2C%22queryLocale%22%3A%22en_US%22%2C%22realm%22%3A%22BCVK%22%2C%22siteId%22%3A%22US%22%2C%22instanceType%22%3A%22prd%22%7D%7D%5D; __cq_dnt=0; dw_dnt=0; __cqact=%5B%7B%22activityType%22%3A%22viewSearch%22%2C%22parameters%22%3A%7B%22cookieId%22%3A%22%22%2C%22userId%22%3A%22%22%2C%22searchText%22%3A%221295739%22%2C%22suggestedSearchText%22%3A%22__UNDEFINED__%22%2C%22products%22%3A%5B%5D%2C%22showProducts%22%3Afalse%2C%22personalized%22%3Atrue%2C%22refinements%22%3A%22%5B%5D%22%2C%22searchID%22%3A%22099339d6-c424-474a-9071-ba1e42aadb0f%22%2C%22locale%22%3A%22en_US%22%2C%22queryLocale%22%3A%22en_US%22%2C%22realm%22%3A%22BCVK%22%2C%22siteId%22%3A%22US%22%2C%22instanceType%22%3A%22prd%22%7D%7D%5D; notice_behavior=implied,eu; emailSubscribeCookie=second; consentCookie=first; utag_main=v_id:018642fba1d2007535f436a5767805054004200f00942$_sn:1$_se:3$_ss:0$_st:1676162848388$ses_id:1676161032658%3Bexp-session$_pn:3%3Bexp-session; bfx.apiKey=41a1f990-a119-11ea-9767-f9dfebd38fce; bfx.env=PROD; bfx.logLevel=ERROR; _px_f394gi7Fvmc43dfg_user_id=OTkwZTRkMjEtYWE2YS0xMWVkLWI0NWItZDU0YWFjZGY3MDdi; bfx.country=US; bfx.currency=USD; bfx.language=es; bfx.isInternational=false; bfx.sessionId=7be7e8c4-7afb-4c8c-ad69-bff6172ad449; ua-experience-plp=salesforce; UAVisitorType=guest; BVBRANDID=b991a91d-75e0-41d9-8f0b-b93b2ce12822; BVBRANDSID=ad6de37d-842f-4cf2-b4a7-eb27f5c821b3; s_fid=45E76AE22B025A1E-30B7567530E7FCB8; s_sq=underarmourtealiumdev%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fwww.underarmour.com%25252Fen-us%25252Fc%25252Fshoes%25252F%2526link%253DUnisex%252520UA%252520SlipSpeed%2525E2%252584%2525A2%252520Training%252520Shoes%2526region%253D3027057%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fwww.underarmour.com%25252Fen-us%25252Fc%25252Fshoes%25252F%2526oid%253Dhttps%25253A%25252F%25252Fwww.underarmour.com%25252Fen-us%25252Fp%25252Ftraining%25252Funisex_ua_slipspeed_training_shoes%25252F3027057.html%25253Fdwvar_3%2526ot%253DA; ak_bmsc=A48C9CA45534F7476B908B7036C2C9E5~000000000000000000000000000000~YAAQPdcwF0zCKjCGAQAAEOD7QhILfNJPQEUx/mG9cEzI+h8Gd0foK2iYuLP5TcnPHBiu6hWG9mMFledgCkpbkzLVKRGHTB/7yHLURf2vkINez+QgR1lxXAjki7kONQQHWe9MJLGlXlSccgYvEoMtij+Ukp8JIkds6uF4RRCzRW810I7d/mtuHAEcDiy3cnVvdWUdzJ7Y7qyG/9hbvVYHzT2iBP+XAgsMhjb4dn76yHj6eulQXoEFl98GZD5YkieyTfErITD5WnvDJGo7Ner8A+84M6TY7IVdjEMFXOj8iG1uxd4Hz0J/LVyTInD4231yQ1Sg4Apm+iKmXRCefhKztb2IzTzqEHZWWFCGTSYUMjwA//4r+A/ZAOi2tYPozolDo9xqsVP6yBysQz6eDLGu; BVImplmain_site=2471',
#     'Upgrade-Insecure-Requests': '1',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     # Requests doesn't support trailers
#     # 'TE': 'trailers',
# }

# params = {
#     'dwvar_3027057_color': '001',
#     'start': '0',
#     'breadCrumbLast': 'Shoes',
# }

# response = requests.get(
#     'https://www.underarmour.com/en-us/p/training/unisex_ua_slipspeed_training_shoes/3027057.html',
#     params=params,
#     cookies=cookies,
#     headers=headers,
# )

# url = 'https://golfwang.com/collections/new/products/logo-puffy-jacket-by-golf-wang?variant=42362847133868'
# cookies =cookiehead[0]
# headers =cookiehead[1]

# new_cookie = cookiehead.cookies
# new_header = cookiehead.headers

cookie , header = cookiehead.get_cookies_and_headers('https://golfwang.com/collections/all')

def imagescrape(url):
    response = requests.get(url, headers=header, cookies=cookie)
    # url = '' + url + ''
    # r = requests.get(url)

    #### option 1 for generalized

    # soup = BeautifulSoup(r.text, 'html.parser')

    #### option 2 for specific targeted site

    soup = BeautifulSoup(response.content,'html.parser')

    # test if we are sucessfully accesing page
    print(soup.title.text,"\n")

    images = soup.findAll('img',{"src":True})
    

    # gives a bunch of elements but not what we want
    # print(images)

    for image in images:
        # gives list of image links
        name = image['alt']
        url_link = image['src']
        #for shopify sites(golfwang)
        # full_link = 'http:' + url_link 
        # get rid of trailing // in link
        # url_link = url_link.replace('//','')

        print(name,url_link,'\n')

        # print(full_link,'\n')

    # downloads images to current directory
        # with open(name.replace(' ', '-').replace('/','') + '.jpg', 'wb') as f:
        #     im = requests.get(full_link)
        #     f.write(im.content)


    # '//cdn.shopify.com/s/files/1/0412/0133/6481/products/FW22LOGOPUFFYJACKET-BROWN_300x300.jpg?v=1675797870'
    # http:////cdn.shopify.com/s/files/1/0412/0133/6481/products/FW22LOGOPUFFYJACKET-BROWN_300x300.jpg?v=1675797870?

imagescrape('https://golfwang.com/collections/all')