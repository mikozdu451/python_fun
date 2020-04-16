import requests
import time
from datetime import datetime

url = "https://platforma.polsl.pl/rau2/login/index.php"
heavy = {'username': 'mikozdu451', 'password': 'kXAMXoe4'}
with requests.Session() as f:
    post = f.post(url, data = heavy)
    szuber = f.get('https://platforma.polsl.pl/rau2/course/view.php?id=980')
    print(szuber.status_code)
    stop = datetime.now()
    stop = stop.replace(hour=21, minute=35, second=0)
    while datetime.now() < stop:
        if szuber.status_code == 200:
            time.sleep(60)
        print("Refreshing")
        szuber = f.get('https://platforma.polsl.pl/rau2/course/view.php?id=980')


