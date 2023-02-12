import requests
import pprint

def get_cookies_and_headers(url):
    # pp = pprint.PrettyPrinter(indent=4)

    # Make a request to the website
    # print("hi")
    response = requests.get(url)
    # print(response)
    
    # Extract the cookies and headers from the response
    cookies = response.cookies
    # pp.pprint(cookies)
    headers = response.headers
    # pp.pprint(headers)
    
    # Return the cookies and headers
    return cookies,headers

# get_cookies_and_headers('https://golfwang.com/collections/all')

