from urllib import request
import nltk
from nltk import word_tokenize
from bs4 import BeautifulSoup
import timex
from nltk.tag import pos_tag
from nltk.tokenize import sent_tokenize
import re
from io import BytesIO
from PyPDF2 import PdfFileReader
import whenhubApi
url = "http://www.wayne.k12.ms.us/userfiles/191/Classes/1372/billgatesbiography1.pdf"
response = request.urlopen(url)
print(response.headers.get('content-type'))

if response.headers.get('content-type')=="application/html":
     print("y")
     html = request.urlopen(url).read().decode('utf8',errors='ignore')
     content = BeautifulSoup(html).get_text().decode('utf8',errors='ignore')
     
elif response.headers.get('content-type')=="application/pdf":
     raw = response.read()
     memoryFile = BytesIO(raw)
     pdf = PdfFileReader(memoryFile)
     content=pdf.getPage(0).extractText()+"\n"
     for i in range(1, pdf.getNumPages()):
        content += pdf.getPage(i).extractText() + "\n"
     print(content)
else:
    content = response.read().decode('utf8',errors='ignore')
    print("n")

t=(timex.tag(content))
year=[]
data=[]
nme=url.rsplit('/', 1)[-1]
name="TimeOpedia of "+nme

sId=whenhubApi.createSchedule(nme)
for x in t:
 if x.isdigit() and int(x)<2100 and int(x)>100:
       year.append(int(x))
year.sort()
print(year)
for y in year:
    y=str(y)
    for sentence in content.split('.'):
      if y in sentence:
       tagged_sent = pos_tag(sentence.split())
       propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
       verbs = [word for word,pos in tagged_sent if pos == 'VBD']
       adj = [word for word,pos in tagged_sent if pos == 'ADJ']
       data=(str(propernouns+verbs+adj))
       eId=whenhubApi.addEvent(sId,y,data)

wId=whenhubApi.addWhencast(sId,name)

finalUrl="https://studio.whenhub.com/schedules/"+sId+"/"+name

print(finalUrl)


        
          


