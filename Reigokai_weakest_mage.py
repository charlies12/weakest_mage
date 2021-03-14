import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://isekailunatic.com/category/weakest-mage/")
soup = BeautifulSoup(page.content, 'html.parser')

# Searches main page for chapters
title = soup.find(id="main")
title_items = title.find_all(class_="entry-title")
current = title_items[0]

# Date posted on 
posted_on = title.find_all(class_="entry-meta")
current_post = posted_on[0]

# Selects date
date_tag = title.select("time.entry-date")
simple_date = [dts.get_text() for dts in date_tag]

# Searches for url
search_url = title.select(".entry-title a[href]")
url_link = [ul.get('href') for ul in search_url]

# Searches for chapter number and title
chapter_header = title.select("h1.entry-title")
tag = [ch.get_text() for ch in chapter_header]

chapter_details = pd.DataFrame(
    {
        "Title": tag,
        "URL": url_link,
        "Posted-on": simple_date
    }
)

print(chapter_details)



# Things that didn't work how I wanted

# This only searches 1 link. Not used, but will leave here.
# url_description = current.find('a')
# url_short_description = url_description['href']

# Searches URLs that start with 'https'
# Actually, this doesn't do what I want it to do. I'll leave it here.
# link_description = title.select("a[href^='https']")
# just_link = [ld.get_text() for ld in link_description]

# column alignment and column width
# pd.set_option('display.max_colwidth', 100)
# chapter_details.style.set_properties(subset=["col1", "col2"], **{'text-align': 'left'})





