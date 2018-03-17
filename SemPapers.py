import prettytable
import webbrowser
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

def year(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')

    
    div=soup.findAll('div', xmlns="http://di.tamu.edu/DRI/1.0/")
    ul=div[0].findAll('ul')
    li=ul[0].findAll('li')
    hyper=li[0].a['href']
    url='http://dspace.amritanet.edu:8080/'
    url+=hyper
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    t=PrettyTable(['No','Subjects']) 
    div=soup.findAll('div', class_="file-list")
    subdiv=div[0].findAll('div',class_="file-wrapper clearfix")
    for i in range(len(subdiv)):
        title=subdiv[i].findAll('div')
        span=title[1].div.findAll('span')
        t.add_row([i+1,span[1]['title']])
    t.align='l'
    print(t)
    ch=int(input("Enter your choice: "))
    title=subdiv[ch-1].findAll('div')
    link=title[0].a['href']
    url='http://dspace.amritanet.edu:8080/'
    url+=link
    webbrowser.open_new_tab(url)

    



def semchoose(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')

    t=PrettyTable(['No','Available Assessments'])  
    div=soup.findAll('div', id="aspect_artifactbrowser_CommunityViewer_div_community-view")
    ul=div[0].findAll('ul')
    li=ul[1].findAll('li')

    for i in range(len(li)):
        t.add_row([i+1,li[i].a.text.strip()])
    t.align = "l"
    print(t)  
    ch=int(input("Enter your choice: "))
    url='http://dspace.amritanet.edu:8080/'
    url+=li[ch-1].a['href']
    year(url)



url="http://dspace.amritanet.edu:8080/xmlui/handle/123456789/150"
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

print("Hello! This was developed by Rajkumar. Have a look at your question papers without wasting time !! ")

t=PrettyTable(['Semesters'])
div=soup.findAll('div', id="aspect_artifactbrowser_CommunityViewer_div_community-view")
li=div[0].ul.findAll('li')

for i in range(len(li)):
    t.add_row([li[i].a.text.strip()])
t.align = "l"
print(t)
ch=int(input("Enter your semester : "))
url='http://dspace.amritanet.edu:8080/'
url+=li[ch-1].a['href']
semchoose(url)

