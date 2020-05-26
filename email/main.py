import smtplib
import datetime
from bs4 import BeautifulSoup
import requests
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    #spiker321!
    server.login('spiker.python@gmail.com', 'spiker321!')
    date = datetime.date.today()

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    page = requests.get('https://weather.com/weather/today/l/50.12,18.96?par=google&temp=c', headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        temp_high = float(soup.find(class_='deg-hilo-nowcard').get_text()[:2])
        temp_high = str(round((temp_high-32)/1.8, 1)) + 'C'
    except ValueError:
        temp_high = "unknown"

    rain_chance = soup.find(class_='precip-val').get_text()
    location = str(soup.find(class_='h4 today_nowcard-location').get_text()).split()[0][:-1]
    final = ""
    if temp_high != "unknown":
        if float(temp_high[:-1]) > 30:
            final += "Wow! Today it's gonna be really hot! Remember to drink plenty of fluids!\n"
        elif float(temp_high[:-1]) > 20:
            final += "Nice weather today! Enjoy your day!\n"
        elif float(temp_high[:-1]) > 10:
            final += "It's not very hot but you can still go outside!\n"
        elif float(temp_high[:-1]) > 0:
            final += "It's chilly today. Remember to wear a hat!\n"
        elif float(temp_high[:-1]) > -10:
            final += "It's cold! Dress warm and don't forget gloves\n"
        elif float(temp_high[:-1]) > -20:
            final += "Wow! Stay home, leave only if you must!\n"
        elif float(temp_high[:-1]) > -30:
            final += "Don't go outside! You'll freeze\n"

    if int(rain_chance[:-1]) > 60:
        final += "It will rain! Take an umbrella!"
    elif int(rain_chance[:-1]) > 40:
        final += "It can rain today! Make sure you have a hood in your jacket!"
    else:
        final += "It probably won't rain today!"

    subject = f"Beautiful day {str(date)[6:]}!"
    body = f"Good morning!\nIt's {days[datetime.datetime.today().weekday()]}, {str(date)[8:]} of {months[int(str(datetime.datetime.today())[5:7])-1]}!\nWeather for {location}: Highest temperature is {temp_high}, chance of rain is {rain_chance}.\n{final}"
    msg = f"Subject: {subject}\n\n{body}"
    #Katarzyna_sek@interia.eu
    server.sendmail('spiker.python@gmail.com', 'krzysztofzduniak2@gmail.com', msg)
    print("Email sent!")
    server.quit()


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
send_mail()
print(days[datetime.datetime.today().weekday()], end=" ")
print(months[int(str(datetime.datetime.today())[5:7])-1])


