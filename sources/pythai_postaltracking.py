import requests
from bs4 import BeautifulSoup

def tracking_status(tracking_id) :
    url = 'https://track.aftership.com/thailand-post/'+tracking_id
    html_doc = requests.get(url).content.decode('utf-8')
    soup = BeautifulSoup(html_doc,'html.parser')
    recent_list = soup.find_all('strong')[:2]
    print (recent_list)
    if len(recent_list) > 0 :
        date = recent_list[0].text
        status = recent_list[1].text
        return (date,status)
    return None
