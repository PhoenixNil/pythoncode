# Optimized version of the code
from bs4 import BeautifulSoup
import requests
import socket

# Function to send HTTP GET request and parse the webpage content
def get_links_from_url(url, is_zhihu=False):
    response = requests.get(url)
    domain_set = set()

    # Check if the request is successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        links = []

        # Find all the links
        if is_zhihu:
            class_element = soup.find(class_="RichText ztext Post-RichText css-1g0fqss")
            if class_element:
                links = class_element.find_all("a")
        else:
            links = soup.find_all("a")

        for link in links:
            domain = link.get("href")
            if "google" in domain:
                if is_zhihu:
                    domain = domain.replace("https://link.zhihu.com/?target=https%3A//", "")
                if len(domain) < 30:
                    domain_set.add(domain.replace("https://", "").rstrip("/"))
    else:
        print(f"Request to {url} failed, error code: {response.status_code}")

    return domain_set

# Get IP address of google safe search
domain = "forcesafesearch.google.com"
ip = socket.gethostbyname(domain)

# URLs to send HTTP GET request
url1 = "https://www.fobnotes.com/tools/google-global-country-sites/"
url2 = "https://zhuanlan.zhihu.com/p/83273024"

# Get the domains from the URLs
domains = get_links_from_url(url1)
domains.update(get_links_from_url(url2, is_zhihu=True))

# Generate the address domain list
address_domain = [f"{ip} {domain} #forcesafesearch" for domain in domains]

# Sort the address domain list
sorted_address_domain = sorted(address_domain)

for domain in sorted_address_domain:
    print(domain)