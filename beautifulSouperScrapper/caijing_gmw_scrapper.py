# from bs4 import BeautifulSoup
# import requests
# import json
# import re
#
# visited_Urls = set()
# # base_Url = 'http://caijing.com.cn/index.html'
# base_Url = 'http://www.caijing.com.cn/original/'
# # base_Url = 'http://auto.caijing.com.cn/2022/0420/4855019.shtml'
# # base_Url = 'http://stock.caijing.com.cn/20210820/4789845.shtml'
# url_Scope = 'caijing.com'
# output_name = 'caijing_titles2.json'
# urls = []
# max_page_count = 0
# output = []
#
# # def isClickBait(title):
# #     prob = 0
# #     if "没" in title:
# #         prob = prob + 0.30
# #     if "险" in title:
# #         prob = prob + 0.30
# #     if "惊" in title:
# #         prob = prob + 0.30
# #     if "呆" in title:
# #         prob = prob + 0.30
# #     if "震" in title:
# #         prob = prob + 0.30
# #     if "撼" in title:
# #         prob = prob + 0.30
# #     if "吓" in title:
# #         prob = prob + 0.30
# #     if "傻" in title:
# #         prob = prob + 0.30
# #     if "骗" in title:
# #         prob = prob + 0.30
# #     if "爆" in title:
# #         prob = prob + 0.30
# #     if "财富" in title:
# #         prob = prob + 0.30
# #     if "密码" in title:
# #         prob = prob + 0.30
# #     if "译局" in title:
# #         prob = prob + 0.30
# #     if "破" in title:
# #         prob = prob + 0.30
# #     if "打" in title:
# #         prob = prob + 0.30
# #     if "千万" in title:
# #         prob = prob + 0.30
# #     if "罚" in title:
# #         prob = prob + 0.30
# #     if "谨记" in title:
# #         prob = prob + 0.30
# #     if "不" in title:
# #         prob = prob + 0.30
# #     if "了" in title:
# #         prob = prob + 0.30
# #     if "香" in title:
# #         prob = prob + 0.30
# #     if "吃" in title:
# #         prob = prob + 0.30
# #     if "定" in title:
# #         prob = prob + 0.30
# #     if "好" in title:
# #         prob = prob + 0.30
# #     if "严" in title:
# #         prob = prob + 0.30
# #     if "极" in title:
# #         prob = prob + 0.30
# #     if "端" in title:
# #         prob = prob + 0.30
# #     if "拒" in title:
# #         prob = prob + 0.30
# #     if "绝" in title:
# #         prob = prob + 0.30
# #     if "巨" in title:
# #         prob = prob + 0.30
# #     if "大" in title:
# #         prob = prob + 0.30
# #     if "快" in title:
# #         prob = prob + 0.30
# #     if "看" in title:
# #         prob = prob + 0.30
# #     if "坏" in title:
# #         prob = prob + 0.30
# #     if "偷" in title:
# #         prob = prob + 0.30
# #     if "逃" in title:
# #         prob = prob + 0.30
# #
# #     if "!" in title:
# #         prob = prob + 0.60
# #     if "！" in title:
# #         prob = prob + 0.60
# #     if "?" in title:
# #         prob = prob + 0.60
# #     if "？" in title:
# #         prob = prob + 0.60
# #     if "。。。" in title:
# #         prob = prob + 0.60
# #     if "..." in title:
# #         prob = prob + 0.60
# #     if "危" in title:
# #         prob = prob + 0.60
# #     if "天呀" in title:
# #         prob = prob + 0.60
# #     if "一口气" in title:
# #         prob = prob + 0.60
# #     if "秘密" in title:
# #         prob = prob + 0.60
# #     if "暴跌" in title:
# #         prob = prob + 0.60
# #     if "暴涨" in title:
# #         prob = prob + 0.60
# #     if "骗局" in title:
# #         prob = prob + 0.60
# #     if "居然" in title:
# #         prob = prob + 0.60
# #     if "切记" in title:
# #         prob = prob + 0.60
# #     if "解密" in title:
# #         prob = prob + 0.60
# #     if "揭秘" in title:
# #         prob = prob + 0.60
# #     if "慌" in title:
# #         prob = prob + 0.60
# #     if "注意" in title:
# #         prob = prob + 0.60
# #     if "小心" in title:
# #         prob = prob + 0.60
# #
# #
# #     if prob >= 0.6:
# #         global max_page_count
# #         print(max_page_count)
# #         max_page_count = max_page_count + 1
# #         return True
# #     else:
# #         return False
#
# def search(url,depth):
#     global max_page_count
#
#     if "2015" in url or "2014" in url or "2016" in url or "2017" in url or "2018" in url:
#         return
#
#     if url in visited_Urls:
#         return
#
#     if depth == 800:
#         print("depth reached")
#         return
#
#     if max_page_count == 30000:
#         return
#
#     # 有些网页限制了访问，可能会失败
#     try:
#         webpage = requests.get(url)
#     except:
#         visited_Urls.add(url)
#         return
#
#     print(url)
#
#     webpage.encoding = 'utf-8'
#     soup = BeautifulSoup(webpage.text, 'html.parser')
#
#     if re.match(r'http://[a-z]+\.caijing\.com\.cn/[0-9]+/[0-9]+\.shtml', url) or re.match(r'http://[a-z]+\.caijing\.com\.cn/[0-9]+/[0-9]+/[0-9]+\.shtml', url):
#         title = None
#         for temp in soup.head.find_all('title'):
#             title = temp
#         print(title)
#         temp = str(title)
#         if temp == None or "页面未找到-财经网" in temp or "404 Not Found" in temp:
#             print("no title")
#             return
#         else:
#             # if isClickBait(str(title)):
#             #     content = None
#             #     for div in soup.find_all('div'):
#             #         if (div.has_attr('class') and div['class'] == ['article-content']) or (
#             #                 div.has_attr('id') and div['id'] == 'the_content'):
#             #             content = div
#             #             break
#             #     if content != None:
#             #         article = ''.join(p.text.strip() for p in content.find_all('p'))
#             #     else:
#             #         return
#             #     output.append({'id': max_page_count, 'title': str(title), 'article': article, 'url': url})
#             output.append({'url': url})
#             max_page_count = max_page_count + 1
#             print(max_page_count)
#
#
#     elif re.match(r'http://m\.caijing\.com\.cn/article/[0-9]', url):
#         title = None
#         for temp in soup.head.find_all('title'):
#             title = temp
#
#         print(title)
#         temp = str(title)
#         if temp == None or "页面未找到-财经网" in temp or "404 Not Found" in temp:
#             print("no title")
#             return
#         else:
#             # if isClickBait(str(title)):
#             #     content = None
#             #     for div in soup.find_all('div'):
#             #         if (div.has_attr('class') and div['class'] == ['article-content']) or (
#             #                 div.has_attr('id') and div['id'] == 'the_content'):
#             #             content = div
#             #             break
#             #     if content != None:
#             #         article = ''.join(p.text.strip() for p in content.find_all('p'))
#             #     else:
#             #         return
#             #     output.append({'id': max_page_count, 'title': str(title), 'article': article, 'url': url})
#             output.append({'url': url})
#             max_page_count = max_page_count + 1
#             print(max_page_count)
#
#     visited_Urls.add(url)
#     for link in soup.find_all('a'):
#         nxt_url = link.get('href')
#         if nxt_url != None and url_Scope in nxt_url:
#             search(nxt_url,depth+1)
#
#     print("end node")
#     return
#
# search(base_Url,0)
#
# json.dump(output, open(output_name, 'w', encoding='utf-8'), ensure_ascii=False, indent=4)


