import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
links=[]
Companies=[]
Skills=[]
More_info=[]
job_function=[]
request=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').content
soup=BeautifulSoup(request,'lxml')
jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
for job in jobs :
     
     date=job.find('span',class_='sim-posted').text
     if 'few' in date:
         company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
         skills=job.find('span',class_='srp-skills').text.replace(' ','')
         more_info=job.header.h2.a['href']
         Companies.append(company_name)
         Skills.append(skills)
         More_info.append(more_info)
         links.append(more_info)
for link in links:
    request=requests.get(link).text
    soup=BeautifulSoup(request,'lxml')
    works=soup.find_all('div',class_='wht-shd-bx jd-more-dtl')
    for work in works:
        
        job_fun=work.find('ul',class_='clearfix').text.replace(' ','')
        job_function.append(job_fun)
file_list=[links,Companies,Skills,More_info,job_function]
exported=zip_longest(*file_list)
with open('D:/new.csv','w') as myfile: 
    wr=csv.writer(myfile)
    wr.writerow(['links','Companies','Skills','more_info','job function'])
    wr.writerows(exported)
              
