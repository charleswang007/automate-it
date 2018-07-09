import requests
from bs4 import BeautifulSoup

target_url = 'https://www.suse.com/c/news/'
print('Start parsing news ...')
rs = requests.session()
res = rs.get(target_url, verify=False)
#res.encoding = 'utf8'
soup = BeautifulSoup(res.text, 'html.parser')
content = ""
date_lst = []
subject_lst = []

for i in soup.select('div .col-sm-3 p.date'):
    date_lst.append(i.getText())
for j in soup.select('div .col-sm-8 .content'):
    subject_lst.append(j.getText())
for k in range(len(date_lst)):
    content += u'\u2022' + " " + date_lst[k].replace('\t','').replace('\n','') + '\n'
    if k != len(date_lst) - 1:
        content += subject_lst[k].replace('\n','') + '\n\n'
    else:
        content += subject_lst[k].replace('\n','')
print content