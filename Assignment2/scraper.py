#-------------------------------------------------------------------------
# AUTHOR: Shinhwa Kim
# FILENAME: scraper.py
# SPECIFICATION: Crawl the Circular Links pages and print headings and seen URLs.
# FOR: CS 4250 - Assignment #2
# TIME SPENT: 45min-1hr
#-------------------------------------------------------------------------

# Importing Python libraries
import requests
from bs4 import BeautifulSoup

# Defining the seed URL
seed = "https://testingurl.dev/scraping/links/circular"
baseURL = "/".join(seed.split("/")[:3])

# Creating the frontier and seen collections
frontier = [seed]  # URLs waiting to be crawled, in first-in-first-out order
seen = {seed}     # URLs already discovered, including those still in frontier


# Crawling until the frontier is empty
while frontier:

    # Removing the first URL from the frontier
    url = frontier.pop(0)


    # Retrieving and parsing the Web page
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")


    # Printing the text contained in the <h1> element
    h1 = soup.find("h1")
    if h1:
        print(h1.get_text(strip=True))


    # Extracting and processing hyperlinks
    for link in soup.find_all("a", href=True):
        href = link["href"]

        if href.startswith("http://") or href.startswith("https://"):
            absolute_url = href
        elif href.startswith("/"):
            absolute_url = baseURL + href
        else:
            current_directory = url.rsplit("/", 1)[0]
            absolute_url = current_directory + "/" + href

        if absolute_url.startswith(seed) and absolute_url not in seen:
            seen.add(absolute_url)
            frontier.append(absolute_url)


# Printing all URLs in seen
print("\nURLs in seen:")
for url in sorted(seen):
    print(url)
