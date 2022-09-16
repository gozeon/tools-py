import os
from turtle import ht

import requests
import pypandoc

api_url = os.getenv("api_url")
project_id = os.getenv("project_id")

# 获取项目
response = requests.get("{}/api/project/{}".format(api_url, project_id))
project_res = response.json()
project_info = project_res['data']

# 获取记录
response = requests.get("{}/api/record/{}".format(api_url, project_id))
record_res = response.json()
record_info = record_res['data']


def E(tag, text):
    return "<{tag}>{text}</{tag}>".format(tag=tag, text=text)


# 写入
html = []
html.append(E("h1", project_info['title']))
html.append(E("i", project_info['description']))


for record in record_info:
    html.append(E("h3", record["title"]))
    html.append(E("div", record["description"]))


pypandoc.convert_text("".join(html), to='md', format='html', outputfile="tmp.md", extra_args=["-s", "--toc"])
pypandoc.convert_file("tmp.md", to='pdf', format='md', outputfile="{}.pdf".format(project_info['title']), extra_args=["--pdf-engine=xelatex", "--toc", "-V","mainfont=Microsoft YaHei UI" ])

os.remove("tmp.md")
