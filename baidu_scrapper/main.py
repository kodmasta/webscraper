import requests
from bs4 import BeautifulSoup
import sys
from time import time
from openpyxl import workbook
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

max_page_count = 0

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    'Host': 'www.baidu.com'
}
headers1 = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    'Host': 'baijiahao.baidu.com'
}

def get_connect(link):
    try:
        r = requests.get(link, headers=headers)
        if 200 != r.status_code:
            return None
        url_list = []
        soup = BeautifulSoup(r.text, "lxml")
        div_list = soup.find_all('div', class_='result-op c-container xpath-log new-pmd')
        for div in div_list:
            mu = div['mu'].strip()
            url_list.append(mu)
            print(mu)
        return get_content(url_list)
    except Exception as e:
        print('e.message:\t', e)
    finally:
        print(u'go ahead!\n\n')



def get_content(url_list):
    global max_page_count
    try:
        for url in url_list:
            # r1 = requests.get(url, timeout=10)
            # r1.encoding = 'utf-8'
            # soup1 = BeautifulSoup(r1.text, "lxml")
            # temp = soup1.select('title')
            # title = temp[0].get_text().strip()
            # article = None
            # paragraphs = []
            # for div in soup1.find_all('div', attrs={"class":"index-module_textWrap_3ygOc"}):
            #     paragraphs.append(''.join(p.text.strip() for p in div.find_all('p')))
            # article = ''.join('%s' % para for para in paragraphs)

            driver.get(url)
            title = driver.title
            if not title: return

            text = driver.find_elements(By.CLASS_NAME, "index-module_textWrap_3ygOc")
            article = ''
            for para in text:
                for p in para.find_elements(By.TAG_NAME, "p"):
                    t = p.text.strip()
                    if t:
                        article += t
            max_page_count = max_page_count + 1
            ws.append([max_page_count, title, article, url])
            print([title])
    except Exception as e:
        print("Error: ", e)
    finally:
        wb.save('keywords_Set5.xlsx')
        print(u'OK!\n\n')

if __name__ == '__main__':
    # keywords_Set1 = ['惊了','刚刚','警告','小心','突然','注意']
    # keywords_Set2 = ['慌了','居然','暴涨']
    # keywords_Set3 = ['秘密','危险','呆了','傻了','震撼','吓']
    # keywords_Set4 = ['绝了','切记','天呀','破防','完了','暴跌']
    # keywords_Set5 = ['新冠','军事','爱情','明星']
    keywords_Set5 = ['搜索概念','科研结果']
    wb = workbook.Workbook()
    ws = wb.active
    ws.append(['id', 'title', 'content', 'url'])
    for keyword in keywords_Set5:
        print(keyword)
        raw_url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd='+keyword+'&medium=2&x_bfe_rqs=20001&x_bfe_tjscore=0.000000&tngroupname=organic_news&newVideo=12&rsv_dl=news_b_pn&pn='
        for i in range(50):
            link = raw_url + str(i * 10)
            get_connect(link)
            print('page', i + 1)
            wb.save('keywords_Set5.xlsx')
    print('finished')
    wb.close()