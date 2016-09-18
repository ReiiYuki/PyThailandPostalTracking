import requests
from bs4 import BeautifulSoup

tracking_id = input('Input Your Tracking_id (EMS Only) : ')
url = 'https://track.aftership.com/thailand-post/'+tracking_id
html_doc = requests.get(url).content.decode('utf-8')
soup = BeautifulSoup(html_doc,'html.parser')
recent_list = soup.find_all('strong')[:2]
date = recent_list[0].text
status = recent_list[1].text
print ('%s %s %s'%(date,tracking_id,status))
