import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://isekailunatic.com/category/weakest-mage/")
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="main")
# chapters = title.find_all(class_="entry-title")
chapters = title.find_all(class_="entry-header")
current_chapters = chapters[0]
# print(current_chapters)
# for chapter in chapters:
#     print(chapter)
# current_chapters = chapters

show = current_chapters.find("a")
desc = show['href']

# print(show)
# print(desc)

entry_title = title.select(".entry-title")
# link = title.select("href")
chapter_title = [ct.get_text() for ct in entry_title]
# periods2 = [pt2.get_text() for pt2 in link]
# print(chapter_title)

# short_descs = [sd.get_text() for sd in title.select(".site-content .href ")]
# temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
# descs = [d["title"] for d in seven_day.select(".tombstone-container img")]


show_chapters = pd.DataFrame(
    {
        "Chapter": chapter_title#,
        #"Link": periods2

    }
)


print(show_chapters)



# show_chapters.to_csv('weakest_mage.csv', index=False)








# print(current_chapters.prettify())

# chapter_title = current_chapters.find(class_="entry-header").get_text()
# chapter_link = current_chapters.find(a="href").get_text()
#
# print(chapter_title)
# print(chapter_link)

# img = current_chapters.find()

# show_me_the_tags = soup.find_all('h1', class_='entry-title')

# print(show_me_the_tags)

'''for tag in show_me_the_tags:
    print(tag)'''

# print(list(soup.children))
# info = [type(item) for item in list(soup.children)]
# print(info)

# html = list(soup.children)[2]

# print(list(html.children))


