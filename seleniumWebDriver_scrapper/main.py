# find links of tencent news
# for every link searched, find more possible links
# collect title and article if it is an article
# remaining links will be stored and can be pass to tencent_news.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os.path
import json
from time import time

source = "https://news.qq.com/"
max_number = 2000  # max number of links to search
store_links = "links1.txt"
output_name = "tencent_news2.json"

if os.path.exists(store_links):  # read previous links
    with open(store_links, encoding="utf-8") as file:
        urls_get = set(s[:-1] if s[-1] == "\n" else s for s in file.readlines())
else:
    urls_get = {source}

urls_searched = set()
output = []

if os.path.exists(output_name):  # read previous output
    with open(output_name, encoding="utf-8") as file:
        output = json.load(file)

# web driver
driver = webdriver.Edge("C:/Users/Johnny Song/edgedriver_win64/msedgedriver.exe")


def find_links(url: str):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "a")))
    urls_searched.add(url)  # store searched links
    links = driver.find_elements(By.TAG_NAME, "a")

    # find more links
    hrefs = [l.get_attribute("href") for l in links]
    for href in hrefs:
        if href and "new.qq.com" in href:  # find a link
            if "omv" in href or "video" in href: continue  # filter
            if href in urls_get: continue
            if href in urls_searched: continue
            urls_get.add(href)
            print(href)

    # find title and content
    title = driver.title
    if not title: return
    if len(title) > 5 and title[-5:] == "_腾讯新闻":
        title = title[:-5]
    else:
        return

    text = driver.find_element(By.CLASS_NAME, "content-article")
    if not text: return
    article = ''
    for p in text.find_elements(By.TAG_NAME, "p"):
        t = p.text.strip()
        if t:
            article += t
    if not article: return
    print(title)
    return title, article


count = len(output)
c0 = count
t0 = time()
try:
    for i in range(max_number):
        if not urls_get: break
        link = urls_get.pop()
        try:
            result = find_links(link)
            if result:
                output.append({"id": count, "title": result[0], "article": result[1], "url": link})
                count += 1
        except Exception as E:
            print("error:", link, E)
finally:
    driver.close()
    # save the remaining links for later use
    with open(store_links, "w", encoding="utf-8") as file:
        for l in urls_get:
            file.write(l + "\n")
        print("saved", len(urls_get), "links")

    # output titles and articles to file
    json.dump(output, open(output_name, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=4)
    print("get", len(output) - c0, "articles")
    t = time() - t0
    print("used", t, "seconds")

    # import tencent_news  # use tencent_news.py to process remaining links

'''
#webpage = requests.get(source)
#webpage.encoding = "GB2312"
soup = BeautifulSoup(page_source, 'html.parser')

channel = soup.find("div",{"class":"channel_mod"})

#with open("tencentnews1.txt", encoding="utf-8") as file:
#    print(file.encoding)
#    website = file.read()

#soup = BeautifulSoup(website, 'html.parser')
for a in channel.find_all("a"):
    link = a["href"]
    print(link)
    if link[:18] == "https://new.qq.com":
        urls_get.add(link)

print(len(urls_get))'''
