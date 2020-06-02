from tkinter import *
import requests
from bs4 import BeautifulSoup
import datetime
root = Tk()
root.title("Weather app")
root.geometry("200x20")


def compare(status):
    page1 = requests.get(url, headers=headers)
    soup = BeautifulSoup(page1.content, 'html.parser')
    change = soup.find(class_="index").get_text().strip()
    if int(status) != int(change):
        print(change)
        status = change
        statusLabel = Label(root, text=status)
        statusLabel.grid(row=0, column=2)

try:
    url = "https://umtychy.pl/powietrze-w-tychach"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    place = soup.find(class_="header").get_text().strip()[:-1]
    status = soup.find(class_="index").get_text().strip()
    print(status)
    print(place)
    placeLabel = Label(root, text=place)
    placeLabel.grid(row=0, column=1)
    dateLabel = Label(root, text=datetime.date.today())
    dateLabel.grid(row=0, column=0)
    statusLabel = Label(root, text=status)
    statusLabel.grid(row=0, column=2)
    startButton = Button(root, text="Update", command=lambda: compare(status))
    startButton.grid(row=0, column=3)
    root.mainloop()

except Exception as e:
    print("Error")






