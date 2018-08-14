import prettytable
import webbrowser
import requests
import time
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from time import sleep

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

    



def semchoose(url,ch):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')

    t=PrettyTable(['No','Available Assessments'])  
    div=soup.findAll('div', id="aspect_artifactbrowser_CommunityViewer_div_community-view")
    ul=div[0].findAll('ul')
    if ch<=6:
	    li=ul[3].findAll("li")
    else:
	    li=ul[2].findAll("li")
    #li=ul[1].findAll('li')

    for i in range(len(li)):
        t.add_row([i+1,li[i].a.text.strip()])
    t.align = "l"
    print(t)  
    ch=int(input("Enter your choice: "))
    url='http://dspace.amritanet.edu:8080/'
    url+=li[ch-1].a['href']
    year(url)



url="http://dspace.amritanet.edu:8080/xmlui/handle/123456789/"
flag=1
try:    
    page = requests.get(url)

except:
    print("Oops!! You're not connected to Amrita Wi-Fi :( !! \nExiting in few seconds... ")
    flag=0
    sleep(5)
    

if(flag==1):
    print("Hello! This was developed by Rajkumar. Have a look at your question papers without wasting time !! ")
    t=PrettyTable(['No','Courses'])
    t.add_row(["1","B.Tech"])
    t.add_row(["2","BA Communication"])
    t.add_row(["3","MA Communication"])
    t.add_row(["4","Integrated MSc & MA"])
    t.add_row(["5","MCA"])
    t.add_row(["6","MSW"])
    t.add_row(["7","M.Tech"])
    t.align="l"
    print(t)
    ch=int(input("Enter your choice : "))
    if(ch==1) : 
      url+="150"
    elif(ch==2) : 
      url+="893"
    elif(ch==3) : 
      url+="894"
    elif(ch==4) : 
      url+="903"
    elif(ch==5) : 
      url+="331"
    elif(ch==6) : 
      url+="393"
    elif(ch==7) : 
      url+="279"

    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')

    

    t=PrettyTable(['No','Semesters'])
    div=soup.findAll('div', id="aspect_artifactbrowser_CommunityViewer_div_community-view")
    li=div[0].ul.findAll('li')

    for i in range(len(li)):
        t.add_row([i+1,li[i].a.text.strip()])
    t.align = "l"
    print(t)
    ch=int(input("Enter your semester : "))
    url='http://dspace.amritanet.edu:8080/'
    url+=li[ch-1].a['href']
    semchoose(url,ch)
