import requests
import urllib.request
import xlsxwriter
import csv
#import PyMySQL
from bs4 import BeautifulSoup



file = open('d:\\ignore.txt', 'r')
ignore = file.read().split()
#print(ignore)




page=requests.get('http://niituniversity.in')
# Create a BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')
for script in soup(["script","style"]):
    script.extract()
text = soup.get_text()
s="car ran after a dog but a dog ran very fast"
l=text.split()
x=set(l)
y=set(ignore)
x=x-y
l1=list(x)
d={}
for words in l1:
    f=l.count(words)
    d[words]=f
    print (f)
print(d)
k=list(d.values())
workbook = xlsxwriter.Workbook('d:\\graph.xlsx')
worksheet = workbook.add_worksheet()


chart1 = workbook.add_chart({'type':'column'})


s = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]
worksheet.write('A1', 'word')
worksheet.write('B1','frequency')
i=2
for k, v in s:
    worksheet.write('A'+str(i), k)
    worksheet.write('B'+str(i),v)
    i+=1
    if i>6:
        break
chart1.add_series({'values': '=Sheet1!$A2:B8'})
worksheet.insert_chart("D5",chart1)
workbook.close()

