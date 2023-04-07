import feedparser
import datetime

tistory_blog_uri = "https://only-wanna.tistory.com"  # Your blog address here
feed = feedparser.parse(tistory_blog_uri+"/rss")

markdown_text = """
##### Recent blog posts
"""

lst = []
post_cnt = 0
# 블로그 포스트 불러오기
for i in feed['entries']:
    if i['tags'][0]['term'] != "문제 풀이":
        post_cnt += 1
        dt = datetime.datetime.strptime(
            i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%Y.%m.%d")
        markdown_text += f"- [{dt} {i['title']}]({i['link']}) <br>\n"
        print(i['link'], i['title'])
    if post_cnt == 4:
        break

# Hits, capsul-render
markdown_text += """
<p align="center">
<img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FWoodywarhol9%2Fwoodywarhol9&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false" />
</p>

<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=timeAuto&height=100&section=footer" />
</p>
"""

with open("README.md", mode="w", encoding="utf-8") as readme:
    with open("intro.md", mode="r", encoding="utf-8") as intro:
        readme.write(intro.read() + "\n")
        readme.write(markdown_text)
