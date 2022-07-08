# ptt八卦版詳細資訊
import requests as req
from bs4 import BeautifulSoup


def sent_req(url):

    root = req.get(url, headers=header)
    html_text = BeautifulSoup(root.text, "lxml")
    articles = html_text.select("div.r-ent")
    return html_text, articles


def parse_data(articles):

    for article in articles:

        # 標題
        title = article.select("div.title")[0].text.strip()

        if "公告" in title or "刪除" in title:
            continue

        file.write(f"標題 : {title}\n")

        # 作者
        author = article.select("div.author")[0].text
        file.write(f"作者 : {author}\n")

        # 推數
        push_num = article.select("div.nrec")[0].text.strip()
        file.write(f"推數 : {push_num if len(push_num)>0 else '0'} \n")

        # 日期
        date = article.select("div.date")[0].text.strip()
        file.write(f"日期 : {date}\n")

        # 連結
        raw_url = article.select("div.title a")[0]["href"]
        file.write(f"連結 : {domain_name+raw_url}\n\n")


url = "https://www.ptt.cc/bbs/Gossiping/index.html"
domain_name = "https://www.ptt.cc/"

header = {
    'cookie': 'over18=1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

page_num = eval(input("輸入頁數："))

with open("ptt八卦版詳細資訊.txt", "w", encoding="utf-8") as file:

    for page in range(page_num):
        html_text, tmp = sent_req(url)
        parse_data(tmp)
        print(html_text.prettify()) #第二頁被擋住
        next_link = html_text.find("a", text="‹ 上頁").get("href")
        url = domain_name+next_link
