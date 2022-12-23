from bs4 import BeautifulSoup
import requests
import json
import re

visited_Urls = set()
# base_Url = 'http://caijing.com.cn/index.html'
# base_Url = 'http://stock.caijing.com.cn/20220322/4848443.shtml'
base_Url = 'http://auto.caijing.com.cn/2022/0420/4855019.shtml'
# base_Url = 'http://stock.caijing.com.cn/20210820/4789845.shtml'
url_Scope = 'caijing.com'
output_name = '50000titles.json'
max_page_count = 0
output = []

def in_Scope(url)->bool:
    if re.match(r'http://[a-z]+\.caijing\.com\.cn/[0-9]+/[0-9]+\.shtml', url) or re.match(
        r'http://[a-z]+\.caijing\.com\.cn/[0-9]+/[0-9]+/[0-9]+\.shtml', url) or re.match(r'http://m\.caijing\.com\.cn/article/[0-9]', url):
        return True
    return False
def isClickBait(title):
    prob = 0
    if "没" in title:
        prob = prob + 0.30
    if "险" in title:
        prob = prob + 0.30
    if "惊" in title:
        prob = prob + 0.30
    if "呆" in title:
        prob = prob + 0.30
    if "震" in title:
        prob = prob + 0.30
    if "撼" in title:
        prob = prob + 0.30
    if "吓" in title:
        prob = prob + 0.30
    if "傻" in title:
        prob = prob + 0.30
    if "骗" in title:
        prob = prob + 0.30
    if "爆" in title:
        prob = prob + 0.30
    if "财富" in title:
        prob = prob + 0.30
    if "密码" in title:
        prob = prob + 0.30
    if "译局" in title:
        prob = prob + 0.30
    if "破" in title:
        prob = prob + 0.30
    if "打" in title:
        prob = prob + 0.30
    if "千万" in title:
        prob = prob + 0.30
    if "罚" in title:
        prob = prob + 0.30
    if "谨记" in title:
        prob = prob + 0.30
    if "不" in title:
        prob = prob + 0.30
    if "了" in title:
        prob = prob + 0.30
    if "香" in title:
        prob = prob + 0.30
    if "吃" in title:
        prob = prob + 0.30
    if "定" in title:
        prob = prob + 0.30
    if "好" in title:
        prob = prob + 0.30
    if "严" in title:
        prob = prob + 0.30
    if "极" in title:
        prob = prob + 0.30
    if "端" in title:
        prob = prob + 0.30
    if "拒" in title:
        prob = prob + 0.30
    if "绝" in title:
        prob = prob + 0.30
    if "巨" in title:
        prob = prob + 0.30
    if "大" in title:
        prob = prob + 0.30
    if "快" in title:
        prob = prob + 0.30
    if "看" in title:
        prob = prob + 0.30
    if "坏" in title:
        prob = prob + 0.30
    if "偷" in title:
        prob = prob + 0.30
    if "逃" in title:
        prob = prob + 0.30

    if "!" in title:
        prob = prob + 0.60
    if "！" in title:
        prob = prob + 0.60
    if "?" in title:
        prob = prob + 0.60
    if "？" in title:
        prob = prob + 0.60
    if "。。。" in title:
        prob = prob + 0.60
    if "..." in title:
        prob = prob + 0.60
    if "危" in title:
        prob = prob + 0.60
    if "天呀" in title:
        prob = prob + 0.60
    if "一口气" in title:
        prob = prob + 0.60
    if "秘密" in title:
        prob = prob + 0.60
    if "暴跌" in title:
        prob = prob + 0.60
    if "暴涨" in title:
        prob = prob + 0.60
    if "骗局" in title:
        prob = prob + 0.60
    if "居然" in title:
        prob = prob + 0.60
    if "切记" in title:
        prob = prob + 0.60
    if "解密" in title:
        prob = prob + 0.60
    if "揭秘" in title:
        prob = prob + 0.60
    if "慌" in title:
        prob = prob + 0.60
    if "注意" in title:
        prob = prob + 0.60
    if "小心" in title:
        prob = prob + 0.60


    if prob >= 0.6:
        global max_page_count
        print(max_page_count)
        max_page_count = max_page_count + 1
        return True
    else:
        return False

def search(url,depth):
    global max_page_count
    if url in visited_Urls:
        return

    if depth == 600:
        print("depth reached")
        return
    # stops recursion
    if max_page_count == 45000:
        return

    # 有些网页限制了访问，可能会失败
    try:
        webpage = requests.get(url)
    except:
        visited_Urls.add(url)
        return

    print(url)

    webpage.encoding = 'utf-8'
    soup = BeautifulSoup(webpage.text, 'html.parser')

    visited_Urls.add(url)

    title = None
    for temp in soup.head.find_all('title'):
        title = temp
    print(title)
    if title != None and title != "页面未找到-财经网" and title != "404 Not Found" and in_Scope(url):
        if isClickBait(str(title)):
            output.append({'url': url})
            # 每次output一个网页的时候，之前的网页就丢失了
            # json.dump(output, open(output_name, 'w', encoding='utf-8'), ensure_ascii=False, indent=4)
    else:
        # 遇到了意外情况，把网页收集起来，逐个分析
        pass

    for link in soup.find_all('a'):
        nxt_url = link.get('href')
        if nxt_url != None and url_Scope in nxt_url:
            search(nxt_url,depth+1)

    print("end node")
    return

search(base_Url,0)
json.dump(output, open(output_name, 'w', encoding='utf-8'), ensure_ascii=False, indent=4)