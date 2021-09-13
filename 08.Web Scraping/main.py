import requests
from bs4 import BeautifulSoup
import pandas
r = requests.get("https://dev.bg/company/jobs/python/")
c = r.content
soup = BeautifulSoup(c,"html.parser")

all_jobs_titles = soup.find_all("div",{"class":"job-list-item"})
all_jobs_company = soup.find_all("span",{"class":"company-name"})

list_company_names = []
list_job_titles = []
list_dates_of_publish = []

dict_info = {}

for company in all_jobs_company:
    list_company_names.append(company.text)


for job in all_jobs_titles:

    titles = job.find("h6",{"class":"job-title"}).text
    date = job.find("span",{"class":'date'}).text

    list_job_titles.append(titles)
    list_dates_of_publish.append(date)

for c, j, d in zip(list_company_names,list_job_titles,list_dates_of_publish):
    dict_info[c] = [j, d]
    # dict_info[c] = d


df =pandas.DataFrame(dict_info)

df.to_csv("Output.csv")
# for k,v in dict_info.items():
#     print (f"{k} - {v}")