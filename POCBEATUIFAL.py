import requests
from bs4 import BeautifulSoup

#target URL
url = "https://github.com"

# Fetch the web page content
response = requests.get(url)

if response.status_code == 200:
    # parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")
    # Extract and print the title
    print("Page Title:", soup.title.string)
    
    # Find and print all links on the domain
    for link in soup.find_all("a"):
        print(link.get("href"))
else:
    print("Failed to retrieve the web page.")