from bs4 import BeautifulSoup
import requests
import json
import re

visited_Urls = set()
base_Url = 'https://kepu.gmw.cn/agri/2022-03/01/content_35555484.htm'
# base_Url = 'https://www.gmw.cn/'
url_Scope = 'gmw.cn'
output_name = 'clickbait_titles_gmw.json'
urls = []
max_page_count = 0
output = []


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
    if "警告" in title:
        prob = prob + 0.60

    if prob >= 0.6:
        global max_page_count
        print(max_page_count)
        max_page_count = max_page_count + 1
        return True
    else:
        return False


def search(url, depth):
    global max_page_count

    if url in visited_Urls:
        return

    if depth == 800:
        print("depth reached")
        return

    if max_page_count == 10000:
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
    if re.match(r'[a-z]+://[a-z]+\.gmw\.cn/[0-9]+-[0-9]+/[0-9]+/content_[0-9]+\.htm', url) or re.match(r'[a-z]+://[a-z]+\.gmw\.cn/[a-z]+/[0-9]+-[0-9]+/[0-9]+/content_[0-9]+\.htm', url) :
        temp = None
        flag = True
        for h1 in soup.find_all('h1'):
            if h1.has_attr('class'):
                if h1['class'] == ['u-title'] or h1['class'] == ['articleTitle']:
                    temp = h1
                    flag = False
                    break
        if flag:
            for div in soup.find_all('div'):
                if div.has_attr('class'):
                    if div['class'] == ['m-title']:
                        temp = div
                        break

        if temp == None:
            print("no title")
        else:
            title = temp.text.strip()
            content = None
            for div in soup.find_all('div'):
                if div.has_attr('class'):
                    if div['class'] == ['u-mainText'] or div['class'] == ['m-left-text'] or div['class'] == ['contentMain']:
                        content = div
                        break
            if content != None:
                article = ''.join(p.text.strip() for p in content.find_all('p'))
                output.append({'id': max_page_count, 'title': title, 'article': article, 'url': url})
                print(max_page_count)
                max_page_count = max_page_count + 1
            else:
                print('no content')

    visited_Urls.add(url)

    for link in soup.find_all('a'):
        nxt_url = link.get('href')
        if nxt_url != None and re.match(r'[a-z]+://[a-z]+\.gmw\.cn', nxt_url) and nxt_url != 'https://www.gmw.cn/03rili/sh2000gb.htm' and 'filedownload' not in nxt_url and 'photo.gmw' not in nxt_url and 'topics.gmw' not in nxt_url and 'm.gmw' not in nxt_url and 'en.gmw' not in nxt_url and 'jyj.gmw' not in nxt_url and 'epaper' not in nxt_url and 'pic' not in nxt_url and 'default.htm' not in nxt_url:
            search(nxt_url, depth + 1)

    print("end node")
    return


search(base_Url, 0)

json.dump(output, open(output_name, 'w', encoding='utf-8'), ensure_ascii=False, indent=4)
