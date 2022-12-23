from bs4 import BeautifulSoup
import requests
import json
import re

output_name = 'output.json'
output = []
max_page_count = 0

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

def search(url):
    try:
        webpage = requests.get(url)
    except:
        print("error loading page")
        return

    print(url)

    webpage.encoding = 'utf-8'
    soup = BeautifulSoup(webpage.text, 'html.parser')

    if re.match(r'http://[a-z]+\.caijing\.com\.cn/[0-9]+/[0-9]+\.shtml', url) or re.match(r'http://[a-z]+\.caijing\.com\.cn/[0-9]+/[0-9]+/[0-9]+\.shtml', url):
        title = None
        for temp in soup.head.find_all('title'):
            title = temp
        print(title)
        if isClickBait(str(title)):
            content = None
            for div in soup.find_all('div'):
                if (div.has_attr('class') and div['class'] == ['article-content']) or (
                        div.has_attr('id') and div['id'] == 'the_content'):
                    content = div
                    break
            if content != None:
                article = ''.join(p.text.strip() for p in content.find_all('p'))
                output.append({'id': max_page_count, 'title': str(title), 'article': article, 'url': url})
            else:
                pass
        else:
            pass

    elif re.match(r'http://m\.caijing\.com\.cn/article/[0-9]', url):
        title = None
        for temp in soup.head.find_all('title'):
            title = temp
        print(title)
        if isClickBait(str(title)):
            content = None
            for div in soup.find_all('div'):
                if (div.has_attr('class') and div['class'] == ['articleText']):
                    content = div
                    break
            if content != None:
                article = ''.join(p.text.strip() for p in content.find_all('p'))
                output.append({'id': max_page_count, 'title': str(title), 'article': article, 'url': url})
            else:
                pass
        else:
            pass

with open("/Users/hengwei/PycharmProjects/clickbait_filter/input.json", "r") as json_file:
    data = json.load(json_file)
    for url in data:
        search(str(url["url"]))

    json.dump(output, open(output_name, 'w', encoding='utf-8'), ensure_ascii=False, indent=4)
