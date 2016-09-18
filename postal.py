import requests
from bs4 import BeautifulSoup

def tracking_status(tracking_id) :
    url = 'https://track.aftership.com/thailand-post/'+tracking_id
    html_doc = requests.get(url).content.decode('utf-8')
    soup = BeautifulSoup(html_doc,'html.parser')
    recent_list = soup.find_all('strong')[:2]
    date = recent_list[0].text
    status = recent_list[1].text
    return (date,status)

tracking_id = input('Input Your Tracking_id (EMS Only) : ')
date_status = tracking_status(tracking_id)
print ('%s %s %s'%(date_status[0],tracking_id,date_status[1]))
