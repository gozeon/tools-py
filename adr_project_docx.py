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
p_title = project_info['title']
html.append(E("h1", p_title))
html.append(E("i", project_info['description']))


for record in record_info:
    html.append(E("h3", record["title"]))
    html.append(E("div", record["description"]))

o_pdf = "{}.pdf".format(p_title)
pypandoc.convert_text("".join(html), to='md', format='html', outputfile="tmp.md", extra_args=["-s", "--toc"])

extra_args=["--pdf-engine=xelatex", "--toc", "-V","mainfont=Microsoft YaHei UI","-V", "title={}".format(p_title) ]
pypandoc.convert_file("tmp.md", to='pdf', format='md', outputfile=o_pdf, extra_args=extra_args)

os.remove("tmp.md")
