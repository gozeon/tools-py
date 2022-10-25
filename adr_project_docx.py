import os
from datetime import date

from markdownify import markdownify as md
import requests
import pypandoc


api_url = os.getenv("api_url")
project_id = os.getenv("project_id")
author =  os.getenv("author")

# 获取项目
response = requests.get("{}/api/project/{}".format(api_url, project_id))
project_res = response.json()
project_info = project_res['data']

# 获取记录
response = requests.get("{}/api/record/{}".format(api_url, project_id))
record_res = response.json()
record_info = record_res['data']

# 写入
text = []

p_title = project_info['title']
text.append("""

---
title: {title}
author: {author}
date: {date}
subject: {description}
---

""".format(title=p_title, author=author, date=date.today().isoformat(), description=project_info['description']))

for record in record_info:
    if record["status"] == 1:
        text.append("# " + record["title"] + '\n\n')
        text.append(md(record["description"]))


# print(text)
o_pdf = "{}.pdf".format(p_title)

extra_args=["--pdf-engine=xelatex", "--standalone","--toc", "--number-sections", "--template=templates/eisvogel.tex", "-V","CJKmainfont=Microsoft YaHei UI" ]
pypandoc.convert_text("".join(text), to='pdf', format='md', outputfile=o_pdf, extra_args=extra_args)
