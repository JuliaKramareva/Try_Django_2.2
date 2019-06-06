from bs4 import BeautifulSoup
import requests

url = "https://boston.craigslist.org/search/sof"
response = requests.get(url)
assert response.status_code == 200
# print(response)
data = response.text
# print(data)
soup = BeautifulSoup(data, 'html.parser')
# tags = soup.find_all('a')a
# for tag in tags:
#     print(tag.get('href'))
titles = soup.find_all("a", {"class":"result-title"})
# for title in titles:
#     print(title.text)

adresses = soup.find_all("span", {"class":"result-hood"})

# for adress in adresses:
#     print(adress.text)

jobs = soup.find_all('p', {"class":{'result-info'}})

for job in jobs:
    title = job.find('a', {'class':'result-title'}).test
    location_tag = job.find('span', {'class':'result-hood'})
    location = location_tag.text[2:-1] if location_tag else 'N/A'
    date = job.find('time', {'class':'result-date'}).text
    link = job.find('a', {'class':'result-title'}).get('href')
    job_response = requests.get(link)
    job_data = job_response.text
    job_soup = BeautifulSoup(job_data, 'html.parser')
    job_descriotion = job_soup.find('section', {'id': 'postingbody'}).text
    job_attributes_tag = job_soup.find('p', {'class': 'attrgroup'})
    job_attributes = job_attributes_tag.text if job_attributes_tag else 'N/A'


    print('Job Title:', title, '\nLocation', location, '\nDate:', date, '\nlink', link, '\n', job_attributes, '\nJob Description',
          )